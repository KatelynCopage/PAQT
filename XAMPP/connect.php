
<?php

//Connects localhost to phpMyAdmin and the database called db_connect
$con = mysqli_connect('localhost', 'root', '','db_connect');


$txtEmail = $_POST['txtEmail'];
$txtPass = $_POST['txtPass'];

//mitigations 
$txtEmail = mysqli_real_escape_string($_POST['txtEmail']);
$txtPass = mysqli_real_escape_string($_POST['txtPass']);

//Insert SQL string into database 
$sql = "SELECT * FROM tbl_contact WHERE email = '".$txtEmail . "' AND password = '".$txtPass."';";

//Goes to homepage if returns true otherwise returns an error
$rs = mysqli_query($con, $sql);
if(mysqli_num_rows($rs) == 1) {
	header('Location: test.html');
} else{
	print_r("Login Unsuccessful");
}



?>
