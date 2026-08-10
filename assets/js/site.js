"use strict";

for (const node of document.querySelectorAll("[data-current-year]")) {
  node.textContent = new Date().getFullYear();
}

for (const node of document.querySelectorAll("[data-current-date-time]")) {
  const now = new Date();
  const fecha = now.toLocaleDateString("es-CO", { year: "numeric", month: "2-digit", day: "2-digit" });
  const hora = now.toLocaleTimeString("es-CO", { hour: "2-digit", minute: "2-digit" });
  node.textContent = `${fecha} ${hora}`;
}

const menu = document.querySelector(".info-menu");
if (menu) {
  document.addEventListener("click", (event) => {
    if (menu.open && !menu.contains(event.target)) menu.open = false;
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") menu.open = false;
  });
}
