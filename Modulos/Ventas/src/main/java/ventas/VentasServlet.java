package ventas;

import inventarios.Producto;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.ArrayList;

public class VentasServlet extends HttpServlet {
    private static final ArrayList<Producto> productos = new ArrayList<>();


    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        String nombre = req.getParameter("nombre");
        int cantidadVenta = Integer.parseInt(req.getParameter("cantidad"));

        String mensaje = "Producto no encontrado.";
        for (Producto p : productos) {
            if (p.getNombre().equalsIgnoreCase(nombre)) {
                if (p.getCantidad() >= cantidadVenta) {
                    p.setCantidad(p.getCantidad() - cantidadVenta);
                    mensaje = "Venta exitosa: " + cantidadVenta + " unidades de " + nombre;
                } else {
                    mensaje = "Stock insuficiente para " + nombre;
                }
                break;
            }
        }
        req.setAttribute("mensaje", mensaje);
        req.setAttribute("productos", productos);
        req.getRequestDispatcher("/ventas.jsp").forward(req, resp);
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        req.setAttribute("productos", productos);
        req.getRequestDispatcher("/ventas.jsp").forward(req, resp);
    }
}
