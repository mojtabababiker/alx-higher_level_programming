$('div#add_item').on('click', function () {
  const myList = $('ul.my_list');
  const newItem = document.createElement('li');
  newItem.innerText = 'Item';
  myList.append(newItem);
});
