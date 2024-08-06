// static/js/modal.js
document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript 已加載');

    document.querySelectorAll('[data-modal-target]').forEach(button => {
        button.addEventListener('click', () => {
            console.log('顯示模態窗口', button.getAttribute('data-modal-target'));
            const modalId = button.getAttribute('data-modal-target');
            document.getElementById(modalId).classList.remove('hidden');
        });
    });

    document.querySelectorAll('[data-modal-close]').forEach(button => {
        button.addEventListener('click', () => {
            console.log('隱藏模態窗口');
            button.closest('.fixed').classList.add('hidden');
        });
    });

    document.querySelectorAll('.fixed').forEach(modal => {
        modal.addEventListener('click', (event) => {
            if (event.target === modal) {
                console.log('點擊模態窗口外部');
                modal.classList.add('hidden');
            }
        });
    });
});
