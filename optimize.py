import plotly
import plotly.graph_objs as go
import numpy as np
import torch
from hyperopt import fmin, hp, tpe
import torch_optimizer as optim
from landscapes import *
from configs import *
from functools import partial

def execute_steps(
    func, initial_state, optimizer_class, optimizer_config, num_iter
):
    x = torch.Tensor(initial_state).requires_grad_(True)
    optimizer = optimizer_class([x], **optimizer_config)
    steps = []
    steps = np.zeros((2, num_iter + 1))
    steps[:, 0] = np.array(initial_state)
    for i in range(1, num_iter + 1):
        optimizer.zero_grad()
        f = func(x,torch)
        f.backward(retain_graph=True)
        torch.nn.utils.clip_grad_norm_(x, 1.0)
        optimizer.step()
        steps[:, i] = x.detach().numpy()
    return steps

def compute_min(x,y,steps):
    return (steps[0][-1] - x) ** 2 + (steps[1][-1] - y) ** 2


def objective_fn(land_scape_fn,initial_state,minimum,num_iter,params):
    lr = params['lr']
    optimizer_class = params['optimizer_class']
    optimizer_config = dict(lr=lr)
    steps = execute_steps(
        land_scape_fn, initial_state, optimizer_class, optimizer_config, num_iter
    )
    return  min([compute_min(x,y,steps) for (x,y,z) in minimum])


def execute_experiments(
    optimizer_config, ls_func, initial_state, minimum,num_iter,max_evals
):
    seed = 1
    optimizer_class, lr_low, lr_hi = optimizer_config
    space = {
        'optimizer_class': hp.choice('optimizer_class', [optimizer_class]),
        'lr': hp.loguniform('lr', lr_low, lr_hi),

    }
    try:
        objective=partial(objective_fn,ls_func,initial_state,minimum,num_iter)
        best = fmin(
            fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=max_evals,
            rstate=np.random.RandomState(seed),
        )
    except:best={'lr':1}
    steps = execute_steps(
        ls_func,
        initial_state,
        optimizer_class,
        {'lr': best['lr']},
        num_iter=num_iter,
    )
    return steps,best['lr']



