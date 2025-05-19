function [n, xn, fm, dfm, E] = newton(f_input, x0, Tol, niter, error_type)
    % Método de Newton-Raphson con gráfico al final

    % Validación
    if nargin < 5
        error('Faltan argumentos. Se requieren: f_input, x0, Tol, niter, error_type.');
    end
    if Tol <= 0 || niter <= 0 || floor(niter) ~= niter
        error('Tolerancia debe ser positiva y niter un entero positivo.');
    end
    if ~strcmpi(error_type, 'relativo') && ~strcmpi(error_type, 'absoluto')
        error('Tipo de error debe ser "relativo" o "absoluto".');
    end

    % Convertir función simbólica a anónima
    if isa(f_input, 'sym')
        syms x
        f = matlabFunction(f_input, 'vars', x);
        df = matlabFunction(diff(f_input), 'vars', x);
    elseif isa(f_input, 'function_handle')
        syms x
        try
            f_sym = f_input(x);  % convertir a simbólica para derivar
            f = matlabFunction(f_sym, 'vars', x);
            df = matlabFunction(diff(f_sym), 'vars', x);
        catch
            error('La función anónima debe poder evaluarse simbólicamente para derivarla.');
        end
    else
        error('f_input debe ser una función anónima o simbólica.');
    end

    % Inicialización
    c = 0;
    xn = x0;
    E = Tol + 1;
    errores = [];
    iteraciones = [];

    try
        fm = f(xn);
        dfm = df(xn);
    catch ME
        error('Error al evaluar f o f'' en x0: %s', ME.message);
    end

    fprintf('\n----------------------------------------------------------------------------\n');
    fprintf("| Iter |     Xn     |    F(Xn)    |   F'(Xn)   |   Error (%s)   |\n", error_type);
    fprintf('----------------------------------------------------------------------------\n');

    while E > Tol && abs(fm) > 1e-12 && c < niter
        if dfm == 0
            fprintf("\nF'(Xn) = 0. Posible raíz múltiple o método inválido.\n");
            break;
        end

        x_new = xn - fm / dfm;

        if strcmpi(error_type, 'relativo')
            E = abs((x_new - xn) / max(abs(x_new), eps));
        else
            E = abs(x_new - xn);
        end

        xn = x_new;
        fm = f(xn);
        dfm = df(xn);

        fprintf('| %4d | %10.6f | %10.6f | %10.6f | %14.5e |\n', ...
                c, xn, fm, dfm, E);

        errores(end+1) = E;
        iteraciones(end+1) = xn;
        c = c + 1;
    end

    fprintf('----------------------------------------------------------------------------\n');

    % Mensaje final
    if abs(fm) < 1e-12
        fprintf('\n%.10f es raíz exacta de f(x)\n', xn);
    elseif E < Tol
        fprintf('\n%.10f es una aproximación con tolerancia %.2e\n', xn, Tol);
    elseif dfm == 0
        fprintf('\n%.10f es una posible raíz múltiple (f''(x)=0)\n', xn);
    else
        fprintf('\nEl método fracasó después de %d iteraciones.\n', niter);
    end

    n = c;

    % -------------------
    % GRÁFICA DE LA FUNCIÓN
    % -------------------
    x_vals = linspace(xn - 1, xn + 1, 400);
    y_vals = arrayfun(f, x_vals);

    figure;
    plot(x_vals, y_vals, 'b-', 'LineWidth', 2); hold on;
    yline(0, 'k--', 'LineWidth', 1);
    plot(xn, f(xn), 'ro', 'MarkerFaceColor', 'r', 'DisplayName', 'Raíz aproximada');

    title('Método de Newton-Raphson');
    xlabel('x');
    ylabel('f(x)');
    legend('f(x)', 'y = 0', 'Raíz aproximada', 'Location', 'best');
    grid on;
end
