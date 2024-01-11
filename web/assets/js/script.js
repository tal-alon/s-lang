document.addEventListener("DOMContentLoaded", function() {

    let editor = ace.edit("codeInput"); // Get the editor
    editor.setTheme("ace/theme/monokai"); // Set theme to monokai
    editor.session.setMode("ace/mode/javascript"); // Set syntax highlighting to javascript
    editor.session.setOption("useWorker", false); // Disable syntax checking


    document.getElementById("executeButton").addEventListener("click", function() {

        let variables = document.getElementById("variablesInput").value.split(',').map(Number);
        let code = editor.getValue();

        fetch('http://20.217.131.28:8000/run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: code, inputs: variables }),
        })
        .then(response => response.json())
        .then(data => {
            if(data.error === null) {
                document.getElementById("resultOutput").textContent = data.output;
            }
            else {
                document.getElementById("resultOutput").textContent = data.error;
            }
        })
        .catch((error) => {
            document.getElementById("resultOutput").textContent = error;
        });

    });

});
