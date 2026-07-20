fetch("http://127.0.0.1:8000/get_recepts")
  .then((response) => response.json())
  .then((data) => {
    const container = document.getElementById("container");

    data.forEach((recept) => {
      container.innerHTML += `
        <div class="recept">
          <h2>${recept.title}</h2>
          <p>${recept.recept}</p>
        </div>
      `;
    });
  });