$(document).ready(function () {

  // Initialize textillate ONCE
  $(".siri-message").textillate({
    loop: true,
    in: { effect: "fadeIn", sync: true },
    out: { effect: "fadeOut", sync: true }
  });

  // Expose to Python
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    // update text correctly
    $(".siri-message").text(message);
    // start animation
    $(".siri-message").textillate("start");
  }

});
