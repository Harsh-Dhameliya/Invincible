function change_image(src) {
  let stat = document.querySelector(".states");
  if (src == "saputara") {
    stat.style.backgroundImage = "url('../static/images/gj-vav.jpg')";
  } 
  else if (src == "goa") {
    stat.style.backgroundImage = "url('../static/images/goa-2.jpg')";
  } 
  else if (src == "manali") {
    stat.style.backgroundImage = "url('../static/images/uttrakhand-1.jpg')";
  } 
  else if (src == "rajasthan") {
    stat.style.backgroundImage = "url('../static/images/rajasthan-thar-desert.jpg')";
  } 
  else {
    stat.style.backgroundImage = "url('../static/images/jammu-1.jpg')";
  }
}
