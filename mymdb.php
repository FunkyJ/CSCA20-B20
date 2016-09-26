<!DOCTYPE html>
<html>
    <?php include 'top.html'; ?>
            <div id="main">
                <h1 class="title"> The One Degree of Kevin Bacon</h1>
                <h2 class="subtitle"> Type in an actor's name to see if s/he ever appeared in a movie with Kevin Bacon!</h2>
                <img src="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/a3/img/kevin_bacon.jpg" alt="Kevin Bacon"/><br/>
                <form id="f1">
                    <div class="input">
                        <fieldset>
                            <legend> Search Movies</legend>
                                <input type="text" id ="fname" name="firstname" placeholder="First Name"/>
                                <input type="text" id ="lname" name="lastname" placeholder="Last Name"/>
                                <input type="submit" value="Filter"/>
                                <select id="actor_id" onchange="pagepush(event)" name="actor_id">
    <?php include 'bottom.html';?>
</html>