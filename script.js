function mountInput(placeholder, type = "text", classes = "input-value") {
    var newInput = document.createElement("input");
    newInput.classList.add(classes)
    newInput.setAttribute("type", type)  
    newInput.setAttribute("placeholder", placeholder)   
    return newInput;
}

function addRow() {
    var container = document.querySelector(".students_inputs_container");
    var newRow = document.createElement("div");
    newRow.classList.add("row");
    newRow.appendChild(mountInput('Nome do Aluno(a)'))
    newRow.appendChild(mountInput('RA do Aluno(a)'))
    container.appendChild(newRow);
}

// Event listener for the button
document.getElementById("addRowBtn").addEventListener("click", addRow);
