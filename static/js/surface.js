var i = 0
let iters=line_data['iters']
var redraw = true
var x = [0], y = [0], z = [0],c=[0];
var min=line_data['min']
var min = {

    marker: {

        'colorscale': 'oranges',
        'size': 6
    },
    type: 'scatter3d',
    x: min[0],
    y: min[1],
    z: min[2],
    mode: 'markers'
}
var data = [{

    line: { color: c, width: 5,colorscale: "Aggrnyl" },
    marker: {

        color: c,
        size: 2,
        colorscale: "Aggrnyl"
        
    },
    type: 'scatter3d',
    x: x,
    y: y,
    z: z,
    mode: 'lines+markers'
}, min, surface_data]

var layout = {
    showlegend: false,
    showscale: false,
    height: 640,
}

var config = { displayModeBar: false, format: 'svg' }

Plotly.plot('graph', data, layout, config)


var cx = document.querySelector('#x');
var cy = document.querySelector('#y');
var cz = document.querySelector('#z');
var iter = document.querySelector('#iter');


function color(n){
    var carray=[]
        for(c=0;c<n;c++){
            carray.push(c)
        }
        return carray
    }

function compute() {
    i = i + 1
    x = line_data.x.slice(0, i)
    y = line_data.y.slice(0, i)
    z = line_data.z.slice(0, i)
    c=color(i)

   
}

var check_pause=true
var button=document.getElementById("pause_play")
function pauseAnimation(){
    if (check_pause==true){
        check_pause=false 
        button.value="Continue"; 
    }
    else{
        check_pause=true
        button.value="Adjust View"
        requestAnimationFrame(update,);
        requestAnimationFrame(line_update);


    }
}

function update() {
    compute();
    Plotly.animate('graph', {
        data: [{

            line: { color: c, width: 5,colorscale: "Aggrnyl" },
            marker: {
                color: c,
                size: 2,
                colorscale: "Aggrnyl"
            },
            type: 'scatter3d', x: x, y: y, z: z
        }, min, surface_data]
    }, {
        transition: {
            duration: 0,
        },
        frame: {
            duration: 0,
            redraw: redraw,
        }
    });
    if (i<iters && check_pause){
    cx.textContent = line_data.x[i].toString();
    cy.textContent = line_data.y[i].toString();
    cz.textContent = line_data.z[i].toString();
    iter.textContent = 'ITER :'+i.toString()+'/'+iters;

        requestAnimationFrame(update);

    }
    else if(check_pause && i>=iters){
        alert("Done rendering!")
    }
}

requestAnimationFrame(update,);

