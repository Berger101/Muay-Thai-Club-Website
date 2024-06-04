document.addEventListener("DOMContentLoaded", function () {
  function sendMail(contactForm) {
    emailjs.init(window.emailjsConfig.publicKey);

    emailjs
      .send(window.emailjsConfig.serviceID, window.emailjsConfig.templateID, {
        from_name: contactForm.name.value,
        to_name: contactForm.emailaddress.value,
        message: contactForm.message.value,
      })
      .then(
        function (response) {
          console.log("SUCCESS", response);
          alert("Your message was sent successfully!");
        },
        function (error) {
          console.log("FAILED", error);
          alert("There was an error sending your message. Please try again later.");
        }
      );
    return false; // To block from loading a new page
  }

  // Attach the sendMail function to the form submit event
  document.querySelector("form").onsubmit = function () {
    return sendMail(this);
  };
});
