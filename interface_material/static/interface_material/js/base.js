$(".gui-folder a").on("click", function () {
    var id = $(this).attr('id');
    $('.gui-controls-interno').hide(200);
    $('#ul-'+id).toggle(200);
});
