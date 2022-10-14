let saveFile = () => {


       const name = document.getElementById('name');
       const password = document.getElementById('password');
        
        
        let data = 
            '\r Username: ' + name.value + ' \r\n ' + 
            'Password: ' +password.value + ' \r\n ' + 
            
        
        // Convert the text to BLOB.
        const textToBLOB = new Blob([data], { type: 'text/plain' });
        const sFileName = 'formData.txt';	   // The file to save the data.

        let newLink = document.createElement("a");
        newLink.download = sFileName;

        if (window.webkitURL != null) {
            newLink.href = window.webkitURL.createObjectURL(textToBLOB);
        }
        else {
            newLink.href = window.URL.createObjectURL(textToBLOB);
            newLink.style.display = "none";
            document.body.appendChild(newLink);
        }

        newLink.click(); 
    }