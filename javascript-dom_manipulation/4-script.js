const add_button = document.querySelector("#add_item")

add_button.addEventListener("click", addElement)

function addElement() {
    const list = document.querySelector("ul.my_list")
    const node = document.createElement("li")
    const textnode = document.createTextNode("Item")
    node.appendChild(textnode)
    list.appendChild(node);
}
