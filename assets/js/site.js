"use strict";

for (const node of document.querySelectorAll("[data-current-year]")) {
  node.textContent = new Date().getFullYear();
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
