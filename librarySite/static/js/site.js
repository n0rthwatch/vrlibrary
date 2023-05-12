// Слайдер

if (document.querySelectorAll(".splide").length) {
  let splide = new Splide(".splide", {
    type: "loop",
    drag: "free",
    interval: 4000,
    autoplay: true,
    pauseOnHover: true,
    speed: 700,
    pagination: false,
  });

  let bar = document.querySelector(".my-slider-progress-bar");

  splide.on("mounted move", function () {
    let end = splide.Components.Controller.getEnd() + 1;
    let rate = Math.min((splide.index + 1) / end, 1);
    bar.style.width = String(100 * rate) + "%";
  });

  splide.mount();
}

// Дропдауны

const dropdownBlocks = document.querySelectorAll(".dropdown-block");

if (dropdownBlocks.length) {
  dropdownBlocks.forEach((block) => {
    let btn = block.querySelector(".dropdown-btn");
    let menu = block.querySelector(".dropdown-menu");
    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
      btn.querySelector("svg").classList.toggle("rotate-180");
    });
  });
}

// Фильтр жанров

const genresList = document.querySelector(".genres-list");
const genresShowBtn = document.querySelector(".genres-show-btn");

if (genresShowBtn) {
  genresShowBtn.addEventListener("click", () => {
    let isGenresHidden = genresList.classList.contains("hidden");
    if (isGenresHidden) {
      genresList.classList.remove("hidden");
      genresShowBtn.textContent = "Скрыть фильтр жанров";
    } else {
      genresList.classList.add("hidden");
      genresShowBtn.textContent = "Показать фильтр жанров";
    }
  });
}

// скрытие сообщений

const messages = document.querySelectorAll(".site-message");

messages.forEach((msg) => {
  msg.addEventListener("click", () => {
    console.log(msg);
    msg.classList.add("fade-hide");
    setTimeout(() => {
      msg.remove();
    }, 500);
  });
});
