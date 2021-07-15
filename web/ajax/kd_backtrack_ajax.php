<?php
#$requests = $_REQUEST['requests'];
#---------------------MySQL登入資訊
$retrieve = $date = $id = "";
$host = "220.135.176.190";
$user = "k20";
$passwd = "jona789521456";
$database = "stonk";
$connect = new mysqli($host, $user, $passwd, $database);

$connect->query("SET NAMES 'utf8'");

$selectSql = "SELECT * FROM semi_kd_backtrack ORDER BY `date` DESC LIMIT 10";

$totaldata = $connect->query($selectSql);

if ($totaldata->num_rows > 0) {
    while ($row = $totaldata->fetch_assoc()) {
        $db_date = $row['date'];
        $db_original_prediction = $row['original_prediction'];
        $db_3day_result = $row['3day_result'];
        $db_5day_result = $row['5day_result'];
        $db_10day_result = $row['10day_result'];
        $db_20day_result = $row['20day_result'];
        $db_30day_result = $row['30day_result'];

        echo $db_date;
        echo $db_original_prediction;
        echo $db_3day_result;
        echo $db_5day_result;
        echo $db_10day_result;
        echo $db_20day_result;
        echo $db_30day_result;
    }
}