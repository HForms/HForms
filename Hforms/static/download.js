function add_options(options){
	let select = document.querySelector('#options');
	let option = '';
	for(let i = 0; i < options.length; i++){
		option += '<option value = "' + options[i] + '">' + options[i] + '</option>';
		select.innerHTML = option;
	}
}