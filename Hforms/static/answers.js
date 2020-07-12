function create_fields(questions,data_type){
	for ( let i = 1 ; i < questions.length; i++){
		let ul = document.querySelector('#answers')
		let list = document.createElement('li');
		let ques = document.createElement('p');
		if(data_type[i] == "TEXT"){
			var answer = document.createElement('textarea');
			answer.placeholder = "Only characters allowed";
			answer.className = 'form-control form-control-lg answer_text_input'; /* CSS */
		}
		else{
			var answer = document.createElement('input');
			answer.type = 'number';
			answer.placeholder = "Only numbers allowed";
			answer.className = 'form-control form-control-lg'; /* CSS */
		}
		ques.id = 'question'+i.toString();
		ques.innerHTML = questions[i];

		ques.className = ''; /* CSS */

		answer.name = 'answer'+i.toString();
		answer.id = 'answer'+i.toString();
		
		list.className = 'answer_li'; /* CSS */
    
		answer.name = 'answer'+i.toString();
		answer.id = 'answer'+i.toString();

		ul.appendChild(list);
		list.appendChild(ques);
		list.appendChild(answer);
	}
}
function check_fields(is_req){
	document.querySelector('#submit').onclick = (eve) => {	
		for (let i = 1; i < is_req.length; i++) {
			if(is_req[i] == 1){
				if(!document.getElementById('answer'+i.toString()).value){
					alert('Answer to question '+i.toString()+' is compulsory');
					eve.preventDefault();
				}
			}
		}
	}
}