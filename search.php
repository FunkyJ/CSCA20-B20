<?php
	// create a function to display the result of a query as a table
	// use the foreach loop with each item as index => array[index]
	function make_table($query) {
		echo "<table><tr>";
		$row = mysqli_fetch_assoc($query);
		foreach ($row as $attr => $value) {
			echo "<th>$attr</th>";
		}
		echo "</tr>";
		while ($row = mysqli_fetch_assoc($query)) { 
			echo "<tr>";
			foreach($row as $value) {
				echo "<td>$value</td>";
			}
			echo "</tr>";
		}
		echo "</table>";
	}
?>
<!DOCTYPE html>
<html>
    <?php include 'top.html';
    $first = $_REQUEST["firstname"];
    $last = $_REQUEST["lastname"];
    $name = $first." ".$last;
    $id = $_REQUEST["id"];
    ?>
        
        <div id="main">
            <h1 class="title"> Results for <?= $name ?></h1>
            <h2 class="subtitle"> Films with <?= $name ?></h2>
            <?php
            include 'config.php';
            // Create connection
            $conn = mysqli_connect($servername, $username, $password, $dbname);
            // Check connection
            if (!$conn) {
                echo "Failure";
                die("Connection failed: " . mysqli_connect_error());
            }
            $sql = "SELECT DISTINCT name,year FROM roles JOIN actors JOIN movies WHERE actor_id = actors.id AND movies.id = movie_id AND actors.id =".$id;
            $result = mysqli_query($conn, $sql);
            ?>
            <table id="results"><tr><th>#</th><th>Title</th><th>Year</th></tr>
            <?php
            // display results as a table
            while ($row = mysqli_fetch_assoc($result)) { 
                $number += 1; ?>
                <tr><td> <?= $number ?></td><td><?= $row["name"] ?></td><td><?= $row["year"] ?></td></tr>
            <?php
            }
            ?>
            </table>
                <form id="f1">
                    <div class="input">
                        <fieldset>
                            <legend> Search Movies</legend>
                                <input type="text" id ="fname" name="firstname" placeholder="First Name"/>
                                <input type="text" id ="lname" name="lastname" placeholder="Last Name"/>
                                <input type="submit" value="Go"/>
                                <select id="actor_id" onchange="pagepush(event)" name="actor_id">
    <?php include 'bottom.html';?>
</html>