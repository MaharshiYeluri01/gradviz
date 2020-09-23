

from flask import Flask, render_template,request,jsonify,request
import json
from visualize import *
from utils import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
landscape_fns=list(configs.keys())
landscapes_3d=[(ls,plotLandScape(ls)) for ls in landscape_fns]
landscapes_3d_json=createJson(landscapes_3d)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/landscape/optimize/<name>')
def optimize_state(name):

    optim=request.args.get('optim')
    x=float(request.args.get('x'))
    y=float(request.args.get('y'))
    iters=int(request.args.get('iter'))
    param_dict={'optim':optim,'x':x,'y':y,'iters':iters}
    print(param_dict)

    minLR=request.args.get('minLR')

    if minLR:
        minLR=float(minLR)
        maxLR=float(request.args.get('maxLR'))
        evals=int(request.args.get('evals'))
        param_dict['minLR']=minLR
        param_dict['maxLR']=maxLR
        param_dict['evals']=evals
        print(param_dict)

        (x,y,z),surface,minimun,lr=dynamicLandscape(name,True,param_dict)



    lr_val=request.args.get('lr')
    print(param_dict,lr_val)
    if lr_val:
        param_dict['lr']=float(lr_val)
        print(param_dict)
        (x,y,z),surface,minimun,lr=dynamicLandscape(name,False,param_dict)

    return render_template('chart.html',surface=createJson(surface),line=json.dumps({'x':list(x),'y':list(y),'z':list(z),'min':minimun,'iters':iters}),
    title=json.dumps(f"Function : {name}  optimizer: Adam Best LR : {lr}"))



@app.route('/landscapes')
def render_landscapes(): 
    return render_template('landscapes.html',landscapes=landscapes_3d_json,landscape_fns=landscape_fns)

@app.route('/landscape/<name>')
def landscape(name):

    landscape_3d_json= createJson(landscapes_3d[landscape_fns.index(name)])
    return render_template('optimize.html',landscape=landscape_3d_json,ls_name=json.dumps(name),optimizers=optimizers.keys())

if __name__ == '__main__':
    app.run(debug=True)
