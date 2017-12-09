 $(function () {
    $(".date").attr('readonly','readonly');
    var picker = $(".date").datetimepicker({
        minView: "month",   //选择到日期为止，不会显示分钟
        format: "yyyy-mm-dd",
        locale: moment.locale('zh-CN'),
        language: 'zh-CN'
        //minDate: '2016-7-1'
    });
    //动态设置最小值
    picker.on('dp.change', function (e) {
        alert(e.date);
        picker.data('DateTimePicker').minDate(e.date);
    });
});