function [s,E,fm] = Biseccion(f, xi, xs, Tol, niter, error_type)
    % Bisección con gráfica y manejo de errores
    if nargin < 6
        error('Faltan argumentos. Debes ingresar: f, xi, xs, Tol, niter, error_type');
    end
    if Tol <= 0
        error('La tolerancia debe ser positiva.');
    end
    if niter <= 0 || floor(niter) ~= niter
        error('niter debe ser un entero positivo.');
    end
    if ~(strcmpi(error_type, 'relativo') || strcmpi(error_type, 'absoluto'))
        error('El tipo de error debe ser ''relativo'' o ''absoluto''.');
    end

    % Convertir función simbólica si es necesario
    if isa(f, 'sym')
        f = matlabFunction(f, 'vars', {'x'});
    elseif ~isa(f, 'function_handle')
        error('f debe ser una función anónima o simbólica.');
    end

    % Guardar valores originales para graficar
    xi0 = xi;
    xs0 = xs;

    fi = f(xi);
    fs = f(xs);
    c = 0;
    E = [];
    fm = [];

    % Tabla de resultados
    fprintf('--------------------------------------------------------------------------------\n');
    fprintf('| Iter |    xi    |    xs    |    xm    |  f(xm)   |     Error (%s)    |\n', error_type);
    fprintf('--------------------------------------------------------------------------------\n');

    if fi == 0
        xm = xi;
        fprintf('|  %3d | %8.5f | %8.5f | %8.5f | %8.5f |       ---        |\n', c, xi, xs, xm, fi);
        fprintf('--------------------------------------------------------------------------------\n');
        fprintf('%f es raíz de f(x)\n', xi);
        s = xi;
        E = 0;
        fm = fi;
        return;
    elseif fs == 0
        xm = xs;
        fprintf('|  %3d | %8.5f | %8.5f | %8.5f | %8.5f |       ---        |\n', c, xi, xs, xm, fs);
        fprintf('--------------------------------------------------------------------------------\n');
        fprintf('%f es raíz de f(x)\n', xs);
        s = xs;
        E = 0;
        fm = fs;
        return;
    elseif fi * fs > 0
        error('El intervalo [%f, %f] no es adecuado. f(xi)*f(xs) > 0', xi, xs);
    end

    xm = (xi + xs) / 2;
    fm(1) = f(xm);
    fe = fm(1);
    error_val = Tol + 1;
    E(1) = error_val;

    fprintf('|  %3d | %8.5f | %8.5f | %8.5f | %8.5f | %14.5e |\n', c, xi, xs, xm, fe, error_val);

    while error_val > Tol && fe ~= 0 && c < niter
        if fi * fe < 0
            xs = xm;
            fs = f(xs);
        else
            xi = xm;
            fi = f(xi);
        end

        xa = xm;
        xm = (xi + xs) / 2;
        fm(c + 2) = f(xm);
        fe = fm(c + 2);

        if strcmpi(error_type, 'relativo')
            error_val = abs((xm - xa) / max(abs(xm), eps));
        else
            error_val = abs(xm - xa);
        end

        E(c + 2) = error_val;
        c = c + 1;

        fprintf('|  %3d | %8.5f | %8.5f | %8.5f | %8.5f | %14.5e |\n', c, xi, xs, xm, fe, error_val);
    end

    fprintf('--------------------------------------------------------------------------------\n');

    s = xm;
    if fe == 0
        fprintf('%f es raíz exacta de f(x)\n', xm);
    elseif error_val < Tol
        fprintf('%f es una aproximación de una raíz con tolerancia = %e\n', xm, Tol);
    else
        fprintf('El método fracasó después de %d iteraciones\n', niter);
    end

    % ---------- GRÁFICA ----------
    figure;
    x_vals = linspace(xi0, xs0, 100);        % Usar intervalo original
    y_vals = arrayfun(f, x_vals);            % Evaluar la función correctamente
    plot(x_vals, y_vals, 'b', 'LineWidth', 2); hold on;
    yline(0, '--k', 'LineWidth', 1.5);
    plot(s, f(s), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
    title('Método de Bisección');
    xlabel('x'); ylabel('f(x)');
    legend('f(x)', 'y = 0', 'Raíz aproximada');
    grid on;
end
