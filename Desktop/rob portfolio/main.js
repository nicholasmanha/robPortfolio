const inputs = document.querySelectorAll(".input");

function sendEmail(){
    Email.send({
        Host : "smtp.gmail.com",
        Username : "nickrmanha@gmail.com",
        Password : "Martiangaming11",
        To : 'nickrmanha@gmail.com',
        From : document.getElementById("email").value,
        Subject : "New Contact Form",
        Body : "And this is the body"
    }).then(
      message => alert(message)
    );
}

function focusFunc() {
  let parent = this.parentNode;
  parent.classList.add("focus");
}

function blurFunc() {
  let parent = this.parentNode;
  if (this.value == "") {
    parent.classList.remove("focus");
  }
}

inputs.forEach((input) => {
  input.addEventListener("focus", focusFunc);
  input.addEventListener("blur", blurFunc);
});
$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');

        } else {

            $('.navbar').removeClass('active');

        }
    });
});
