<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: *');
header('Access-Control-Allow-Headers: *');

date_default_timezone_set('Asia/Bangkok');

//================================
define('DEBUG', false);
error_reporting(E_ALL);
ini_set('display_errors', DEBUG?1:0);

//================================
$apiUrl = '';
switch($_SERVER['SERVER_NAME']){
    case 'localhost':
        $apiUrl = 'http://127.0.0.1:8000';
        break;
    case 'app.asiagroup1999.co.th':
        $apiUrl = 'http://192.168.3.8:8001';
        break;
}

//================================
$params = $_REQUEST;
$endpoint = $_REQUEST['endpoint'];
$method = $_SERVER['REQUEST_METHOD'];

// อ่าน raw input กรณีที่เป็น PUT, PATCH, DELETE ซึ่งไม่มี $_POST
$rawInput = file_get_contents("php://input");
$params = !empty($rawInput) ? json_decode($rawInput, true) : $_REQUEST;

//================================
$curl = curl_init();
curl_setopt_array($curl, array(
    CURLOPT_URL => rtrim($apiUrl, '/') . '/' . ltrim($endpoint, '/'), // ป้องกัน double slash
    CURLOPT_HTTPHEADER => array(
        'Accept: application/json',
        'Content-Type: application/json',
    ),
    CURLOPT_CUSTOMREQUEST => $method, // ใช้ method ที่ได้รับมา
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_SSL_VERIFYPEER => false,
    CURLOPT_ENCODING => '',
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_VERBOSE => true
));

// ส่ง body เฉพาะ method ที่รองรับ
if (!in_array($method, ['GET', 'HEAD'])) {
    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($params));
}

$response = curl_exec($curl);
$err = curl_error($curl);
curl_close($curl);

if ($err) {
    echo json_encode(['success' => false, 'error' => $err]);
} else {
    echo $response;
}

//================================

?>