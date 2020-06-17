var i=1;
document.addEventListener('DOMContentLoaded',() => {
    document.querySelector('#add').onclick = () => {
        let ul = document.querySelector('#questions');
        let list = document.createElement('li');
        let question = document.createElement('input');
        let remove = document.createElement('input');
        let checkbx = document.createElement('input');
        let select = document.createElement('select');
        let label = document.createElement('label');

        let options =new Array('Text', 'Number');
        let option = '<option value = "" disabled selected>Select Answer type</option>';
        for(var j = 0; j < options.length ; j++)
            option += '<option value = ' + options[j] + '>' + options[j] + '</option>';

        list.id = 'questions'+i.toString();
        
        question.type = 'text'
        question.name = 'question'+i.toString();
        question.id = 'question'+i.toString();
        question.placeholder = 'Enter the question';

        remove.type = 'button'
        remove.value = 'Remove'
        remove.id = 'remove'+i.toString();
        remove.onclick = function() { removequestion(this.id); };

        checkbx.type = 'checkbox';
        checkbx.name = 'is_req'+i.toString();
        checkbx.id = 'id'+i.toString();
        checkbx.value = 'True';

        label.id = 'label'+i.toString();
        label.htmlFor = 'id'+i.toString();
        label.appendChild(document.createTextNode('Is Required '));

        select.name = 'data_type'+i.toString();
        select.id = 'data_type'+i.toString();
        select.innerHTML = option;

        ul.appendChild(list);
        list.appendChild(question);
        list.appendChild(checkbx);
        list.appendChild(label);
        list.appendChild(select);
        list.appendChild(remove);

        i++;

        return false;
}

    function removequestion(question_id) {
        if(question_id.length === 7){
            var remove = document.getElementById('questions'+question_id[6].toString());
        }
        else if(question_id.length === 8){
            var remove = document.getElementById('questions'+question_id[6].toString()+question_id[7].toString());
        }
        else{
            var remove = document.getElementById('questions'+question_id[6].toString()+question_id[7].toString()+question_id[8].toString());
        }
        remove.remove(remove);
        console.log(i)
        if(parseInt(question_id[6]) < i-1){
            var k=1;
            for(let j=parseInt(question_id[6]+question_id[7]+question_id[8]); j < i-1; j++){
                let renameli = document.getElementById('questions'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k).toString());
                let renamequ = document.getElementById('question'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k).toString());
                let renamechkbx = document.getElementById('id'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k).toString());
                let renamelbl = document.getElementById('label'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k).toString());
                let renamesel = document.getElementById('data_type'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k).toString());
                let renamerem = document.getElementById('remove'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k).toString());

                renameli.id = 'questions'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();
                
                renamequ.id = 'question'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();
                renamequ.name = 'question'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();

                renamechkbx.id = 'id'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();
                renamechkbx.name = 'is_req'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();

                renamelbl.id = 'label'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();
                renamelbl.htmlFor = 'id'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();

                renamesel.id = 'data_type'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();
                renamesel.name = 'data_type'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();

                renamerem.id = 'remove'+(parseInt(question_id[6]+question_id[7]+question_id[8])+k-1).toString();

                k++;
            }
        }
        i = (parseInt(question_id[6]+question_id[7]+question_id[8])+k-1);
        return false;
}
    
    document.querySelector('#submit').onclick = (eve) =>{
        
        if(!document.getElementById('title').value){
            alert('Please give a title to the form');
            eve.preventDefault();
        }

        if(!document.getElementById('question').value){
            alert('Please fill first question before submitting the form');
            eve.preventDefault();
        }
        for(let j = 1; j < i; j++)
        {
            if(!document.getElementById('question'+j.toString()).value){
                alert('Please fill question number ' + (j+1).toString() + ' before submitting the form');
            eve.preventDefault();
            }
        }
        for(let j = 0; j < i; j++)
        {
            if(document.getElementById('data_type'+j.toString()).value === ''){
                alert("Please select answer type for question "+(j+1).toString());
                eve.preventDefault();
            }
        }
    }
});
