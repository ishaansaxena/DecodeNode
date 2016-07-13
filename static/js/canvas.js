/*
** Landing Canvas
** Inspired from: http://codepen.io/charliekuldip/pen/KCpHn
*/

var landing_canvas, 
    context, 
    canvas_height, canvas_width, 
    cellSize;

function init(){
    landing_canvas = document.getElementById("bodyCanvas");
    context = landing_canvas.getContext("2d");
    canvas_height = landing_canvas.height = document.body.clientHeight;
    canvas_width = landing_canvas.width = document.body.clientWidth;
    cellSize = 100;
    Render();
}


function Render(){
    context.clearRect(0, 0, canvas_width, canvas_height);
    for(var i = 0; i < Math.ceil(canvas_width/cellSize); i++)
        for(var j = 0; j < Math.ceil(canvas_height/cellSize); j++){       
            var pattern = Math.floor(Math.random()*4);
            var lightness = Math.floor(Math.random()*50+25);       
            context.beginPath();      
            if (pattern === 3){
                context.moveTo(i * cellSize, j * cellSize);      
                context.lineTo(i * cellSize + cellSize, j * cellSize);
                context.lineTo(i * cellSize, j * cellSize + cellSize);
            } 
            else if (pattern === 2){
                context.moveTo(i * cellSize + cellSize, j * cellSize + cellSize);      
                context.lineTo(i * cellSize, j * cellSize + cellSize);
                context.lineTo(i * cellSize + cellSize, j * cellSize);
            } 
            else if (pattern === 1){
                context.moveTo(i * cellSize + cellSize, j * cellSize);      
                context.lineTo(i * cellSize + cellSize, j * cellSize + cellSize);
                context.lineTo(i * cellSize, j * cellSize);
            } 
            else {
                context.moveTo(i * cellSize, j * cellSize + cellSize);      
                context.lineTo(i * cellSize, j * cellSize);
                context.lineTo(i * cellSize + cellSize, j * cellSize + cellSize);
            }
            context.fillStyle = 'hsl(141, 36%, ' + lightness + '%)';
            context.closePath();      
            context.fill();
        };
}

window.onload = init;
