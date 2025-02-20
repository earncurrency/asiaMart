<?php
// กำหนดให้รองรับ CORS
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

$rawInput = file_get_contents("php://input");
$params = !empty($rawInput) ? json_decode($rawInput, true) : $_REQUEST;

if($fpt = fopen(__DIR__.'/data.txt','a+')){
    fwrite($fpt, "========== test.php ========="."\n");
    fwrite($fpt, json_encode($params)."\n");
    fwrite($fpt, "\n");
    fclose($fpt);
}else{
    echo 'can\'n open file';
}
?>