const header_div = document.querySelector("#red_header")

header_div.addEventListener("click", updatecolor)

function updatecolor() {
    const headr = document.querySelector("header")
    headr.style.color = "#FF0000";
}
