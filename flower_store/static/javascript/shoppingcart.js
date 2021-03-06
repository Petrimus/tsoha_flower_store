document.querySelectorAll('.plus_minus').forEach((item) => {
  item.addEventListener('click', (event) => {
    if (item.name === 'minus') {
      var input = item.parentElement.nextElementSibling;
      input.nextElementSibling.nextElementSibling.firstElementChild.disabled = false;
      var value = parseInt(input.value);
      value--;
      if (value < 1) value = 1;
      // console.log('child: ', input.nextElementSibling.nextElementSibling.firstChild)
      if (value === 1) item.disabled = true;
      input.value = value;
      document.getElementById(input.name).value = value;
    }

    if (item.name === 'plus') {
      var input =
        item.parentElement.previousElementSibling.previousElementSibling;     
      input.previousElementSibling.firstElementChild.disabled = false;
      var value = parseInt(input.value);
      var maxValue = input.max
      value++;
      if (value > maxValue) value = maxValue;      
      if (value === maxValue) item.disabled = true;
      input.value = value;
      document.getElementById(input.name).value = value;
    }
  });
});

function increaseValue() {
  document.getElementById('minus').disabled = false;
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  console.log(typeof value);
  value++;
  if (value == 15) document.getElementById('plus').disabled = true;
  document.getElementById('number').value = value;
}

function decreaseValue() {  
  document.getElementById('plus').disabled = false;
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 0 : value;
  value < 1 ? (value = 1) : '';
  value--;
  if (value == 1) document.getElementById('minus').disabled = true;
  document.getElementById('number').value = value;
}
