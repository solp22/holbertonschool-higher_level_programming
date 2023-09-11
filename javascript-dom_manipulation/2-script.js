const header_div = document.querySelector("#red_header")

header_div.addEventListener("click", updateclass)

function updateclass() {
    const headr = document.querySelector("header")
    headr.classList.add("red")
}
