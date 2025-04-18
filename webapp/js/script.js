document.addEventListener('DOMContentLoaded', async () => {
    const tapButton = document.getElementById('tapButton');
    const coinCountElement = document.getElementById('coinCount');
    const energyElement = document.getElementById('energy');
    const userId = Math.floor(Math.random() * 1000000);

    const response = await fetch(`https://dubai-city-bot-4411f7915851.herokuapp.com/user/${userId}`);
    const data = await response.json();
    coinCountElement.textContent = data.coins;
    energyElement.textContent = data.energy;

    tapButton.addEventListener('click', async () => {
        const response = await fetch(`https://dubai-city-bot-4411f7915851.herokuapp.com/tap/${userId}`, { method: 'POST' });
        const data = await response.json();
        if (data.success) {
            coinCountElement.textContent = data.coins;
            energyElement.textContent = data.energy;
        } else {
            alert('Energiya tugadi! Keyinroq sinab ko‘ring.');
        }
    });
});