<?php

$con = mysqli_connect('localhost', 'root', '','db_connect');


$txtEmail = $_POST['txtEmail'];
$txtPass = $_POST['txtPass'];


$sql = "INSERT INTO `tbl_contact` (`email`, `password`) VALUES ('$txtEmail', '$txtPass')";

$rs = mysqli_query($con, $sql);

if($rs)
{
	header('Location: test.html');
}

?>