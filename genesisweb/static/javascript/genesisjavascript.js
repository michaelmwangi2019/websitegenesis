
//Get to the topbutton
//onscrollfunction for the transparent box in the home page ie mwangaza wa jamii
//scroll function for the homepage elements

var mybutton = document.getElementById("myBtnup");
var mytextarea = document.getElementById("mytext");
var myanimation = document.getElementById("soberexp");
var myanimation2 = document.getElementById("imagesoberexp");
var myanimation3 = document.getElementById("titlesoberexp");

// When the user scrolls down 500px from the top of the document, show the button
//when user scrolls animate the home page elements

window.onscroll = function() {scrollFunction};

function scrollFunction() {
    if (document.body.scrollTop > 450 || document.documentElement.scrollTop > 450) {
    mybutton.style.display = "block";
    mytextarea.style.display = "none";
  }
  else {
    mybutton.style.display = "none";
    mytextarea.style.display = "block";
}

    }

// When the user clicks on the button, scroll to the top of the document
function topFunction2() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
    }

function scrollFunction2() {
  if (document.body.scrollTop >= 150 || document.documentElement.scrollTop >= 150) {
    myanimation.className = "slide-up-fade-in";
    myanimation2.className = "slideLeft";
    myanimation3.className = "slideRightLeft";
  }
  else {
    document.getElementById("soberexp").className = "";
    document.getElementById("imagesoberexp").className = "";
    document.getElementById("titlesoberexp").className = "";
  }

}


/**********************************************************************************
<script>
//Get the button
var mybutton = document.getElementById("myBtnup");
var mytextarea = document.getElementById("mytext");
var myanimation = document.getElementById("soberexp");
var myanimation2 = document.getElementById("imagesoberexp");
var myanimation3 = document.getElementById("titlesoberexp");

// When the user scrolls down 450px from the top of the document, show the button
window.onscroll = function() {scrollFunction2(),scrollFunction()};

function scrollFunction() {

  if (document.body.scrollTop >= 450 || document.documentElement.scrollTop >= 450){
    mybutton.style.display = "block";
    mytextarea.style.display = "none";
    }
   else {
    mybutton.style.display = "none";
    mytextarea.style.display = "block";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

function scrollFunction2() {
  if (document.body.scrollTop >= 150 || document.documentElement.scrollTop >= 150){
    myanimation.className = "slide-up-fade-in";
    myanimation2.className = "slideLeft";
    myanimation3.className = "slideRightLeft";
  }
  else {
    myanimation.className = "";
    myanimation2.className = "";
    myanimation3.className = "";
  }
  }
</script>
**********************************************************************************/