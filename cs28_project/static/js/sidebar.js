$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#collapseSidebar').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#bodyBlock').toggleClass('active');
        $('.bars').toggleClass('active');
        $('#table').bootstrapTable('resetView')
    });

    $('#overlay').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#overlay').toggleClass('active');
        $('.bars').toggleClass('active');
    });
});