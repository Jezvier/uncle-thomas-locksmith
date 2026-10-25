// Uncle Thomas Locksmith — tiny JS (mobile menu + footer year)
(function () {
  var b = document.querySelector('.menu-btn'), m = document.getElementById('mobile-menu');
  if (b && m) b.addEventListener('click', function () {
    var open = m.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
    b.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
