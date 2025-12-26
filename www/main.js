$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        in:{
            effect: "bounceIn",
            delayScale:3,
            delay: 2,
        },
        out:{
            effect:"bounceOut",
            delayScale:3,
            delay:2
        }
    });
    //siri configuration

    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style:"ios9",
    amplitude: "1",
    speed: "0.30",
    autostart:true
  });
  //siri message animation
    $('.siri-message').textillate({
        loop: true,
        in:{
            effect: "fadeIn",
            sync: true, 
        },
        out:{
            effect:"fadeOut",
            sync:true,
        }
    });

    //mic button click event
   $("#MicBtn").click(function () { 
    eel.playAssistantSound()
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.takecommand()()
   });
});
