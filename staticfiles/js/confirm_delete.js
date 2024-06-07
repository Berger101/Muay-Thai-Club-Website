document.addEventListener('DOMContentLoaded', function () {
  var deleteButtons = document.querySelectorAll('.delete-button');

  deleteButtons.forEach(function (button) {
      button.addEventListener('click', function (event) {
          var confirmed = confirm("Are you sure you want to proceed?");
          if (!confirmed) {
              event.preventDefault();
          }
      });
  });
});
