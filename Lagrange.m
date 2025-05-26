function [pol] = Lagrange(x, y)
    % Lagrange: Interpolación de Lagrange con manejo de errores.
    % Entrada:
    %   x: vector de valores distintos (abscisas)
    %   y: vector de valores correspondientes (ordenadas)
    % Salida:
    %   pol: coeficientes del polinomio interpolante

    % Validaciones básicas
    if ~isvector(x) || ~isvector(y)
        error('Las entradas deben ser vectores.');
    end

    if length(x) ~= length(y)
        error('Los vectores x e y deben tener la misma longitud.');
    end

    n = length(x);

    if length(unique(x)) < n
        error('Los valores de x deben ser distintos.');
    end

    % Inicialización
    Tabla = zeros(n, n);

    for i = 1:n
        Li = 1;
        den = 1;
        for j = 1:n
            if j ~= i
                paux = [1, -x(j)];
                Li = conv(Li, paux);
                den = den * (x(i) - x(j));
            end
        end
        Tabla(i, :) = y(i) * Li / den;
    end

    pol = sum(Tabla);  % Coeficientes del polinomio

    % Mostrar el polinomio simbólicamente en forma decimal (plana)
    syms t
    poly_sym = 0;
    grado = length(pol) - 1;
    for i = 1:length(pol)
        poly_sym = poly_sym + pol(i) * t^(grado - i + 1);
    end

    poly_sym = vpa(poly_sym, 6);  % Convertir a decimal con 6 cifras

    disp('Polinomio de interpolación (forma simbólica, decimal):')
    disp(char(poly_sym))

    % Graficar el polinomio
    fplot(poly_sym, [min(x)-1, max(x)+1], 'LineWidth', 2)
    hold on
    plot(x, y, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r')
    title('Polinomio de Interpolación de Lagrange')
    xlabel('x')
    ylabel('P(x)')
    grid on
    legend('Polinomio', 'Datos originales')
    hold off
end
