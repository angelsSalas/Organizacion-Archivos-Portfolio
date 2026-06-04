<?php

$archivo_maestro = "maestro.txt";
$archivo_filtrado = "filtrado.txt";

$palabra = $_POST['palabra_clave'];

$resultados = [];

if(file_exists($archivo_maestro)){

    $lineas = file($archivo_maestro);

    foreach($lineas as $linea){

        // stripos busca sin distinguir mayúsculas/minúsculas
        if(stripos($linea, $palabra) !== false){
            $resultados[] = $linea;
        }
    }

    file_put_contents($archivo_filtrado, $resultados);
}

header("Location: visualizar.php");
exit();

?>