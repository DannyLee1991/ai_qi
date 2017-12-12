$(function() {
    // 选择id以bt_table_开头的button
    var prefix = "bt_view_";
    $('button[id^='+prefix+']').click(function(){
        var id = this.id.substring(prefix.length,this.id.length);

        $.ajax({
            url:"/visualization/" + id,
            type:'get',
            dataType:"html",
            success: function(data,status){
              $('#view_container').html(data);
            }
        });
    });
});