$(document).ready(function(){
    $('.video-thumb').click(function(e){
        var self = $(this);
        e.preventDefault();

        $('#ytplayer').attr('src', self.attr('href'));
    });
});