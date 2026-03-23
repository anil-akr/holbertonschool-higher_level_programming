const updateBtn = document.querySelector("#update_header");

updateBtn.addEventListener("click", function () {
    const header = document.querySelector("header");
    header.textContent = "New Header!!!";
});