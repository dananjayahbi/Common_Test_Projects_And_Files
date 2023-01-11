// get references to the form and input fields
const form = document.querySelector("form");
const username = document.querySelector("#username");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const passwordConfirm = document.querySelector("#password-confirm");

// add a submit event listener to the form
form.addEventListener("submit", (e) => {
  e.preventDefault();
  
  // check if the username is valid
  if (username.value.length < 3) {
    alert("Username must be at least 3 characters long");
    return;
  }

  // check if the email is valid
  if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email.value)) {
    alert("Invalid email address");
    return;
  }

  // check if the password is valid
  if (password.value.length < 8) {
    alert("Password must be at least 8 characters long");
    return;
  }

  // check if the password confirmation matches the password
  if (password.value !== passwordConfirm.value) {
    alert("Passwords do not match");
    return;
  }

  // if all validation checks pass, submit the form
  form.submit();
});