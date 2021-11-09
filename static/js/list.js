async function showValues() {    
        const response = await fetch('http://192.168.0.27:8000/list_api/', {            
                method: 'GET', // *GET, POST, PUT, DELETE, etc.          
        });
        const myJson = await response.json(); //extract JSON from the http response        
        console.log(myJson);        
};

async function saveValues() {    
        var url = 'http://192.168.0.27:8000/list_api/';        
        let myForm = document.getElementById('form_custom_settings');        
        var formData = new FormData(myForm);        
        var configurations = {
                "label_one": formData.get("label_one"),
                "label_two": formData.get("label_two")
        }   
        formData.append("configurations", JSON.stringify(configurations));
        var fileField = document.querySelector("input[type='file']");
        formData["photo"] = fileField.files[0];        
        await fetch(url, {
                method: 'POST', // or 'PUT'
                body: formData, // data can be `string` or {object}!
                headers:{                 
                  'X-CSRFToken': csrftoken
                }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(response => console.log('Success:', response));       
}


$( "#btn_save_form" ).click( saveValues );