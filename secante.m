function [n, X, FX, E] = secante(f_input, x0, x1, Tol, niter, error_type)
    % Método de la secante para encontrar raíces con gráfica incluida
    % Entradas:
    %   f_input    -> función simbólica o anónima
    %   x0, x1     -> valores iniciales
    %   Tol        -> tolerancia
    %   niter      -> número máximo de iteraciones
    %   error_type -> 'relativo' o 'absoluto'

    % Validaciones
    if nargin < 6
        error('Faltan argumentos. Se requieren: f_input, x0, x1, Tol, niter, error_type.');
    end
    if ~isa(f_input, 'function_handle') && ~isa(f_input, 'sym')
        error('La función debe ser simbólica o anónima.');
    end
    if Tol <= 0
        error('La tolerancia debe ser positiva.');
    end
    if niter <= 1 || floor(niter) ~= niter
        error('niter debe ser un entero mayor que 1.');
    end
    if ~strcmpi(error_type, 'relativo') && ~strcmpi(error_type, 'absoluto')
        error('El tipo de error debe ser "relativo" o "absoluto".');
    end

    % Convertir función simbólica a anónima si es necesario
    if isa(f_input, 'sym')
        f = matlabFunction(f_input);
    else
        f = f_input;
    end

    % Inicialización
    X = zeros(1, niter);
    FX = zeros(1, niter);
    E = NaN(1, niter);

    X(1) = x0;
    X(2) = x1;
    FX(1) = f(x0);
    FX(2) = f(x1);

    fprintf('\n-------------------------------------------------------------------------------\n');
    fprintf('| Iter |     x_n     |    f(x_n)   |     Error (%s)     |\n', error_type);
    fprintf('-------------------------------------------------------------------------------\n');
    fprintf('| %4d | %10.6f | %10.6f |       ---         |\n', 1, X(1), FX(1));
    fprintf('| %4d | %10.6f | %10.6f |       ---         |\n', 2, X(2), FX(2));

    for n = 3:niter
        if (FX(n - 1) - FX(n - 2)) == 0
            error('División por cero en la iteración %d. Método fracasó.', n);
        end

        X(n) = X(n - 1) - FX(n - 1) * (X(n - 1) - X(n - 2)) / (FX(n - 1) - FX(n - 2));
        FX(n) = f(X(n));

        % Error
        if strcmpi(error_type, 'relativo')
            E(n) = abs((X(n) - X(n - 1)) / max(abs(X(n)), eps));
        else
            E(n) = abs(X(n) - X(n - 1));
        end

        fprintf('| %4d | %10.6f | %10.6f | %16.5e |\n', n, X(n), FX(n), E(n));

        if abs(FX(n)) < 1e-12 || E(n) < Tol
            break;
        end
    end

    fprintf('-------------------------------------------------------------------------------\n');

    % Resultado final
    if abs(FX(n)) < 1e-12
        fprintf('\n%f es raíz de f(x)\n', X(n));
    elseif E(n) < Tol
        fprintf('\n%f es una aproximación de una raíz con tolerancia %e\n', X(n), Tol);
    else
        fprintf('\nEl método fracasó después de %d iteraciones\n', niter);
    end

    % Recortar salida a n iteraciones reales
    X = X(1:n);
    FX = FX(1:n);
    E = E(1:n);

    % === GRAFICAR ===
    figure;
    fplot(f, [min(X)-1, max(X)+1], 'b-', 'LineWidth', 2); hold on;
    yline(0, 'r--');
    plot(X, FX, 'ko-', 'MarkerFaceColor', 'g', 'LineWidth', 1.5);
    plot(X(end), FX(end), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
    title('Método de la Secante');
    xlabel('x');
    ylabel('f(x)');
    legend('f(x)', 'y = 0', 'Iteraciones', 'Raíz aproximada', 'Location', 'best');
    grid on;
end