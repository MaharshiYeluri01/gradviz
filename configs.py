
import numpy as np
pi=np.pi
e=np.e
configs={
  'ackley':{'bounds':[(-5,5),(-5,5)],'minima':[(0,0,0)]},
  'bartels_conn':{'bounds':[(-50,50),(-50,50)],'minima':[(0,0,1)]},
  'beale':{'bounds':[(-4.5,4.5),(-4.5,4.5)],'minima':[(3,0.5,0)]},
  'booth':{'bounds':[(-10,10),(-10,10)],'minima':[(1,3,0)]},
  'branin':{'bounds':[(-5,10),(0,15)],'minima':[(-pi, 12.275,0.397887),(pi, 2.275,0.397887),(9.42478, 2.475,0.397887)]},
  'bukin_n6':{'bounds':[(-15,-5),(-3,3)],'minima':[(-10,1,0)]},
  'camel_hump_3':{'bounds':[(-5,5),(-5,5)],'minima':[(0,0,0)]},
  'camel_hump_6':{'bounds':[(-3,3),(-2,2)],'minima':[(0.0898, -0.7126, -1.0316),(-0.0898,  0.7126, -1.0316)]},
  'drop_wave':{'bounds':[(-5.12,5.12),(-5.12,5.12)],'minima':[(0,0,-1)]},
  'himmelblau':{'bounds':[(-5,5),(-5,5)],'minima':[(3.0, 2.0,0),(-2.805118, 3.131312,0),(-3.779310, -3.283186,0),(3.584428, -1.848126,0)]},
  'eggholder':{'bounds':[(-512,512),(-512,512)],'minima':[(512,404.2319,-959.6407)]},
  'holder_table':{'bounds':[(-12,12),(-12,12)],'minima':[ (8.05502,9.66459,-19.2085),(-8.05502,9.66459,-19.2085),(8.05502,9.66459,-19.2085),(-8.05502,9.66459,-19.2085)]},
  'rosenbrock':{'bounds':[(-2,2),(-2,2)],'minima':[(1,1,0)]},
  'rastrigin':{'bounds':[(-5.12,5.12),(-5.12,5.12)],'minima':[(0,0,0)]}
  
}
optimizers = {
# baselines
"Adam":("torch.optim.Adam", -8, 0.5),
"SGD":("torch.optim.SGD", -8, -1.0),
# Adam based
"AdaBound":("optim.AdaBound", -8, 0.3),
"AdaMod":("optim.AdaMod", -8, 0.2),
"AdamP":("optim.AdamP", -8, 0.2),
"DiffGrad":("optim.DiffGrad", -8, 0.4),
"Lamb":("optim.Lamb", -8, -2.9),
"NovoGrad":("optim.NovoGrad", -8, -1.7),
"RAdam":("optim.RAdam", -8, 0.5),
"Yogi":("optim.Yogi", -8, 0.1),
# SGD/Momentum based
"AccSGD":("optim.AccSGD", -8, -1.4),
"SGDW":("optim.SGDW", -8, -1.5),
"SGDP":("optim.SGDP", -8, -1.5),
"PID":("optim.PID", -8, -1.0),
"QHM":("optim.QHM", -6, -0.2),
"QHAdam":("optim.QHAdam", -8, 0.1),
"Ranger":("optim.Ranger", -8, 0.1),
"RangerVA":("optim.RangerQH", -8, 0.1),
"RangerVA":("optim.RangerVA", -8, 0.1),
"Shampoo":("optim.Shampoo", -8, 0.1),
"LookaheadYogi":("LookaheadYogi", -8, 0.1),
"AggMo":("optim.AggMo", -8, -1.5),
"SWATS":("optim.SWATS", -8, -1.5),
"Adafactor":("optim.Adafactor", -8, 0.5)}


