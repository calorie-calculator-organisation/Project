document.addEventListener('DOMContentLoaded', () => {
    const addFoodForm = document.querySelector('form');

    if (addFoodForm) {
        addFoodForm.addEventListener('submit', (event) => {
            const foodName = document.querySelector('input[name="name"]').value;
            const calories = document.querySelector('input[name="calories"]').value;

            // Перевірка, чи заповнені всі поля
            if (!foodName || !calories) {
                alert('Будь ласка, заповніть всі поля!');
                event.preventDefault(); // Зупиняє відправку форми
            }
        });
    }
});