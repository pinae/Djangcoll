function sendCalibrationDataRequest(event) {
    let mailRegex = new RegExp("^(?<username>[a-zA-Z0-9_.]+)@((?<subdomain>\\w*)\\.)*(?<domain>[a-zA-Z]\\w*)\\.(?<topleveldomain>[a-zA-Z]\\w+)$");
    if (mailRegex.test(event.target.value)) {
        document.getElementById("mailhint").style.visibility = "visible";
        document.getElementById("mailhint").style.backgroundColor = "green"
        document.getElementById("mailhint").innerText = "This is a valid email address.";
        let xhr = new XMLHttpRequest();
        xhr.addEventListener('load', (event) => {
            console.log(event.target.responseText);
        });
        xhr.addEventListener('error', (event) => {
            console.log(event);
        });
        xhr.open("POST", "calibration/init", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader("X-CSRFToken", document.getElementById('UploadForm').childNodes[1]['value']);
        xhr.send(JSON.stringify({
            email: ""
        }));
    } else {
        document.getElementById("mailhint").style.visibility = "visible";
        document.getElementById("mailhint").style.backgroundColor = "red"
        document.getElementById("mailhint").innerText = "Not a email address: " + event.target.value;
        console.log("Not a email address: " + event.target.value);
    }
}

document.getElementById("id_email").addEventListener('keyup', sendCalibrationDataRequest);