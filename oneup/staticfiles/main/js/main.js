function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');

    // Додаємо/знімаємо класи активності
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
}