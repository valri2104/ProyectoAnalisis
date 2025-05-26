function pol = Vandermonde(x, y)
    % VandermondeInterpolacion: Interpolación mediante el método de Vandermonde.
    % Entrada:
    %   x: vector de nodos (abscisas), deben ser distintos
    %   y: vector de valores en los nodos
    % Salida:
    %   pol: polinomio interpolante en forma simbólica

    % Validaciones
    if ~isvector(x) || ~isvector(y)
        error('Las entradas deben ser vectores.');
    end
    if length(x) ~= length(y)
        error('Los vectores x e y deben tener la misma longitud.');
    end
    if length(unique(x)) < length(x)
        error('Los valores de x deben ser distintos.');
    end

    n = length(x);

    % Matriz de Vandermonde
    V = zeros(n);
    for i = 1:n
        V(i, :) = x(i).^(n-1:-1:0);
    end

    % Resolver sistema
    coef = V \ y(:);

    % Polinomio simbólico
    syms t
    pol = 0;
    for i = 1:n
        pol = pol + coef(i) * t^(n - i);
    end

    % Mostrar polinomio en forma simbólica (decimal)
    pol_decimal = vpa(pol, 6);
    disp('Polinomio de interpolación (forma simbólica, decimal):')
    disp(char(pol_decimal))

    % Gráfica
    fplot(pol_decimal, [min(x)-1, max(x)+1], 'LineWidth', 2)
    hold on
    plot(x, y, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r')
    title('Polinomio de Interpolación - Método de Vandermonde')
    xlabel('x')
    ylabel('P(x)')
    grid on
    legend('Polinomio', 'Datos originales')
    hold off
end
