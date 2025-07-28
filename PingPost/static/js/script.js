document.querySelectorAll(".search-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    btn.classList.remove("jiggle"); // reset
    void btn.offsetWidth; // force reflow
    btn.classList.add("jiggle");
  });
});
