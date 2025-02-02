var counts = 0;
function addperson(e) {
  counts = e;
  let person_info = document.getElementById("person-info");
  person_info.innerHTML = "";
  for (let index = 0; index < e; index++) {
    person_info.innerHTML += ` <div class="person-info-outer">
                                <div class="person-title pb-1">
                                    Participent ${index + 1}
                                </div>
                                <div class="person-info d-flex flex-column gap-2">
                                    <div class="d-flex gap-2">
                                        <div class=" w-50">
                                            <label for="">First Name</label>
                                            <input type="text" class="form-control theme-control"
                                                onkeyup="valiadate(this)" name="fname">
                                        </div>
                                        <div class=" w-50">
                                            <label for="">Last Name</label>
                                            <input type="text" class="form-control theme-control"
                                                onkeyup="valiadate(this)" name="lname">
                                        </div>
                                    </div>
                                    <div class="w-100">
                                        <label for="">Mobile</label>
                                        <input type="text" class="form-control theme-control" onkeyup="valiadate(this)"
                                            name="mobile" maxlength="10">
                                    </div>
                                    <div class="d-flex gap-2">
                                        <div class="w-50">
                                            <label for="">Birth Date</label>
                                            <span name="birthDate"></span>
                                             <input type="date" class="form-control theme-control" onclick="maxdate(this)" name="date" onchange="valiadate(this)">
                                        </div>
                                        <div class=" w-50">
                                            <label for="">Gender</label>
                                            <select class="form-select theme-control"
                                                aria-label="Default select example" name="gender"
                                                onchange="valiadate(this)">
                                                <option selected disabled="disabled" value="Select Gender">Select Gender
                                                </option>
                                                <option value="Male">Male</option>
                                                <option value="Female">Female</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <hr style="border: 1px solid black; margin: 2rem 0px 2rem 0px ;">
                            </div>`;
  }
}

let maxdate = (abc) => {
  // console.log(abc);
  max = new Date().toISOString().slice(0, 10);
  abc.setAttribute("max", max);
};

function valiadate(abc) {
  let status = true;

  if (abc.name === "fname" || abc.id === "myForm") {
    const namePattern = /^[a-zA-Z]+$/;
    let fname = document.getElementsByName("fname");

    // console.log(fname.length);

    for (i = 0; i < fname.length; i++) {
      if (fname[i].value.length >= 0 && namePattern.test(fname[i].value)) {
        fname[i].classList.remove("is-invalid");
        fname[i].classList.add("is-valid");
      } else {
        fname[i].classList.remove("is-valid");
        fname[i].classList.add("is-invalid");
        status = false;
      }
    }
  }

  if (abc.name === "lname" || abc.id === "myForm") {
    const namePattern = /^[a-zA-Z]+$/;
    let lname = document.getElementsByName("lname");

    for (i = 0; i < lname.length; i++) {
      if (lname[i].value.length >= 0 && namePattern.test(lname[i].value)) {
        lname[i].classList.remove("is-invalid");
        lname[i].classList.add("is-valid");
      } else {
        lname[i].classList.remove("is-valid");
        lname[i].classList.add("is-invalid");
        status = false;
      }
    }
  }

  if (abc.name === "mobile" || abc.id === "myForm") {
    const mobilePattern = /^[6-9]\d{9}$/;

    let mobile = document.getElementsByName("mobile");

    for (i = 0; i < mobile.length; i++) {
      if (mobile[i].value.length >= 0 && mobilePattern.test(mobile[i].value)) {
        mobile[i].classList.remove("is-invalid");
        mobile[i].classList.add("is-valid");
      } else {
        mobile[i].classList.remove("is-valid");
        mobile[i].classList.add("is-invalid");
        status = false;
      }
    }
  }

  if (abc.name === "gender" || abc.id === "myForm") {
    let gender = document.getElementsByName("gender");

    for (i = 0; i < gender.length; i++) {
      if (gender[i].value === "Male" || gender[i].value === "Female") {
        gender[i].classList.remove("is-invalid");
        gender[i].classList.add("is-valid");
      } else {
        gender[i].classList.remove("is-valid");
        gender[i].classList.add("is-invalid");
        status = false;
      }
    }
  }

  if (abc.name === "date" || abc.id === "myForm") {
    let date = document.getElementsByName("date");

    for (i = 0; i < date.length; i++) {
      if (date[i].value) {
        date[i].classList.remove("is-invalid");
        date[i].classList.add("is-valid");
      } else {
        date[i].classList.remove("is-valid");
        date[i].classList.add("is-invalid");
        status = false;
      }
    }
  }

  if (abc.id === "flexCheckDefault" || abc.id === "myForm") {
    let tc = document.getElementById("flexCheckDefault");

    if (tc.checked) {
      tc.classList.remove("is-invalid");
      tc.classList.add("is-valid");
    } else {
      tc.classList.remove("is-valid");
      tc.classList.add("is-invalid");
      status = false;
    }
  }

  if (status == true) {
    return true;
  } else {
    return false;
  }
}
