$(function(){
    toggle_nav()
});


function toggle_nav() {
    var pathname = window.location.pathname;

    $('#nav-*').removeClass("active");
    var to = pathname.length;
    var id = "";
    if (pathname == '/') {
        id = '#nav-index';
    } else {
        id = '#nav-' + pathname.substring(1,to);
    }
    $(id).addClass("active");

}