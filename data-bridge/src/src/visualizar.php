<!DOCTYPE html>
<html>
<head>
    <title>Resultados</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>

<h1>Resultados de Búsqueda</h1>

<table border="1" style="margin:auto; background:white; color:black;">
<tr>
    <th>ID</th>
    <th>Modelo</th>
    <th>Color</th>
    <th>Material</th>
    <th>Chasis</th>
    <th>Año</th>
</tr>

<?php

$archivo_filtrado = "filtrado.txt";

if(file_exists($archivo_filtrado)){
    $lineas = file($archivo_filtrado);

    foreach($lineas as $linea){
        $datos = explode("|", trim($linea));
        echo "<tr>";
        foreach($datos as $dato){
            echo "<td>$dato</td>";
        }
        echo "</tr>";
    }
}

?>

</table>

</body>
</html>