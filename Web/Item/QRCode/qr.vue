<template>
    <div id= 'app'>
        <img src="qrcodeurl" alt="">
    </div>
</template>

<script>
import QRCode from "qrcode";
export default {
    name:'app',
    data(){
        return{
            qrcodeUrl:" "
        };
    },
    method(){
        let self = this;
        QRCode.toDataURL(
            "123455",
            {
                errorCorrectionLevel:"H",version:1
            },
            function (err,url){
                if(!err){
                    self.qrcodeUrl = url;
                }
            }
        )
    }
}
</script>