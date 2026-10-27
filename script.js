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
  // Live Google reviews (homepage). Fetched from Google only when the section is near the
  // screen, kept for the visit in sessionStorage, never stored on our side.
  var rv = document.getElementById('g-reviews');
  if (rv && window.fetch) {
    var load = function () {
      var ck = 'g-reviews-v1', cached = null;
      try { cached = JSON.parse(sessionStorage.getItem(ck)); } catch (e) {}
      var show = function (d) {
        var list = ((d && d.reviews) || []).filter(function (r) { return r.rating >= 4 && r.text && r.text.text; }).slice(0, 3);
        list.forEach(function (r) {
          var card = document.createElement('figure'); card.className = 'rv-card';
          var st = document.createElement('div'); st.className = 'rv-stars';
          st.setAttribute('aria-label', r.rating + ' out of 5 stars'); st.textContent = '★★★★★'.slice(0, r.rating);
          var t = r.text.text;
          if (t.length > 260) { t = t.slice(0, 250); t = t.slice(0, t.lastIndexOf(' ')) + '…'; }
          var q = document.createElement('blockquote'); q.textContent = t;
          var cap = document.createElement('figcaption'), a = r.authorAttribution || {};
          var who = document.createElement(a.uri ? 'a' : 'span');
          who.textContent = a.displayName || 'Google user';
          if (a.uri) { who.href = a.uri; who.target = '_blank'; who.rel = 'noopener'; }
          var when = document.createElement('span'); when.textContent = r.relativePublishTimeDescription ? ' · ' + r.relativePublishTimeDescription : '';
          cap.appendChild(who); cap.appendChild(when);
          card.appendChild(st); card.appendChild(q); card.appendChild(cap); rv.appendChild(card);
        });
        if (list.length) rv.className += ' loaded';
      };
      if (cached) { show(cached); return; }
      fetch('https://places.googleapis.com/v1/places/' + rv.getAttribute('data-place') + '?fields=reviews&languageCode=en&key=' + rv.getAttribute('data-key'))
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (d) { if (!d) return; try { sessionStorage.setItem(ck, JSON.stringify({ reviews: d.reviews || [] })); } catch (e) {} show(d); })
        .catch(function () {});
    };
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); load(); } }, { rootMargin: '600px' });
      io.observe(rv);
    } else { load(); }
  }
})();
