function loadXMLDoc(url){
    var xmlhttp;
    var txt,x,i;
    xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
            xmlDoc=xmlhttp.responseXML;
            txt="";
            x=xmlDoc.getElementsByTagName("title");
            for (i=0;i<x.length;i++)
            {
            txt=txt + x[i].childNodes[0].nodeValue + "<br />";
            }
            document.getElementById("myDiv").innerHTML=txt;
            }
    };
   
    // var a =  xmlhttp.open("GET","http://127.0.0.1:8011/h.html",true);
    var a =  xmlhttp.open("GET",url,true);

    xmlhttp.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
    // var x=  xmlhttp.setRequestHeader("Access-Control-Allow-Origin","*");
    console.log(xmlhttp.responseText);
    xmlhttp.send();
    return xmlhttp.responseXML;
}


function Cal(){

    a = document.getElementById('n1');
    b = document.getElementById("n2");

    res = document.getElementById("res");
    var xmlhttp =  Get("http://127.0.0.1:8011/WebApplication2/Cal");
    

    res.innerHTML =Number(a.value) +Number(b.value);
}

function Get(url){
    var xmlhttp;
    var txt,x,i;
    xmlhttp = new XMLHttpRequest();

    var a =  xmlhttp.open("GET",url,true);

    xmlhttp.send();
    return xmlhttp.responseXML;
}

function GetText (url){

}