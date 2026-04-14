// app.js – Shared interactivity for all pages

// Highlight the active nav link based on current page
(function () {
  const page = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-tab').forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
})();

// Mobile hamburger menu toggle
const hamburger = document.getElementById('hamburger');
const sidebar   = document.getElementById('sidebar');

if (hamburger && sidebar) {
  hamburger.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    hamburger.textContent = sidebar.classList.contains('open') ? '✕' : '☰';
  });

  // Close sidebar when a nav link is clicked (mobile)
  sidebar.querySelectorAll('.nav-item').forEach(link => {
    link.addEventListener('click', () => {
      sidebar.classList.remove('open');
      hamburger.textContent = '☰';
    });
  });
}
