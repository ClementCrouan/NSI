const modalInput = document.querySelector('.modal__input')
const modalValidate = document.querySelector('.modal__validate')
const modal = document.querySelector('.modal')

const userInput = document.querySelector('.container__user_input')
const addOne = document.querySelector('.conainer__add-one')
const addTen = document.querySelector('.conainer__add-ten')

let value = 0

modalValidate.addEventListener('click', () => {
	const userValue = parseInt(modalInput.value)

	if (isNaN(userValue)) {
		alert('Veuiller rentrer un chiffre')
		return
	}
	
	value = userValue
	modal.classList.add('hidden')
	
	userInput.textContent = `Valeur: $(value)`
}) 