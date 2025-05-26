function [coef] = SplineCubico(x, y)
    % SplineCubico: Interpolación spline cúbico natural.
    % Entrada:
    %   x: nodos (vector de abscisas, ordenado y sin repetidos)
    %   y: valores en los nodos (vector de ordenadas)
    % Salida:
    %   coef: matriz (n-1)x4 con los coeficientes de cada tramo: [a, b, c, d]

    % Validaciones
    if ~isvector(x) || ~isvector(y)
        error('Las entradas deben ser vectores.');
    end
    if length(x) ~= length(y)
        error('Los vectores x e y deben tener la misma longitud.');
    end
    if length(unique(x)) ~= length(x)
        error('Los valores de x deben ser distintos.');
    end
    if any(diff(x) <= 0)
        error('x debe estar ordenado estrictamente de forma creciente.');
    end

    n = length(x);
    N = 4 * (n - 1);  % Número de incógnitas
    A = zeros(N);
    b = zeros(N, 1);

    % Ecuaciones: coincidencia en los extremos de cada intervalo
    row = 1;
    col = 1;
    for i = 1:n-1
        xi = x(i);
        A(row, col:col+3) = [xi^3, xi^2, xi, 1];
        b(row) = y(i);
        row = row + 1;
        col = col + 4;
    end

    col = 1;
    for i = 2:n
        xi = x(i);
        A(row, col:col+3) = [xi^3, xi^2, xi, 1];
        b(row) = y(i);
        row = row + 1;
        col = col + 4;
    end

    % Derivadas de primer orden iguales en puntos interiores
    col = 1;
    for i = 2:n-1
        xi = x(i);
        A(row, col:col+2) = [3*xi^2, 2*xi, 1];
        A(row, col+4:col+6) = [-3*xi^2, -2*xi, -1];
        b(row) = 0;
        row = row + 1;
        col = col + 4;
    end

    % Derivadas de segundo orden iguales en puntos interiores
    col = 1;
    for i = 2:n-1
        xi = x(i);
        A(row, col:col+1) = [6*xi, 2];
        A(row, col+4:col+5) = [-6*xi, -2];
        b(row) = 0;
        row = row + 1;
        col = col + 4;
    end

    % Condición de spline natural (segunda derivada = 0 en extremos)
    A(row, 1:2) = [6*x(1), 2];  % en x1
    b(row) = 0;
    row = row + 1;
    A(row, end-3:end-2) = [6*x(end), 2];  % en xn
    b(row) = 0;

    % Resolución del sistema
    sol = A \ b;
    coef = reshape(sol, 4, n-1)';  % Cada fila: [a b c d] de a*x^3 + b*x^2 + c*x + d

    % Mostrar los polinomios por tramos
    fprintf('Polinomio Spline Cúbico por tramos:\n');
    for i = 1:n-1
        fprintf('P%d(x) = %.6f*x^3 + %.6f*x^2 + %.6f*x + %.6f,  x ∈ [%.2f, %.2f]\n', ...
            i, coef(i,1), coef(i,2), coef(i,3), coef(i,4), x(i), x(i+1));
    end

    % Graficar los tramos
    figure;
    hold on;
    for i = 1:n-1
        a = coef(i,1); b_ = coef(i,2); c = coef(i,3); d = coef(i,4);
        f = @(t) a*t.^3 + b_*t.^2 + c*t + d;
        fplot(f, [x(i), x(i+1)], 'LineWidth', 2);
    end
    plot(x, y, 'ro', 'MarkerFaceColor', 'r');
    grid on;
    xlabel('x');
    ylabel('Spline Cúbico');
    title('Interpolación Spline Cúbico Natural');
    legend('Tramos cúbicos', 'Puntos de datos', 'Location', 'best');
    hold off;
end
