<!DOCTYPE html>
<html>
    <head>
        <title>My Movie Database (MyMDb)</title>
        <meta charset="utf-8" />

        <!-- Links to provided files.  Do not change these links -->
        <link href="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/a3/img/favicon.png" type="image/png" rel="shortcut icon" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js" type="text/javascript"></script>
        <script src="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/kwongka4/mymdb.js" type="text/javascript"></script>
        
        <!-- Link to your CSS file that you should edit -->
        <link href="mymdb.css" type="text/css" rel="stylesheet" />
    </head>
    <body>
        <div id="frame">
            <header>  <!-- new HTML5 page-section structure element -->
                <a href="index.php"><img src="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/a3/img/mymdb_logo.png" alt="banner logo" /></a>
                <h0 id="webpage">My Movie Database</h0>
            </header>
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
                                    <option value="1">Select an Actor</option>
                                </select><br/>
                        </fieldset>
                        </div>
                        <div id="kevbox">
                            <input type="checkbox" name="kevin">Show only movies with Kevin Bacon     
                        </div>
                </form>
            </div>
            <footer>  <!-- new HTML5 page-section structure element -->
                <a href="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/html_validator.php"><img src="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/a3/img/w3c-html.png" alt="Valid HTML5" /></a> <!--<br />-->
                <a href="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/css_validator.php"><img src="https://mathlab.utsc.utoronto.ca/courses/cscb20w16/bretsche/assignments/a3/img/w3c-css.png" alt="Valid CSS" /></a>
            </footer>
        </div>
    </body>
</html>