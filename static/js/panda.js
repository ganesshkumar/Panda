search = function() {
    $.getJSON($root_url + 'search', {
        search: document.getElementById('search').value,
    }, function(data) {
        if (data.result == "ITEM_NOT_FOUND")
            document.getElementById('not-found').style.display = 'Block';
        else {
            document.getElementById('not-found').style.display = 'None';
            window.analysis = data.result;
        }
    });
}

