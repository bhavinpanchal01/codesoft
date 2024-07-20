function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculate() {
    let expression = document.getElementById('display').value;
    let result = eval(expression); // Using eval for simplicity; in production, consider using a safer method to evaluate expressions.
    document.getElementById('display').value = result;
}
