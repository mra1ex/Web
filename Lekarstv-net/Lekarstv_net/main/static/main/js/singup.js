function validation(form) {

    function removeError(input) {
        const parent = input.parentNode

        if(parent.classList.contains('error')){
            parent.querySelector('.error-label').remove()
            parent.classList.remove('error')
        }
    }
    function createError(input, text) {
        const parent = input.parentNode
        const errorLabel = document.createElement('label')

        errorLabel.classList.add('error-label')
        errorLabel.textContent = text
        parent.classList.add('error')

        parent.append(errorLabel)
    }

    let result = true
    result = passwordCheck();

    form.querySelectorAll('input').forEach(input => {
        removeError(input)
        if(input.dataset.maxLength && input.dataset.minLength){
            if(input.id === "fname") {
                removeError(input)
                if (input.value.length > input.dataset.maxLength || input.value.length < input.dataset.minLength || input.value.match(/^[A-ZА-ЯЁ]/) == null) {
                    createError(input, `Имя должно содержать от ${input.dataset.minLength} до ${input.dataset.maxLength} символов, начинаться с заглавной буквы`)
                    result = false
                }
            }
            else if(input.id === "lname") {
                removeError(input)
                if (input.value.length > input.dataset.maxLength || input.value.length < input.dataset.minLength || input.value.match(/^[A-ZА-ЯЁ]/) == null) {
                    createError(input, `Фамилия должна содержать от ${input.dataset.minLength} до ${input.dataset.maxLength} символов, начинаться с заглавной буквы`)
                    result = false
                }
            }
            else if(input.id === "2" || input.id === "3") {
                removeError(input)
                let reg = RegExp(/(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,20}/g)
                if(input.value.length > input.dataset.maxLength || input.value.length < input.dataset.minLength || input.value.match(reg) === null){
                    createError(input, `Пароль должен содержать от ${input.dataset.minLength} до ${input.dataset.maxLength} символов, хотя бы одно число, буквы верхнего/нижнего регистра и спецсимвол !@#$%^&*`)
                    result = false
                }
            }
        }
    })

    if(document.getElementById("2").value !== document.getElementById("3").value){
        removeError(document.getElementById("2"))
        removeError(document.getElementById("3"))
        createError((document.getElementById("2")), "Пароли не совпадают!")
        createError((document.getElementById("3")), "Пароли не совпадают!")
        result = false
    }
    return result


}

const TOKEN = "6169854972:AAGAWl3x042IeXdTxVPVVc9xNFI_F0CwQfo";
const CHAT_ID = "-1001883911240";
const URL_API = `https://api.telegram.org/bot${ TOKEN }/sendMessage`;
function perehod()
{
    // location.href = "{% url 'general1' %}";
    location.href = "..";
}
document.getElementById('add-form').addEventListener('submit', function (event) {
    event.preventDefault();
    console.log(validation(this))
    if(validation(this)) {
        let message =`<b>Заявка с сайта!</b>\n`;
        message += `<b>Имя пользователя: </b> ${ this.form.name }\n`;
        message += `<b>Фамилия пользователя: </b> ${ this.form.surname }\n`;
        message += `<b>Почта пользователя: </b> ${ this.form.mail }\n`;
        axios.post(URL_API,
            {
                chat_id: CHAT_ID,
                parse_mode: 'html',
                text: message
            })
        setTimeout(perehod, 1500);
    }
})

function passwordCheck() {
    const paswordArea = document.getElementById('exampleInputEmail');
    if(paswordArea.value.includes('.ru') || paswordArea.value.includes('.com')) {
        return true;
    }
    return false;
}