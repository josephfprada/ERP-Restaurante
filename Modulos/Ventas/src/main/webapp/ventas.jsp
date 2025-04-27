<%@ page import="java.util.ArrayList" %>
<%@ page import="inventarios.Producto" %>
<!DOCTYPE html>
<html>
<head>
    <title>Ventas</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
<h2>Gestion de Ventas</h2>

<form method="post" action="ventas" class="mb-4">
    <input name="nombre" placeholder="Nombre del producto a vender" class="form-control mb-2" required/>
    <input name="cantidad" type="number" placeholder="Cantidad a vender" class="form-control mb-2" required/>
    <button class="btn btn-success">Vender Producto</button>
</form>

<% String mensaje = (String) request.getAttribute("mensaje");
    if (mensaje != null) { %>
<div class="alert alert-info">
    <%= mensaje %>
</div>
<% } %>

<h3>Inventario Actualizado</h3>
<ul class="list-group">
    <%
        ArrayList<Producto> productos = (ArrayList<Producto>) request.getAttribute("productos");
        if (productos != null) {
            for (Producto p : productos) {
    %>
    <li class="list-group-item">
        <strong><%= p.getNombre() %></strong> -
        <%= p.getCantidad() %> unidades disponibles
    </li>
    <%
            }
        }
    %>
</ul>

<a href="index.jsp" class="btn btn-secondary mt-4">Volver al Inicio</a>
</body>
</html>
