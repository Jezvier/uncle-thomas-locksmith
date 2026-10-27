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
  // WhatsApp quick-quote form: turn the answers into a ready-made message
  var qs = document.querySelectorAll('form[data-qq]');
  for (var i = 0; i < qs.length; i++) qs[i].addEventListener('submit', function (e) {
    e.preventDefault();
    var f = e.target, v = function (n) { var el = f.querySelector('[name="' + n + '"]:checked') || f.elements[n]; return el ? (el.value || '').trim() : ''; };
    var t = 'Hi Uncle Thomas, I need a locksmith.\nService: ' + v('what') + '\nLocation: ' + (v('where') || '(will send)') + '\nWhen: ' + v('when') + '\n(Sent from your website)';
    var url = f.getAttribute('action') + '?text=' + encodeURIComponent(t);
    if (typeof window.gtag === 'function') window.gtag('event', 'quote_form_submit', { service: v('what'), urgency: v('when'), page_path: location.pathname, transport_type: 'beacon' });
    var w = window.open(url, '_blank', 'noopener');
    if (!w) location.href = url;
  });
})();
