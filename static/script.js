document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("fraudForm").addEventListener("submit", function (event) {
        event.preventDefault();
        
        let formData = new FormData(this);
        
        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data.prediction || "Error: " + data.error;
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("result").innerText = "An error occurred.";
        });
    });
});
