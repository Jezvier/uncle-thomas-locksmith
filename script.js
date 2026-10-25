// Uncle Thomas Locksmith — minimal JS (keep it light for speed)

// Auto-update footer year
document.addEventListener('DOMContentLoaded', function () {
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
});
