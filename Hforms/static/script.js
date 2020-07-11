const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

var isActive = false;

document.body.addEventListener('click', () => {

	var togglerClicked = false;

	toggleButton.addEventListener('click', () => {;
		isActive = !isActive;
		navbarLinks.classList.toggle('active');
		togglerClicked = true;
	});

	if(isActive && !togglerClicked) {
		navbarLinks.classList.toggle('active');
		isActive = !isActive;
	}
	
}, true);