$(function() {
    $('#bt_execute').click(function(){
      var sql = $('#txt_sql').val();
      execute_sql(sql,true);
    });

    // 选择id以bt_table_开头的button
    var prefix = "bt_table_";
    $('button[id^='+prefix+']').click(function(){
        var table = this.id.substring(prefix.length,this.id.length);
        var sql = "select * from " + table + " limit 100;";
        execute_sql(sql,false);

        this.addClass('active');
    });
});

function execute_sql(sql_str,save_sql) {

    $.post("/tables/sql",
    {
      sql:sql_str,
      save:save_sql
    },
    function(data,status){
      $('#table_container').html(data);
    });

//  $("#myDiv").html(htmlobj.responseText);
}