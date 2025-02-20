<?php
// กำหนดให้รองรับ CORS
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");

date_default_timezone_set('Asia/Bangkok');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

//================================
define('DEBUG', true);
error_reporting(E_ALL);
ini_set('display_errors', DEBUG?1:0);

//================================
$apiUrl = '';
switch($_SERVER['SERVER_NAME']){
    case 'localhost':
        $apiUrl = 'http://127.0.0.1:8000/';
        // $apiUrl = 'http://localhost/asiaMart/test.php';
        break;
    case 'app.asiagroup1999.co.th':
        $apiUrl = 'http://192.168.3.8:8001/';
        break;
}

//================================
// รับข้อมูลที่ส่งมา (ถ้ามี)
$rawInput = file_get_contents("php://input");
$params = !empty($rawInput) ? json_decode($rawInput, true) : $_REQUEST;

//================================
$method = $_SERVER['REQUEST_METHOD'];
$endpoint = isset($_REQUEST['endpoint']) ? $_REQUEST['endpoint'] : '';
$url = $apiUrl . $endpoint;

unset($params['endpoint']);
$queryParam = ($method == 'POST' || $method == 'PUT')?'':'?'.http_build_query($params);

// if($fpt = fopen(__DIR__.'/data.txt','a+')){
//     fwrite($fpt, "========== '.$method.' = middleware.php ========="."\n");
//     fwrite($fpt, json_encode($params)."\n");
//     fwrite($fpt, 'url = '.$url. "\n");
//     fwrite($fpt, "\n");
//     fclose($fpt);
// }else{
//     // echo 'can\'n open file';
// }
// exit;

//================================
// ตั้งค่า cURL เพื่อส่งข้อมูลไปยัง FastAPI
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url.$queryParam);
// curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
curl_setopt($ch, CURLOPT_HTTP_VERSION, CURL_HTTP_VERSION_1_1);
// curl_setopt($ch, CURLOPT_VERBOSE, true);
// curl_setopt($ch, CURLOPT_ENCODING, '');

if ($method == 'POST' || $method == 'PUT') {
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept: application/json','Content-Type: application/json']);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($params));
// }else{
    // curl_setopt($ch, CURLOPT_HTTPHEADER, ['Accept: application/json','Content-Type: application/x-www-form-urlencoded']);
    // curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($params));
}

// ส่งคำขอไปยัง FastAPI
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// ส่งผลลัพธ์กลับไปยัง Vue.js
http_response_code($httpCode);
echo $response;
//================================

?>