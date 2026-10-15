// Change the site name in ONE place:
const SITE_NAME = "AI Tool Tracker";
document.querySelectorAll("[data-sitename]").forEach(e=>e.textContent=SITE_NAME);
document.title = document.title.replace("AI Tool Tracker", SITE_NAME);
