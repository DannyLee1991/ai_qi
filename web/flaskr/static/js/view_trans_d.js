$(function() {

    $('#searchbtn').click(function(){

        var words = $('#searchWords').val();

        // 生成which查询语句
        var selection=get_select_which();

        var start = $('#ip_date_start').val();
        var end = $('#ip_date_end').val();

        if(!validSarchWord(words)) {
            alert("请输入要查询的股票名或代码");
        } else if(selection.length == 0) {
            alert("至少需要选取一个特征");
        } else if (!validTime(start,end)) {
            alert("开始时间必须小于结束时间");
        } else {
            ajaxForView(words,selection,start,end);
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
    function ajaxForView(searchWord,selection,start,end){
        $.ajax({
            url:"/views/view_trans_d",
            type:'post',
            data:{
                  queryWord:searchWord,
                  which:selection,
                  start:start,
                  end:end
                },
            dataType:"html",
            success: function(data,status){
              $('#view').html(data);
            }
        });
    }

    function validTime(start,end) {
        return start < end;
    }

    function validSarchWord(words) {
        return words.length > 0;
    }

})
