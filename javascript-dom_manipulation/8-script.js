document.addEventListener("DOMContentLoaded", function () {
    const hello = document.getElementById("hello");

    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
        .then(function (response) {
            if (!response.ok) {
                throw new Error("Error network response");
            }
            return response.json();
        })
        .then(function (data) {
            hello.textContent = data.hello
        })
        .catch(function (error) {
            console.error("There was a problem with the fetch operation:", error);
        });
});