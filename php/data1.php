<?php
    $username = "felfel"; 
    $password = "I_suvikifu584";   
    $host = "b54roabzas.database.windows.net";
    $database="felfel0A3A8dqTdG";
    
    $server = mysql_connect($host, $username, $password);
    $connection = mysql_select_db($database, $server);
/*
    $myquery = "
    SELECT  `locationname` FROM  `locations`
    ";
    $query = mysql_query($myquery);
    
    if ( ! $query ) {
        echo mysql_error();
        die;
    }
    
    $data = array();
    
    for ($x = 0; $x < mysql_num_rows($query); $x++) {
        $data[] = mysql_fetch_assoc($query);
    }
    
    echo json_encode($data);     
     
    mysql_close($server); */
?>