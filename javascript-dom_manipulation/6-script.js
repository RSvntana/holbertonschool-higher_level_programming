const character_element = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(function(response) {
        if (!response.ok){
            throw new Error("Network response was not ok")
        }
        return response.json();
    })
    .then(
        function(data){
            const character_name = data.name;

            character_element.textContent = "Character: " + character_name;
    })
    .catch(function(error){
        console.error('There was a problem with fetch operation:', error)
    })