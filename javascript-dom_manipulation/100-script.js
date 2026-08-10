document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  const list = document.querySelector('#my_list') ||
    document.querySelector('.my_list');

  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });

  removeItem.addEventListener('click', function () {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  clearList.addEventListener('click', function () {
    list.innerHTML = '';
  });
});
