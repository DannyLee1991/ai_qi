$(function() {
    var forSearchStock = {
        source: function (query, process) {
            $.get("/query/stockNames",
            {
                word:query
            },
            function(data,status){
                // data 是字符串列表
                var subjects = eval(data);
                return process(subjects);
            });
        },
        afterSelect: function (item) {
            //选择项之后的时间，item是当前选中的项
//            alert(item);
        },
        items: 8, //显示8条
        delay: 100 //延迟时间
    };
    $('#searchWords').typeahead(forSearchStock);
    $(".stock").typeahead(forSearchStock);
})