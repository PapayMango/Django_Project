function create_progress_bar(){
    var progress = `
        <div class="progress my-3" style="height:30px;">
            <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width:0%"></div>
        </div>`
    document.getElementById('progressbar').innerHTML = progress
    console.log('c');
    startDL();
}

function startDL(){
    $.ajaxSetup({
        headers:{
            "X-CSRFToken":document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    var form = $('form');
    // console.log(form);
    // console.log(form.prop('action'));
    $.ajax({
        // xhr:function(){
        //     var xhr = new XMLHttpRequest();
        //     xhr.upload.addEventListener('progress',function(e){
        //         print("abc")
        //         print(e)
        //     });
        //     return xhr;
        // },
        url:form.prop('action'),
        method:form.prop('method'),
        // dataType:'text',
        dataType:'json',
        // cache:false,
        // processData:false,
        // contentType:false,
        // data:form.serialize(),
        // success:function(res){
        //     // alert(res.data)
        //     console.log('success');
        //     console.log(res);
        // }
    })
    .done(function(data){
        console.log('success')
        console.log('data : ' + data['p'])
        console.log('data : ' + data['t'])
        console.log(typeof data)
        p = data['p']
        t = data['t']
        if (t != 0){
            r = p/t
            console.log(r)
            // console.log($('.progress-bar'))
            $('.progress-bar').css('width', r*100 + '%')
        }
        if(!data['f']){
            setTimeout(startDL,2000)
        }
    })
}
var time = 0;
(function ($) {
    $('#submit').on('click',(event) => {
        // console.log(event)
        // event.preventDefault();
        create_progress_bar();
        // console.log('a');
        // startDL();
        // console.log('sa')
        setInterval(() => {
            $('#timer').text(time + 's');
            print(time)
            time = time +1; 
        }, 1000);
    })
})(jQuery);

console.log('s');
