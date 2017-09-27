$(document).ready(function(){
    $('.show_more').click(function(e){
        var self = $(this);
        e.preventDefault();

        $.get($(this).attr('href'), function(response) {
            self.closest('.article-description').find('.article-text').html(response);
            self.remove();
        });
    });
});