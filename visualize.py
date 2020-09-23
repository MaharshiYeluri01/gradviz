from optimize import *
import json

def createJson(trace):
    return json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

def plotLandScape(landscape):
    con=configs[landscape]
    (x1,x2),(y1,y2)=con['bounds']
    minima=np.array(con['minima'])
    x = np.linspace(x1, x2, 50)
    y = np.linspace(y1,y2, 50)
    X, Y = np.meshgrid(x, y)
    ls_func=eval(landscape)
    Z = ls_func([X, Y],lib=np)
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y,showscale=False,),go.Scatter3d(x=minima[:,0],y=minima[:,1],z=minima[:,2])])
    
    return fig


def dynamicLandscape(ls,lr_search,params):
    minimum=np.array(configs[ls]['minima'])
    init_x,init_y=params['x'],params['y']
    optimizer_config=params['optim']
    optimizer,minLR,maxLR=optimizers[optimizer_config]
    func=eval(ls)
    if lr_search:
        steps,lr=execute_experiments((eval(optimizer),minLR,maxLR),func,(init_x,init_y),minimum,params['iters'],params['evals'])
    else:
        lr=params['lr']
        steps = execute_steps(
        func,
        (init_x,init_y),
        eval(optimizer),
        {'lr': lr},
        num_iter=params['iters'],
        )

    (x1,x2),(y1,y2)=configs[ls]['bounds']
    x = np.linspace(x1, x2, 50)
    y = np.linspace(y1,y2, 50)

    X, Y = np.meshgrid(x, y)
    Z = func([X, Y],np)
    X,Y,Z=X.tolist(),Y.tolist(),Z.tolist()
    z=func([steps[0,:],steps[1,:]],np)
    x,y,z=(steps[0,:],steps[1,:],z)
    minimum=minimum.astype(float)
    min_x,min_y=minimum[:,0],minimum[:,1]
    min_z=func([min_x,min_y],np)
    return (x,y,z),go.Surface(z=Z, x=X, y=Y),[list(min_x),list(min_y),list(min_z)],lr