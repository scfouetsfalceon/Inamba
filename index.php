<?php
$config = parse_ini_file("config.ini", true);
$ddbb = $config['BD'];

$link = mysql_connect($ddbb['servidor'], $ddbb['usuario'], $ddbb['contrasena']);
mysql_select_db($ddbb['bd']);

$ini_array = parse_ini_file("boleta.cfg", true);
$i = 1;
$j = 1;

$consejo = array();
$corte = array();

$sql = "SELECT `candidato`, COUNT(id) as cantidad FROM `consejo` GROUP BY `candidato`";
$rs = mysql_query($sql);

while ($resultados = mysql_fetch_object($rs)){
    $consejo[$resultados->candidato] = $resultados->cantidad;
}

$sql = "SELECT `candidato`, COUNT(id) as cantidad FROM `corte` GROUP BY `candidato`";
$rs = mysql_query($sql);

while ($resultados = mysql_fetch_object($rs)){
    $corte[$resultados->candidato] = $resultados->cantidad;
}

$sql = "SELECT COUNT(id) as cantidad FROM `votos`";
$rs = mysql_fetch_object(mysql_query($sql));

$votos = $rs->cantidad;
print "Para una cantidad de votos de $votos<br/>\n";
foreach ($ini_array as $key => $value) {
    if ( $key != 'VOTOS' ) {

        if ( substr($key, 0, -1) == "CONSEJO" ) {
            if($i==1)print "Consejo Nacional<br/>\n";
            $voto = ( array_key_exists($i, $consejo) )? $consejo[$i]:0;
            ($value['nombre'] != '')?print "$i - ".$value['nombre']." Votos: $voto<br/>\n":'';
            $i++;
        } else {
            if($j==1)print "Corte de Honor<br/>\n";
            $voto = ( array_key_exists($j, $corte) )? $corte[$j]:0;
            ($value['nombre'] != '')?print "$j - ".$value['nombre']." Votos: $voto<br/>\n":'';
            $j++;
        }
    }
}
mysql_close($link);
print 'Descargar boleta para auditoria <a href="auditoria/votacion.txt">aquí</a>'
?>

