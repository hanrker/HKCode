$("#hide").click(function(){
    $("p#h").fadeTo("slow",0.2);

})

$("#callbb").click(function(){
    $("#callb").hide(1000,()=>{alert("隐藏完成")})
})

$('#lianjie').click(function(){
    $('#lianjeContent').css('color','red').slideUp(2000).slideDown(2000);
})

$("#anim").click(function(){
    $("div#move").animate({ left:'100px', height: '30px', backgroundColor: '#00ee00'});
    $("div#move").animate({ left:'100px', height: '310px', backgroundColor: '#00ee00'},5000);
})

$("#GetV").click(function(){
    // alert($("#v").val()); 
    alert("text:"+$("#title").text().toString()); 
    console.log($("#title").text());
    alert("html:"+$("#title").html().toString()); 
    $("#title").text("sss");
})

$("#rem").click(function(){
    $("#par").remove();
})

$("#emp").click(function(){
    $("#par").empty();
})