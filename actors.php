<?php
$first_name = $_REQUEST["firstname"];
$last_name = $_REQUEST["lastname"];
include 'config.php';
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    echo "Failure";
    die("Connection failed: " . mysqli_connect_error());
}
$sql = "SELECT id, first_name, last_name FROM actors WHERE first_name LIKE '%".$first_name."%' AND last_name LIKE '%".$last_name."%'";
$result = mysqli_query($conn, $sql);        
$runs = array();
while ($row = mysqli_fetch_assoc($result)) {
    $runs[] = $row;
}    
mysqli_close($conn);
$json = json_encode($runs);
echo $json
?>
