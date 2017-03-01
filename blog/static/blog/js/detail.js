//修改当鼠标经过a标签时改变颜色
var oA = $('a');
var old_color = oA.css('color');
oA.mouseenter(function() {
    $(this).css('color','red').css('text-decoration','none');
});
oA.mouseleave(function() {
    $(this).css('color',old_color);
});
//当main-right width太小时，设置成同父DIV的比例
var oMain = $('div.wrapper');
new_width = oMain.width() * 0.7;
new_height = oMain.height() * 0.8;
var oRight = $('div #main-right');
if (oRight.width() < new_width) {
    oRight.width(new_width);
};
if (oRight.height() < new_height) {
    oRight.height(new_height);
};

