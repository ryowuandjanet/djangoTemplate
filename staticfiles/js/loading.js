document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const spinner = document.getElementById('loading-spinner');

    form.addEventListener('submit', function () {
        spinner.classList.remove('hidden');
    });
});
