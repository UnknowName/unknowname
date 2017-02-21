//修改当鼠标经过a标签时改变颜色
var oA = $('a');
var old_color = oA.css('color');
oA.mouseenter(function() {
    $(this).css('color','red').css('text-decoration','none');
});
oA.mouseleave(function() {
    $(this).css('color',old_color);
});
