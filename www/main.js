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
});