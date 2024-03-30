function show_password(id) {
  var passwordField = document.getElementById(id);
  var passwordInput = passwordField.getElementsByTagName("input")[0];
  var eyeIcon = passwordField.getElementsByTagName("i")[0];

  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    eyeIcon.classList.remove("fa-eye");
    eyeIcon.classList.add("fa-eye-slash");
  } else {
    passwordInput.type = "password";
    eyeIcon.classList.remove("fa-eye-slash");
    eyeIcon.classList.add("fa-eye");
  }
}