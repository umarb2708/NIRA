<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.container {
  position: relative;
  width: 100%;
  overflow: hidden;
  padding-top: 62.5%; /* 16:9 Aspect Ratio */
}

.responsive-iframe {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  height: 100%;
  border: none;
}
</style>
</head>
<body>
<div class="container">
  <?php 
	global $ip;
	$ip=system("hostname -I");
  ?>
  <?php echo "<iframe class=\"responsive-iframe\" src=\"http://".$ip.":1880/ui\" id=\"target\"></iframe>";?>
</div>
    <script>
        var div = document.getElementById("target");
        div.onload = function() {
            div.style.height =
              div.contentWindow.document.body.scrollHeight + 'px';
        }
    </script>
</body>
</html>

