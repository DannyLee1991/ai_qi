$(function() {

    $('#addOne').click(function(){
        var words = $('#searchWords').val();
        html = genLabelHtml(words);
        $('#stock_labels').append(html);

        $('#searchWords').val("");
    });

    function genLabelHtml(name) {
        html = " <span class='label label-info label-stock' onclick='this.remove()'>" + name + "</span> ";
        return html;
    };

    $('#searchbtn').click(function(){

//        var words = $('#searchWords').val();

        var words = getSearchedWords();
        // 生成which查询语句
        var selection=getSelectWhich();

        var start = $('#ip_date_start').val();
        var end = $('#ip_date_end').val();

        if(!validSarchWord(words)) {
            alert("请输入至少一个要查询的股票名或代码");
        } else if(selection.length == 0) {
            alert("至少需要选取一个特征");
        } else if (!validTime(start,end)) {
            alert("开始时间必须小于结束时间");
        } else {
            ajaxForView(words,selection,start,end);
        }

    });

    // 获取当前需要查询的字符串数组
    function getSearchedWords(){
        var words = "";
        $('.label-stock').each(function(){
            var value = $(this).text();
            words += value + ',';
        });
        return words;
    }

    // 获取多选框选择的结果
    function getSelectWhich(){
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
    function ajaxForView(words,selection,start,end){
        $.ajax({
            url:"/views/view_trans_d",
            type:'post',
            data:{
                  queryWords:words,
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
