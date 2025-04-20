<?php

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nombre_restaurante = $_REQUEST['restaurante'];
    $nombre_gerente = $_REQUEST['gerente'];
    $correo = $_REQUEST['correo'];
    $password = $_REQUEST['contrasena'];

    echo "Bienvenido de vuelta: $nombre_gerente";
} else {
    echo "El método no está permitido";
}

?>