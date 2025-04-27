package inventarios;

import org.jetbrains.annotations.NotNull;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.util.ArrayList;

public class InventarioServlet extends HttpServlet {
    private static final ArrayList<Producto> productos = new ArrayList<>();

    @Override
    protected void doPost(@NotNull HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String nombre = request.getParameter("nombre");
        int cantidad = Integer.parseInt(request.getParameter("cantidad"));
        double precio = Double.parseDouble(request.getParameter("precio"));

        productos.add(new Producto(nombre, cantidad, precio));

        request.setAttribute("productos", productos);
        request.getRequestDispatcher("/inventario.jsp").forward(request, response);
    }

    @Override
    protected void doGet(@org.jetbrains.annotations.NotNull HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        request.setAttribute("productos", productos);
        request.getRequestDispatcher("/inventario.jsp").forward(request, response);
    }
}
