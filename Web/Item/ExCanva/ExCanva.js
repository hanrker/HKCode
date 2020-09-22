let isDrawing = false;
let can=document.getElementById("HCan");
var cxt=can.getContext("2d");

var lastPointX,lastPointY;
   
function CanCor(){
        
}


 function GetCor(){
    x = s.clientX;
    y = s.clientY;
    document.getElementById("cor").innerHTML="x:"+ x+";"+"y:"+y;
}


function Start(){
    isDrawing = true;
    console.log(isDrawing);
}
let isFisrt = true;
function LineDrawing(){
    let x,y;
    x = event.x -can.offsetLeft;
    y = event.y -can.offsetTop;
    console.log("x:"+ x+";"+"y:"+y);
    if (isDrawing){
            if (isFisrt){
                cxt.moveTo(x,y);
                isFisrt = false;
                console.log("第一个点");
            }else{
                cxt.lineTo(x,y);
                isFisrt = true;
                console.log("第二个点");
                cxt.stroke();
            }
            lastPointX = x;
            lastPointY = y;
    }
    }
   function LineReadyDrawing(){
    if (isDrawing && !isFisrt){
        let cxtYL = can.getContext("2d");
      
        let x,y;
        x = event.x -can.offsetLeft;
        y = event.y -can.offsetTop;

        cxtYL.moveTo(lastPointX,lastPointY);
        cxtYL.lineTo(x,y);

        cxt.stroke();
        } 
    }