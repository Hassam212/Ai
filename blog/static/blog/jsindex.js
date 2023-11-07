
document.addEventListener('DOMContentLoaded', function() {
  const body = document.body;
let toggleTheme = document.querySelector('.theme-toggler');

if (localStorage.getItem('dark-theme') === 'enabled') {
    body.classList.add('dark-theme');
}

toggleTheme.addEventListener('click', () => {
    body.classList.toggle('dark-theme');

    if (body.classList.contains('dark-theme')) {
        localStorage.setItem('dark-theme', 'enabled');

        toggleTheme.querySelector('span:nth-child(1)').classList.add('active-theme');
        toggleTheme.querySelector('span:nth-child(2)').classList.remove('active-theme');

    } else {
        localStorage.removeItem('dark-theme');
        toggleTheme.querySelector('span:nth-child(1)').classList.remove('active-theme');
        toggleTheme.querySelector('span:nth-child(2)').classList.add('active-theme');
    }
});



var scrollTop = document.getElementById("scroll-top");

window.addEventListener("scroll", function () {
    if (window.scrollY > 100) {
        scrollTop.classList.add("active");
    } else {
        scrollTop.classList.remove("active");
    }
});




scrollTop.addEventListener("click", function (event) {
    event.preventDefault();
    var scrollOptions = {
        top: 0,
        behavior: "smooth"
    };
    window.scrollTo(scrollOptions);
});
});