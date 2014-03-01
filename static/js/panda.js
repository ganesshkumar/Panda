search = function() {
    $.getJSON($root_url + 'search', {
        search: document.getElementById('search').value,
    }, function(data) {
        alert(data.result)
    });
}