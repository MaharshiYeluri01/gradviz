
Plotly.plot('line', [data[0],data[1]], layout, config)





var layout = {
    showlegend: false,
    showscale: false,
    height: 640,
}


function line_update() {
    Plotly.animate('line', {
    data: [{
        line: { color: c, width: 5,colorscale: "Aggrnyl" },
            markers:{
            color: c,
        size: 2,
        colorscale: "Aggrnyl"
        },
       
        type: 'scatter3d', x: x, y: y, z: z
    }, min]
}, {
    transition: {
        duration: 1,
    },
    frame: {
        duration: 1,
        redraw: redraw,
    }
});

if (i<500 && check_pause){
   
        requestAnimationFrame(line_update);

    }
    else{
        
    }
}

requestAnimationFrame(line_update,);