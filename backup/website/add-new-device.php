<!DOCTYPE HTML>  
<html>
<head>
<style>
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
body {
    margin: 50px auto;
    text-align: center;
    width: 800px;
}
h1 {
    font-family: 'Passion One';
    font-size: 2rem;
    text-transform: uppercase;
}
label {
    width: 150px;
    display: inline-block;
    text-align: left;
    font-size: 1.5rem;
    font-family: 'Lato';
}
input {
    border: 2px solid #ccc;
    font-size: 1.5rem;
    font-weight: 100;
    font-family: 'Lato';
    padding: 10px;
}
select {
    border: 2px solid #ccc;
    font-size: 1.5rem;
    font-weight: 100;
    font-family: 'Lato';
    padding: 10px;
}
form {
    margin: 25px auto;
    padding: 20px;
    border: 5px solid #ccc;
    width: 500px;
    background: #eee;
}
div.form-element {
    margin: 20px 0;
}
button {
    padding: 10px;
    font-size: 1.5rem;
    font-family: 'Lato';
    font-weight: 100;
    background: yellowgreen;
    color: white;
    border: none;
}
p.success,
p.error {
    color: white;
    font-family: lato;
    background: yellowgreen;
    display: inline-block;
    padding: 2px 10px;
}
p.error {
    background: orangered;
}
</style>
</head>
<body>
<?php
    session_start();
    include('config.php');
    if (isset($_POST['register'])) {
        $comp = $_POST['component'];
        $room = $_POST['room'];
        $floor = $_POST['floor'];
	$istuya = $_POST['istuya'];
	$tuyaip = $_POST['tuyaip'];
        $query = $connection->prepare("SELECT * FROM home_automation WHERE component=:comp AND room=:room AND floor=:floor");
        $query->bindParam("comp", $comp, PDO::PARAM_STR);
        $query->bindParam("room", $room, PDO::PARAM_STR);
        $query->bindParam("floor", $floor, PDO::PARAM_STR);
        $query->execute();
        if ($query->rowCount() > 0) {
            echo '<p class="error">Device already registered!</p>';
        }
	//echo '<p class="success"> COMP:'.$comp.' ROOM:'.$room.' FLOOR:'.$floor.' ISTUYA:'.$istuya.' TUYAIP:'.$tuyaip.'</p>';
        if ($query->rowCount() == 0) {
            $query = $connection->prepare("INSERT INTO home_automation(room,floor,component,isTuya,TuyaIP) VALUES (:room,:floor,:comp,:istuya,:tuyaip)");
            $query->bindParam("room", $room, PDO::PARAM_STR);
            $query->bindParam("floor", $floor, PDO::PARAM_STR);
            $query->bindParam("comp", $comp, PDO::PARAM_STR);
            $query->bindParam("istuya", $istuya, PDO::PARAM_STR);
            $query->bindParam("tuyaip", $tuyaip, PDO::PARAM_STR);
            $result = $query->execute();
            if ($result) {
                echo '<p class="success">Your registration was successful!</p>';
            } else {
                echo '<p class="error">Something went wrong!</p>';
  	    }
    	}
    }
?>

<form method="post" action="" name="signup-form">
<div class="form-element">
<label>Component</label>
<select name="component" id="comp" required>
 <option value="light">Light</option>
 <option value="fan">Fan</option>
 <option value="night lamp">Night Lamp</option>
</select>
</div>
<div class="form-element">
<label>Room</label>
<select name="room" id="room" required>
 <option value="master bedroom">Master Bedroom</option>
 <option value="second bedroom">Second Bedroom</option>
 <option value="third bedroom">Third Bedroom</option>
<option value="office room">Office Room</option>
<option value="kitchen">kitchen</option>
<option value="hall">Hall</option>
<option value="sitout">Sitout</option>
<option value="staircase">Staircase</option>
</select>
</div>
<div class="form-element">
<label>Floor</label>
<select name="floor" id="floor" required >
 <option value="ground">Ground</option>
 <option value="first">First</option>
 <option value="top">top</option>
</select>
</div>
<div class="form-element">
<label>Tuya Device</label>
<select name="istuya" id="istuya" required >
 <option value="1">Yes</option>
 <option value="0">No</option>
</select>
</div>
<div class="form-element">
<label>Tuya IP</label>
<input type="text" name="tuyaip" pattern="[0-9]+.[0-9]+.[0-9]+.[0-9]+" />
</div>
<button type="submit" name="register" value="register">Register</button>
</form>
</body>
</html>
