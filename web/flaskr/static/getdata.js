function sendFSPost(w,ps) {

    var params = new Array();
    if (ps !== null) {
        for(var i=0;i<ps.length;i++) {
            params.push({
                for_what:ps[i].for_what,
                value:$('#'+ps[i].id).val()
            });
        }

    }
  $.post("/fs_data",
  {
   what:w,
   params:params
  });
}

function sendFSPost(w) {
    $.get("/fs_data",
    {
    what:w
    });
}