$("div#add_item").on ("click", function() {
    const my_list = $("ul.my_list");
    const new_item = document.createElement("li");
    
    new_item.innerText = "Item"
    my_list.append(new_item);
});
