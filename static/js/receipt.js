function getdata(data) {
  let total = document.getElementsByName["total"].value;
  let fname = document.getElementsByName["fname"].value;
  let lname = document.getElementsByName["lname"].value;
  let mobileno = document.getElementsByName["mobile"].value;
  let date = document.getElementsByName["date"].value;
  let gender = document.getElementsByName["gender"].value;
  let info = document.getElementById("p-info-container");
  let hinput = document.getElementsByName("h-input").value;

  for (let i = 0; i < total; i++) {
    info.innerHTML = `<div class="info d-flex justify-content-between flex-wrap">
                        <div class="p-info-inner d-flex w-50">
                            <div class="info w-50 text-bold"> Customer Name</div>
                            <div class="info w-50"> fname[i] + " " + lname[i]</div>
                        </div>

                        <div class="p-info-inner d-flex w-50 ">
                            <div class="info w-50 text-bold"> Mobile No</div>
                            <div class="info w-50"> mobileno[i]</div>
                        </div>
                    </div>

                    <div class="info d-flex justify-content-between flex-wrap">
                        <div class="p-info-inner d-flex w-50">
                            <div class="info w-50 text-bold"> Date Of Birth</div>
                            <div class="info w-50"> date[i]</div>
                        </div>

                        <div class="p-info-inner d-flex w-50">
                            <div class="info w-50 text-bold"> Gender</div>
                            <div class="info w-50"> gender[i]</div>
                        </div>
                    </div>`;
  }

  document.getElementById("price").value = hinput * total;
}




async function generatePDF() {
    window.print()
    // const { jsPDF } = window.jspdf;

    // // Capture the specific section
    // const invoiceElement = document.getElementById("slip");
    // const canvas = await html2canvas(invoiceElement, { scale: 2 });
    // const imgData = canvas.toDataURL("image/png");

    // // Create A4-sized PDF (210mm x 297mm)
    // const pdf = new jsPDF("p", "mm", "a4");
    // const imgWidth = 210; // A4 width in mm
    // const imgHeight = (canvas.height * imgWidth) / canvas.width; // Keep aspect ratio

    // pdf.addImage(imgData, "PNG", 0, 0, imgWidth, imgHeight);
    // pdf.save("slip.pdf"); // Save the PDF
}