<?php
$currenturl = "http://technikamateur.bplaced.net/raspido";
$latestversion = "1.0";
$name = "raspido.tar.gz"
$userversion = $_GET["userversion"];
if ($latestversion == $userversion)
{
  print "latest-version";
} else {
  print "$currenturl/$latestversion/$name";
}
$requests = file_get_contents('requests.txt');
$requests = intval($requests);
$requests = $requests + 1;
$datei = fopen("requests.txt", "w");
fwrite($datei, $requests);
?>
