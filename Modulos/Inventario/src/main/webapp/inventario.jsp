<%@ page import="java.util.ArrayList" %>
<%@ page import="inventarios.Producto" %>
<!DOCTYPE html>
<html>
<head>
    <title>Inventario</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
<h2>Gestion de Inventario</h2>

<form method="post" action="inventario" class="mb-4">
    <input name="nombre" placeholder="Nombre del producto" class="form-control mb-2" required/>
    <input name="cantidad" type="number" placeholder="Cantidad" class="form-control mb-2" required/>
    <input name="precio" type="number" step="0.01" placeholder="Precio" class="form-control mb-2" required/>
    <button class="btn btn-primary">Agregar Producto</button>
</form>

<h3>Listado de Productos</h3>
<ul class="list-group">
    <%
        ArrayList<Producto> productos = (ArrayList<Producto>) request.getAttribute("productos");
        if (productos != null) {
            for (Producto p : productos) {
    %>
    <li class="list-group-item">
        <strong><%= p.getNombre() %></strong> -
        <%= p.getCantidad() %> unidades -
        $<%= p.getPrecio() %> cada uno
    </li>
    <%
            }
        }
    %>
</ul>

<a href="index.jsp" class="btn btn-secondary mt-4">Volver al Inicio</a>
</body>
</html>
