const addItemBtn = document.querySelector("#add_item");

addItemBtn.addEventListener("click", function () {
    const ul = document.querySelector(".my_list");
    const li = document.createElement("li");
    li.textContent = "Item";
    ul.appendChild(li);
});