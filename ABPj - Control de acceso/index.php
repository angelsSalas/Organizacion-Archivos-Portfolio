<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Control de Acceso - Maquiladora</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<h2 style="text-align:center;">Bitácora de Entradas - Maquiladora</h2>
    <table>
        <tr><th>Fecha/Hora</th><th>Evento</th></tr>
        <?php
        $archivo = fopen("auditoria.txt", "r");
        while(($linea = fgets($archivo)) !== false) {
            $clase = (strpos($linea, "ALERTA") !== false) ? "alerta" : "";
            echo "<tr class='$clase'><td>".substr($linea,0,19)."</td><td>".substr($linea,22)."</td></tr>";
        }
        fclose($archivo);
        ?>
    </table>
</body>
</html>
