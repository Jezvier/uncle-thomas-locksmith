// Uncle Thomas Locksmith — tiny JS: mobile menu, footer year, call/WhatsApp click tracking
(function () {
  var b = document.querySelector('.menu-btn'), m = document.getElementById('mobile-menu');
  if (b && m) b.addEventListener('click', function () {
    var open = m.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
  // GA4 events: call_click / whatsapp_click, labelled by page and button position
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || typeof window.gtag !== 'function') return;
    var h = a.getAttribute('href'), ev = null;
    if (h.indexOf('tel:') === 0) ev = 'call_click';
    else if (h.indexOf('wa.me') !== -1) ev = 'whatsapp_click';
    if (!ev) return;
    window.gtag('event', ev, {
      page_label: document.title,
      page_path: location.pathname,
      link_position: a.getAttribute('data-pos') || 'inline',
      transport_type: 'beacon'
    });
  });
})();
