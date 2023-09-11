const update_button = document.querySelector("#update_header")

update_button.addEventListener("click", changeHeader)

function changeHeader() {
    const headr = document.querySelector("header")
    headr.innerHTML = "New Header!!!"
}
