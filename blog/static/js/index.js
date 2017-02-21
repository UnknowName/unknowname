var oMenu = $('a');
var old_color = oMenu.css('color');

oMenu.mouseenter(function() {
    $(this).css('color','red').css('text-decoration','none');
});

oMenu.mouseleave(function() {
    $(this).css('color',old_color);
});
