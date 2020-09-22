var can = document.getElementById("can");
// var cxt = can.getContext('2d');
// cxt.fillStyle = "#FF0000";
// cxt.fillRect(0,0,100,200);

// document.designMode = 'on';//编辑文档
h = document.getElementById("han");
var inp = document.getElementById("inp");
function hide(){
    h.setAttribute("hidden",true);
    console.log("sd");
    // h.removeAttribute("hidden");
    // h.hidden="hidden";
    
}
function GetFocus(){
    var inp = document.getElementById("inp");
    console.log("focus");
    inp.focus();
}

//闭包
function BiBao(){
    var a = 2;
    var b = 21;
    function a1(){
        console.log(b);
    }
    a1();
    console.log(a=>a*2);
    // // console.log(b);
    // console.log(this);
    let fn3 = (a, b) => a + b;
    console.log(fn3(1,6));
    alert(fn3(1,6));
    
    var id ="11s";
    console.log(
        (id => {
        return {
            say() {
            console.log(id);
            },
            aaa: id+1
        };
        })(20).aaa
    ); 
}

