function validate() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var messagee = document.getElementById("error");

    messagee.style.backgroundColor = '#c';
    messagee.style.textAlign = 'center';
    messagee.style.padding = '10px';
    messagee.style.color = '#fff'
    messagee.style.fontFamily = 'cursive';
    messagee.style.borderRadius = '4px';
    messagee.style.fontWeight = 'bold';
    messagee.style.transition = 'all 0.4s ease-in-out'
    messagee.style.marginBottom = '10px';


    var text

    if (email.indexOf("@") == -1) {

        text = 'please Enter Valid Email'
        messagee.innerHTML = text;
        return false;
    }
    if (name.length < 5) {
        text = 'Full Name must be greater than 5'
        messagee.innerHTML = text;
        return false;

    }
    if (isNaN(phone)) {

        text = 'please Enter Valid phone'
        messagee.innerHTML = text;
        return false;


    } else if (email == none && phone == none) {

        text = 'please Enter Valid email and phone'
        messagee.innerHTML = text;
        return false;
    } else {
        alert('success')
        return true;
    }



}