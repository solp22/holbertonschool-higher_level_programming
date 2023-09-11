const header_div = document.querySelector("#toggle_header")

header_div.addEventListener("click", updateclass)

function updateclass() {
    const headr = document.querySelector("header")
    if (headr.classList == "red"){
        headr.classList.replace("red", "green")
    } else {
        headr.classList.replace("green", "red")
    }
}
