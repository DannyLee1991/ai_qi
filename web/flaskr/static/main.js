$(function(){
    toggle_nav()
});


function toggle_nav() {
    var pathname = window.location.pathname

    $('#nav-setting').removeClass("active")
    $('#nav-index').removeClass("active")
    $('#nav-getdata').removeClass("active")

    if (pathname == '/') {
        $('#nav-index').addClass("active")
    } else if(pathname == '/setting') {
        $('#nav-setting').addClass("active")
    } else if(pathname == '/getdata') {
        $('#nav-getdata').addClass("active")
    }

}