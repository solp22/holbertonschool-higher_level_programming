fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => response.json())
    .then(data => {
        const movies = data.results
        movies.forEach(movie => {
            const list = document.querySelector("#list_movies")
            const node = document.createElement("li")
            const textnode = document.createTextNode(movie.title)
            node.appendChild(textnode)
            list.appendChild(node);
        })
    })
