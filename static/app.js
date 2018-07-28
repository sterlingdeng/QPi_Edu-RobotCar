const robotController = async input => {
  const endpoint = window.location.href + "control?q=" + input;
  const response = await fetch(endpoint);
  console.log(response.text());
};

$(document).ready(() => {
  $("#forward").on("click", () => {
    robotController("forward");
  });
  $("#left").on("click", () => {
    robotController("left");
  });
  $("#right").on("click", () => {
    robotController("right");
  });
  $("#backward").on("click", () => {
    robotController("backward");
  });
  $("#stop").on("click", () => {
    robotController("stop");
  });

  $(document).keydown(e => {
    if (e.keyCode == 37) {
      // left
      robotController("left");
    } else if (e.keyCode == 38) {
      // up
      robotController("forward");
    } else if (e.keyCode == 39) {
      // right
      robotController("right");
    } else if (e.keyCode == 40) {
      // down
      robotController("backward");
    } else if (e.keyCode == 83) {
	// stop
	robotController("stop");	 
    } else {
      return;
    }
    e.preventDefault();
  });
});
