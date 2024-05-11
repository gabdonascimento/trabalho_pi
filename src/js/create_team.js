// Function to add a new row to the form
function addRow() {
    var studentsContainer = document.getElementById("students_container");
    var newRow = document.createElement("div");
    newRow.classList.add("row");
    newRow.innerHTML = `
        <input type="text" id="text" placeholder="Nome do Aluno (a)">
        <input type="text" class="input-value" placeholder="RA do Aluno (a)">
        <button type="button" class="deleteBtn" onclick="removeRow(this)">Remover Aluno</button>
    `;
    studentsContainer.appendChild(newRow);
}

// Function to remove a row from the form
function removeRow(button) {
    var row = button.parentNode;
    row.parentNode.removeChild(row);
}

// Event listener for adding a row
document.getElementById("addRowBtn").addEventListener("click", addRow);
