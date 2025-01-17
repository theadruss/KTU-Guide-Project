document.addEventListener('DOMContentLoaded', function() {
  // Show the newsletter form when the button is clicked
  document.getElementById('joinNewsletterBtn').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default anchor behavior
    document.querySelector('.slider_section').style.display = 'none'; // Hide the current hero section
    document.querySelector('.subscribe').style.display = 'block'; // Show the newsletter form
  });

  // Handle the newsletter form submission
  document.getElementById('newsletter').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const checkbox = this.querySelector('input[type="checkbox"]');

    if (!checkbox.checked) {
      alert('You must agree to the terms before submitting.');
      return; // Stop if checkbox is not checked
    }

    const formData = new FormData(this); // Create a FormData object from the form

    fetch(this.action, {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': this.querySelector('input[name="csrfmiddlewaretoken"]').value // Include CSRF token
      }
    })
    .then(response => {
      if (!response.ok) {
        return response.json().then(err => { throw new Error(err.error); });
      }
      return response.json();
    })
    .then(data => {
      // Display the thank you message
      const thankYouMessage = document.getElementById('thankYouMessage');
      thankYouMessage.textContent = data.message; // Set the message
      thankYouMessage.style.display = 'block'; // Show the message
      this.reset(); // Optionally reset the form
    })
    .catch(error => {
      alert(error.message); // Show error message if any
    });
  });
});