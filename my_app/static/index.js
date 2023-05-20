const indexButton = document.querySelector("#indexButton");
const blogButton = document.querySelector("#blogButton");
const aboutButton = document.querySelector("#aboutButton");
const contactButton = document.querySelector("#contactButton");

// Asigna el evento onclick a cada botón
indexButton.onclick = () => navigatePage("{% url 'templates:index' %}");
blogButton.onclick = () => navigatePage("{% url 'templates:blog' %}");
aboutButton.onclick = () => navigatePage("{% url 'about' %}");
contactButton.onclick = () => navigatePage("{% url 'contact' %}");

// Función para navegar a la página correspondiente
function navigatePage(url) {
  window.location.href = url;
}