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
        xhr.open("POST", "/calibration/init", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader("X-CSRFToken", document.getElementById('UploadForm').childNodes[1]['value']);
        xhr.send(JSON.stringify({
            email: event.target.value
        }));
    } else {
        document.getElementById("mailhint").style.visibility = "visible";
        document.getElementById("mailhint").style.backgroundColor = "red"
        document.getElementById("mailhint").innerText = "Not a email address: " + event.target.value;
        console.log("Not a email address: " + event.target.value);
    }
}

function sendProcessingRequest() {
    let xhr = new XMLHttpRequest();
    xhr.addEventListener('load', (event) => {
        let results = JSON.parse(event.target.responseText);
        document.getElementById("wait_block").style.display = "none";
        document.getElementById("results").style.display = "block";
        document.getElementById("amylum").innerText = results["amylum"].toFixed(2) + " %";
        document.getElementById("lactose").innerText = results["lactose"].toFixed(2) + " %";
        document.getElementById("insect_protein").innerText = results["insect_protein"].toFixed(2) + " %";
    });
    xhr.addEventListener('error', (event) => {
        console.log(event);
    });
    xhr.open("POST", "/processing/ai/results", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader("X-CSRFToken", document.getElementById('processing').childNodes[5]['value']);
    xhr.send(JSON.stringify({
        id: document.getElementById("processingID").innerText
    }));
}

let idEmail = document.getElementById("id_email");
if (idEmail) idEmail.addEventListener('keyup', sendCalibrationDataRequest);
let idDiv = document.getElementById("processingID");
if (idDiv) setTimeout(sendProcessingRequest, 5000);