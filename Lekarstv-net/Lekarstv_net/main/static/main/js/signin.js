function validation(form){

    function removeError(input){
        const parent = input.parentNode;

        if(parent.classList.contains('error')){
            parent.querySelector('.error-label').remove()
            parent.classList.remove('error')
        }
    }
    function createError(input, text){
        const parent = input.parentNode;
        const errorLabel = document.createElement('label')

        errorLabel.classList.add('error-label')

        errorLabel.textContent = text
        parent.classList.add('error')

        parent.append(errorLabel)
    }


    let result = true;

    const allInputs = form.querySelectorAll('input');

    for (const input of allInputs) {

        removeError(input)

        result =  emailCheck();
        if (input.dataset.required == 'true') {
            if (input.value == "") {
                console.log('error');
                createError(input, 'field is empty')
                result = false;
            }
        }

        if (input.dataset.minLength) {
            removeError(input)

            if (input.value.length < input.dataset.minLength) {
                console.log('error');
                createError(input, `number of symbols < ${input.dataset.minLength}`)
                result = false;
            }
        }
    }

    return result;
}






document.getElementById('add-form').addEventListener('submit',function (event)
{
    event.preventDefault()


    if(validation(this) == true)
    {
        location.href = '../../../templates/main/general.html'
    }
})

function emailCheck() {
    const paswordArea = document.getElementById('exampleInputEmail1');
    if(paswordArea.value.includes('.ru') || paswordArea.value.includes('.com')) {
        return true;
    }
    alert('error');
    return false;
}