$(function() {
    $('#bt_show').click(function(){

        var type = getCrtType();
        var limit = getLimitCount();
        if(type.length == 0) {
            alert('请选择一种展示类型');
            return;
        }
       ajaxForView(type,limit);

    });

    // 用户获取绘图结果的ajax请求
    function ajaxForView(type,limit){
        $.ajax({
            url:"/views/view_overall_bar",
            type:'post',
            data:{
                  type:type,
                  limit:limit
                },
            dataType:"html",
            success: function(data,status){
              $('#view').html(data);
            }
        });
    }

    // 获取当前选中的类型
    function getCrtType(){
        var prefix = 'or_'
        var options = $('input[id^='+prefix+']');
        var selectId = '';
        options.each(function(){
            if(this.checked){
                var start = prefix.length;
                var end = this.id.length;
                selectId = this.id.substring(start,end);
            }
        });
        return selectId;
    }

    // 获取数量限制
    function getLimitCount() {
        return $('#ip_count').val()
    }
})