function [pol] = Newtonint(x, y)
    % Newtonint: Interpolación de Newton con diferencias divididas.
    % Entrada:
    %   x: vector de valores distintos (abscisas)
    %   y: vector de valores correspondientes (ordenadas)
    % Salida:
    %   pol: polinomio interpolante en forma simbólica

    % Validaciones
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

    % Construcción de la tabla de diferencias divididas
    Tabla = zeros(n, n);
    Tabla(:,1) = y(:);  % primera columna: y

    for j = 2:n
        for i = j:n
            Tabla(i,j) = (Tabla(i,j-1) - Tabla(i-1,j-1)) / (x(i) - x(i-j+1));
        end
    end

    % Coeficientes de Newton (diagonal superior de la tabla)
    coef = diag(Tabla);

    % Construcción simbólica del polinomio
    syms t
    poly_sym = coef(1);
    term = 1;

    for i = 2:n
        term = term * (t - x(i-1));
        poly_sym = poly_sym + coef(i) * term;
    end

    poly_sym = vpa(poly_sym, 6);  % Polinomio en decimales con 6 cifras

    % Mostrar el polinomio como string plano
    disp('Polinomio de interpolación (forma simbólica, decimal):')
    disp(char(poly_sym))

    % Graficar el polinomio
    fplot(poly_sym, [min(x)-1, max(x)+1], 'LineWidth', 2)
    hold on
    plot(x, y, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r')
    title('Polinomio de Interpolación de Newton')
    xlabel('x')
    ylabel('P(x)')
    grid on
    legend('Polinomio', 'Datos originales')
    hold off

    % Devolver el polinomio simbólico
    pol = poly_sym;
end
