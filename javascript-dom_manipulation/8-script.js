fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then(response => response.json())
    .then(data => {
        const element = document.querySelector("#hello");
        element.textContent = data.hello;
        })
        .catch(error => console.error("Error:", error));