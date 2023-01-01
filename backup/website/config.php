<?php
    define('USER', 'db_admin');
    define('PASSWORD', 'Admin@HIRA123#');
    define('HOST', 'localhost');
    define('DATABASE', 'hira_db');
    try {
        $connection = new PDO("mysql:host=".HOST.";dbname=".DATABASE, USER, PASSWORD);
    } catch (PDOException $e) {
        exit("Error: " . $e->getMessage());
    }
?>
