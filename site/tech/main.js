document.addEventListener('mousemove', e => {
    Object.assign(document.documentElement, {
        style: `
        --move-x: ${(e.clientX - window.innerWidth / 2) * -.005}deg;
        --move-y: ${(e.clientY - window.innerWidth / 2) * -.01}deg;
        `
    })
})
const redirectButton = document.getElementById('redirectButton');

        redirectButton.addEventListener('click', () => {
            window.location.href = 'contacts.html';
        });
