function [n, xn, fm, E] = pf(f, g, x0, Tol, niter, error_type)
    % Método de punto fijo con control de errores, tabla y gráfica
    % Entradas:
    %   f          -> función f(x) (anónima o simbólica)
    %   g          -> función de iteración g(x)
    %   x0         -> valor inicial
    %   Tol        -> tolerancia
    %   niter      -> número máximo de iteraciones
    %   error_type -> 'relativo' o 'absoluto'
    % Salidas:
    %   n          -> número de iteraciones realizadas
    %   xn         -> valores aproximados por iteración
    %   fm         -> f(xn)
    %   E          -> errores por iteración

    % Verificación de argumentos
    if nargin < 6
        error('Faltan argumentos. Debes ingresar f, g, x0, Tol, niter, error_type.');
    end
    if Tol <= 0
        error('La tolerancia debe ser positiva.');
    end
    if niter <= 0 || floor(niter) ~= niter
        error('niter debe ser un entero positivo.');
    end
    if ~strcmpi(error_type, 'relativo') && ~strcmpi(error_type, 'absoluto')
        error('El tipo de error debe ser ''relativo'' o ''absoluto''.');
    end

    % Convertir simbólicas a anónimas
    if isa(f, 'sym')
        f = matlabFunction(f);
    end
    if isa(g, 'sym')
        g = matlabFunction(g);
    end

    % Inicialización
    c = 0;
    xn(1) = x0;
    try
        fm(1) = f(x0);
    catch ME
        error('Error al evaluar f(x0): %s', ME.message);
    end
    E(1) = Tol + 1;

    % Encabezado de tabla
    fprintf('--------------------------------------------------------------------------------\n');
    fprintf('| Iter |        x_n        |      f(x_n)      |      Error (%s)      |\n', error_type);
    fprintf('--------------------------------------------------------------------------------\n');
    fprintf('| %4d | %16.10f | %16.10f | %16s |\n', c, xn(1), fm(1), '---');

    % Iteración de punto fijo
    while E(c + 1) > Tol && abs(fm(c + 1)) > 1e-12 && c < niter
        try
            xn(c + 2) = g(xn(c + 1));
            fm(c + 2) = f(xn(c + 2));
        catch ME
            error('Error al evaluar g o f en iteración %d: %s', c, ME.message);
        end

        % Calcular error
        if strcmpi(error_type, 'relativo')
            E(c + 2) = abs((xn(c + 2) - xn(c + 1)) / max(abs(xn(c + 2)), eps));
        else
            E(c + 2) = abs(xn(c + 2) - xn(c + 1));
        end

        c = c + 1;
        fprintf('| %4d | %16.10f | %16.10f | %16.10e |\n', ...
            c, xn(c + 1), fm(c + 1), E(c + 1));
    end

    fprintf('--------------------------------------------------------------------------------\n');

    % Salida final
    n = c;
    if abs(fm(end)) < 1e-12
        fprintf('\n%.10f es raíz exacta de f(x).\n', xn(end));
    elseif E(end) < Tol
        fprintf('\n%.10f es aproximación con tolerancia = %.10e\n', xn(end), Tol);
    else
        fprintf('\nEl método fracasó después de %d iteraciones.\n', niter);
    end

    % ---------- GRAFICA ----------
    % Generar un intervalo alrededor de la última aproximación
    span = max(1, abs(xn(end)));  % ajusta el rango según la magnitud
    x_vals = linspace(xn(end)-span, xn(end)+span, 200);
    y_vals = arrayfun(f, x_vals);

    figure;
    plot(x_vals, y_vals, 'b-', 'LineWidth', 2); hold on;
    yline(0, '--k', 'LineWidth', 1.5);
    plot(xn(end), f(xn(end)), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
    title('Método de Punto Fijo');
    xlabel('x'); ylabel('f(x)');
    legend('f(x)', 'y = 0', 'Raíz aproximada', 'Location', 'best');
    grid on;
end
