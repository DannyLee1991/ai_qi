function sendFSPost(w,ps) {
  $.get("/fs_data",
  {
   what:w,
   params:ps
  });
}
