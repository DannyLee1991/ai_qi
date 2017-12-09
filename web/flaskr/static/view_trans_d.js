$(function() {

    $('#searchbtn').click(function(){

        var words = $('#searchWords').val();

        // 生成which查询语句
        var selection=get_select_which();

        if(selection.length == 0) {
            alert("至少需要选取一个特征");
        } else {
            ajaxForView(words,selection);
        }

    });

    // 获取多选框选择的结果
    function get_select_which(){
        var select_which='';
        var cb_which_array =$("input[id^='cb_which_']");
        for(var i=0; i<cb_which_array.length; i++){
            var idstr = cb_which_array[i].id;
            var start = "cb_which_".length;
            var end = idstr.length;
            var which = cb_which_array[i].id.substring(start,end);

            if(cb_which_array[i].checked) select_which += which+','; //如果选中，将value添加到变量s中
        }
        return select_which;
    }

    // 用户获取绘图结果的ajax请求
    function ajaxForView(searchWord,selection){
        $.ajax({
            url:"/views/view_trans_d",
            type:'post',
            data:{
                  queryWord:searchWord,
                  which:selection
                },
            dataType:"html",
            success: function(data,status){
              $('#view').html(data);
            }
        });
    }

})
