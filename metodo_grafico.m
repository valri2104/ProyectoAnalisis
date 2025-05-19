function [n, X, FX, E] = metodo_grafico(f_input, a, b, Tol, niter, error_type)
    % Método gráfico para aproximar raíces de f(x)
    % Entradas:
    %   f_input     -> función simbólica o anónima
    %   a, b        -> intervalo de evaluación
    %   Tol         -> tolerancia
    %   niter       -> máximo de puntos (resolución)
    %   error_type  -> 'relativo' o 'absoluto'

    % Validaciones
    if nargin < 6
        error('Faltan argumentos. Se requieren: f_input, a, b, Tol, niter, error_type.');
    end
    if ~isa(f_input, 'function_handle') && ~isa(f_input, 'sym')
        error('La función debe ser simbólica o anónima.');
    end
    if a >= b
        error('El valor de "a" debe ser menor que "b".');
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

    % Convertir función simbólica a anónima
    if isa(f_input, 'sym')
        f = matlabFunction(f_input);
    else
        f = f_input;
    end

    % Preparar puntos a evaluar
    X = linspace(a, b, niter);
    FX = zeros(1, niter);
    E = zeros(1, niter);
    raiz_aprox = NaN;

    fprintf('\n----------------------------------------------------------------------------\n');
    fprintf('|  Idx |     X      |    f(X)     |     Error (%s)     |\n', error_type);
    fprintf('----------------------------------------------------------------------------\n');

    for i = 1:niter
        FX(i) = f(X(i));
        
        % Calcular error si no es la primera iteración
        if i == 1
            E(i) = NaN;
            fprintf('| %4d | %9.6f | %10.6f |     ---           |\n', i, X(i), FX(i));
        else
            if strcmpi(error_type, 'relativo')
                E(i) = abs((X(i) - X(i - 1)) / max(abs(X(i)), eps));
            else
                E(i) = abs(X(i) - X(i - 1));
            end

            fprintf('| %4d | %9.6f | %10.6f | %16.5e |\n', i, X(i), FX(i), E(i));
            
            % Criterio de cambio de signo
            if FX(i - 1) * FX(i) < 0 && isnan(raiz_aprox)
                % Se detecta cambio de signo, aproximamos raíz
                if abs(FX(i)) < abs(FX(i - 1))
                    raiz_aprox = X(i);
                else
                    raiz_aprox = X(i - 1);
                end
            end
        end

        % Si ya hay raíz aproximada con tolerancia, salir
        if i > 1 && ~isnan(raiz_aprox) && E(i) < Tol
            break;
        end
    end

    fprintf('----------------------------------------------------------------------------\n');

    % Resultado final
    n = i;

    if ~isnan(raiz_aprox)
        fprintf('\nLa raíz aproximada es %.10f con tolerancia %.2e\n', raiz_aprox, Tol);
    else
        fprintf('\nNo se detectó un cambio de signo en el intervalo.\n');
    end

    % Gráfica
    figure;
    plot(X, FX, 'b-', 'LineWidth', 2); grid on; hold on;
    yline(0, 'r--');
    title('Método Gráfico para Raíces');
    xlabel('x');
    ylabel('f(x)');

    if ~isnan(raiz_aprox)
        plot(raiz_aprox, f(raiz_aprox), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
        legend('f(x)', 'y = 0', 'Raíz aproximada');
    else
        legend('f(x)', 'y = 0');
    end
end
