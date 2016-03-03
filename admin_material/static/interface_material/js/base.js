$(".gui-folder a").on("click", function () {
    var id = $(this).attr('id');
    $('.gui-controls-interno').hide(200);
    $('#ul-'+id).toggle(200);
});


// Evento para mostrar o menu caso o usuário passe o mouse sobre o item do menu
$( "div[class='mdl-layout__drawer-button']" ).mouseover(function() {
  /* Act on the event */
  console.log('Over');
  $( "div[class='manu-drawer']" ).addClass('is-visible');
});
