$(function() {
    $('#bt_show').click(function(){
       ajaxForView("industry");

    });

    // 用户获取绘图结果的ajax请求
    function ajaxForView(type){
        $.ajax({
            url:"/views/view_overall_bar",
            type:'post',
            data:{
                  type:type
                },
            dataType:"html",
            success: function(data,status){
              $('#view').html(data);
            }
        });
    }
})