function [coef] = SplineLineal(x, y)
    % SplineLineal: Interpolación spline lineal con impresión y gráfica.
    % Entrada:
    %   x: nodos (vector de abscisas, ordenado y sin repetidos)
    %   y: valores en los nodos (vector de ordenadas)
    % Salida:
    %   coef: matriz (n-1)x2 con los coeficientes de cada tramo: [pendiente, constante]

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
    A = zeros(2*(n-1));
    b = zeros(2*(n-1),1);
    
    % Ecuaciones para extremos de cada tramo
    c = 1; h = 1;
    for i = 1:n-1
        A(i,c) = x(i);
        A(i,c+1) = 1;
        b(i) = y(i);
        c = c + 2;
        h = h + 1;
    end

    c = 1;
    for i = 2:n
        A(h,c) = x(i);
        A(h,c+1) = 1;
        b(h) = y(i);
        c = c + 2;
        h = h + 1;
    end

    % Resolver sistema
    sol = A \ b;
    coef = reshape(sol, 2, n-1)';

    % Mostrar los polinomios por tramos
    fprintf('Polinomio Spline Lineal por tramos:\n');
    for i = 1:n-1
        fprintf('P%d(x) = %.6f * x + %.6f,  x ∈ [%.2f, %.2f]\n', ...
            i, coef(i,1), coef(i,2), x(i), x(i+1));
    end

    % Graficar los tramos
    figure;
    hold on;
    for i = 1:n-1
        f = @(t) coef(i,1)*t + coef(i,2);
        fplot(f, [x(i), x(i+1)], 'LineWidth', 2);
    end
    plot(x, y, 'ro', 'MarkerFaceColor', 'r');
    grid on;
    xlabel('x');
    ylabel('Spline Lineal');
    title('Interpolación Spline Lineal');
    legend('Tramos lineales', 'Puntos de datos', 'Location', 'best');
    hold off;
end
