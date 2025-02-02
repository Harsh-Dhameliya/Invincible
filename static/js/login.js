function loginvalidate(data) {
  let status = true;

  if (data.name === "email" || data.id === "log-form") {
    const emailPattern = /^[a-z]*[0-9]*\@[a-z]*\.[a-z]*$/;
    let email = document.getElementById("email");

    if (email.value.length >= 0 && emailPattern.test(email.value)) {
      email.classList.remove("is-invalid");
      email.classList.add("is-valid");
    } else {
      email.classList.remove("is-valid");
      email.classList.add("is-invalid");
      status = false;
    }
  }

  if (data.name === "password" || data.id === "log-form") {
    let password = document.getElementById("password");
    let passError = document.getElementById("pass-error");
    const passwordPattern =
      /[A-Z]/.test(password.value) &&
      /\d/.test(password.value) &&
      /[!@#$%^&*(),.?":{}|<>]/.test(password.value);

    if (
      password.value.length >= 8 &&
      password.value.length <= 12 &&
      passwordPattern
    ) {
      passError.innerHTML = "";
      password.classList.remove("is-invalid");
      password.classList.add("is-valid");
    } else {
      password.classList.remove("is-valid");
      password.classList.add("is-invalid");
      if (data.name === "password") {
        passError.innerHTML =
          "Passord Should be contain A-Z,0-9,Special-character and length of password 8-12";
      }
      status = false;
    }
  }

  if (status == true) {
    return true;
  } else {
    return false;
  }
}
