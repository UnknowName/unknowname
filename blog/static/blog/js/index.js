//修改当鼠标经过a标签时改变颜色
var oA = $('a');
var old_color = oA.css('color');
oA.mouseenter(function() {
    $(this).css('color','red').css('text-decoration','none');
});
oA.mouseleave(function() {
    $(this).css('color',old_color);
});
//修改首页菜单与内容边框不对齐
var oMenu = $('#menu ul');
var oMain = $('#main-right');
if(oUl.width() > oMain.width()) {
    oUl.css('padding','0px 205px');
};
