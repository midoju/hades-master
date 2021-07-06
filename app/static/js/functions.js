function mensaje_error(obj){
    var html = '';
    if(typeof (obj) === 'object'){
        html = '<ul style="text-aling;">';
        $.each(obj, function (key, value){
            html += '<li>' + key + ': ' + value + '</li>';
            console.log(key);
            console.log(value);
        });
        html += '</ul>';    
    }else{
        html = '<p>'+obj+'</p>'; 
    }
    
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error'
    });
}