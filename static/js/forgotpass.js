function forgotvalidate(data) {
  let status = false;

  if (data.name === "email" || data.id === "forgotpass-form") {
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
  if (data.id === "forgotpass-form") {
    const emailPattern = /^[a-z]*[0-9]*\@[a-z]*\.[a-z]*$/;
    let password = document.getElementById("password");
    let forgotpass = document.getElementById("forgotpass-inputs");
    let passError = document.getElementById("pass-error")
    if (password.value == "Harsh@123") {
        forgotpass.innerHTML = `<div class="mb-4">
                            <label for="exampleFormControlInput1" class="form-label">New Password</label>
                            <input type="text" class="form-control" id="npassword" name="npassword"
                                onchange="forgotvalidate(this)">
                        </div>
                        <div class="mb-4">
                            <label for="exampleFormControlInput1" class="form-label">Confirm Password</label>
                            <input type="text" class="form-control" id="cpassword" name="cpassword"
                                onchange="forgotvalidate(this)">
                        </div>

                        <div class="forgotpass-button">
                            <input type="submit" class="form-control  w-100 text-center" value="Change Password">
                        </div>`
    } else {
      password.classList.add("is-invalid");
      passError.innerHTML = "Wrong Password!"
      status = false;
    }
  }

  if (status == true) {
    return true;
  } else {
    return false;
  }
}
function changetoOtp(link) {

  let forgotpass = document.getElementById("forgotpass-inputs");
  if (link.value === "fvo") {
    forgotpass.innerHTML = `<div class="forgotpass-inputs" id="forgotpass-inputs">
                      <div class="mb-4">
                          <label for="exampleFormControlInput1" class="form-label">Email</label>
                          <input type="email" class="form-control" id="email" name="email"
                              onchange="forgotvalidate(this)">
                      </div>
                      <div class="forgotpass-button">
                          <input type="submit" class="form-control  w-100 text-center" value="Send OTP">
                      </div>
                      <div class="via-otp pt-3 text-center">
                          <button type="button" class="text-primary m-0" value="fvp" onclick="changetoOtp(this)">Forgot via Previous Password</button>
                      </div>
                  </div>`
    
  }
  if (link.value === "fvp") {
    forgotpass.innerHTML = `<div class="mb-4">
                            <label for="exampleFormControlInput1" class="form-label">Email</label>
                            <input type="email" class="form-control" id="email" name="email"
                                onchange="forgotvalidate(this)">
                        </div>
                        <div class="mb-4">
                            <label for="exampleFormControlInput1" class="form-label">Password</label>
                            <input type="text" class="form-control" id="password" name="password"
                                onchange="forgotvalidate(this)">
                                <span id="pass-error" class="text-danger pt-2"></span>
                        </div>
                        <div class="forgotpass-button">
                            <input type="submit" class="form-control  w-100 text-center" value="Verify Password">
                        </div>
                        <div class="via-otp pt-3 text-center">
                            <button type="button" class="text-primary m-0" onclick="changetoOtp(this)" value="fvo" >Forgot via OTP</button>
                        </div>`
  }
}
