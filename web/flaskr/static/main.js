$(function(){ 
    toggle_nav()
});


function toggle_nav() {
    var pathname = window.location.pathname

    $('#nav_setting').removeClass("active")
    $('#nav_index').removeClass("active")
    $('#nav_getdata').removeClass("active")

    if (pathname == '/') {
        $('#nav_index').addClass("active")
    } else if(pathname == '/setting') {
        $('#nav_setting').addClass("active")
    } else if(pathname == '/getdata') {
        $('#nav_getdata').addClass("active")
    }

}