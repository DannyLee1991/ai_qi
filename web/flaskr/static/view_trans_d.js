$(function() {
    $('#searchbtn').click(function(){

        var words = $('#searchWords').val();

        // 生成which查询语句
        var cb_which_array =$("input[id^='cb_which_']");
        var select_which='';
        for(var i=0; i<cb_which_array.length; i++){
            var idstr = cb_which_array[i].id;
            var start = "cb_which_".length;
            var end = idstr.length;
            var which = cb_which_array[i].id.substring(start,end);

            if(cb_which_array[i].checked) select_which += which+','; //如果选中，将value添加到变量s中
        }

        if(select_which.length == 0) {
            alert("至少需要选取一个特征");
        } else {
            $.ajax({
                url:"/views/view_trans_d",
                type:'post',
                data:{
                      queryWord:words,
                      which:select_which
                    },
                dataType:"html",
                success: function(data,status){
                  $('#view').html(data);
                }
            });
        }

    });
})