$(".gui-folder a").on("click", function () {
    var id = $(this).attr('id');
    $('.gui-controls-interno').hide(200);
    $('#ul-'+id).toggle(200);
});

// Evento para mostrar o menu caso o usuário passe o mouse sobre o item do menu
$("div").on('mouseover', '.mdl-layout__drawer-button', function(){
    $( "div[id='menu-drawer']" ).addClass('is-visible');
    $( "div[class='mdl-layout__obfuscator']" ).addClass('is-visible');
});
// Evento para ocultar o menu quando ele sair do elemento menu-drawer
$("div").on('mouseleave', '#menu-drawer', function() {
  $( "div[id='menu-drawer']" ).removeClass('is-visible');
  $( "div[class*='mdl-layout__obfuscator']" ).removeClass('is-visible');
});
