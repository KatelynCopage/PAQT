<?php

//Connects localhost to phpMyAdmin and the database called db_connect
$con = mysqli_connect('localhost', 'root', '','db_connect');

// get email and password 

$txtEmail = $_POST['txtEmail'];
$txtPass = $_POST['txtPass'];

//insert into sql database 

$sql = "INSERT INTO `tbl_contact` (`email`, `password`) VALUES ('$txtEmail', '$txtPass')";

$rs = mysqli_query($con, $sql);


// redirecting to test.html once connected to php
if($rs)
{
	header('Location: test.html');
}

?>
