$(document).ready(function(){
    $("#f1").submit(getActor);
            
});
    function getActor(event)  {
        event.preventDefault();
        var $select = $('#actor_id');
        var $fname = $('#fname').val();
        var $lname= $('#lname').val();
        $.getJSON('actors.php?firstname=' + $fname + '&lastname=' + $lname,
            { 'myparam': 'testval' },
            function(data)  {
                $.each(data, function(key,val) {
                var $option = $("<option/>").attr("value",val.id).attr("firstname",val.first_name).attr("lastname",val.last_name).text(val.first_name + " " + val.last_name);
                $select.append($option);         
                });
        });
    }
    function pagepush(event)  {
        var $hl = $(event.target).find("option:selected").text();
        var $id = $('#actor_id').val();
        var $combo = $id + " " + $hl;
        var $code = $combo.split(" ");
        window.location.href = 'https://mathlab.utsc.utoronto.ca/courses/cscb20w16/kwongka4/search.php?firstname=' + $code[1] + '&lastname=' + $code[2] + '&id=' + $code[0];
    }