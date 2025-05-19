function [n, xn, fx, dfx, d2fx, E] = raices_multiples(f_input, x0, Tol, niter, error_type)
    syms x;

    % Validaciones básicas
    if nargin < 5
        error('Faltan argumentos: f_input, x0, Tol, niter, error_type');
    end

    if ~strcmpi(error_type, 'relativo') && ~strcmpi(error_type, 'absoluto')
        error('Tipo de error debe ser "relativo" o "absoluto".');
    end

    % Convertir función simbólica a función anónima
    if isa(f_input, 'sym')
        f_handle = matlabFunction(f_input);
        df_handle = matlabFunction(diff(f_input));
        d2f_handle = matlabFunction(diff(f_input, 2));
    elseif isa(f_input, 'function_handle')
        f_handle = f_input;
        syms x;
        f_sym = f_input(x); % intenta convertir a simbólica
        df_handle = matlabFunction(diff(f_sym));
        d2f_handle = matlabFunction(diff(f_sym, 2));
    else
        error('f_input debe ser función simbólica o función anónima.');
    end

    % Inicialización
    xn = x0;
    fx(1) = f_handle(xn);
    dfx(1) = df_handle(xn);
    d2fx(1) = d2f_handle(xn);
    E(1) = NaN;

    fprintf('\n-------------------------------------------------------------------------------\n');
    fprintf('| Iter |     Xn     |   f(Xn)   |  f''(Xn)  | f''''(Xn) |    Error (%s)   |\n', error_type);
    fprintf('-------------------------------------------------------------------------------\n');
    fprintf('| %4d | %10.6f | %9.3e | %8.3e | %8.3e |       ---       |\n', ...
        0, xn, fx(1), dfx(1), d2fx(1));

    c = 1;
    while c < niter
        % Fórmula de raíces múltiples
        denom = (dfx(c))^2 - fx(c) * d2fx(c);
        if denom == 0
            fprintf('\nError: división por cero en la iteración %d\n', c);
            break;
        end

        xn = xn - (fx(c) * dfx(c)) / denom;

        fx(c+1) = f_handle(xn);
        dfx(c+1) = df_handle(xn);
        d2fx(c+1) = d2f_handle(xn);

        % Cálculo del error
        if strcmpi(error_type, 'relativo')
            E(c+1) = abs((xn - x0) / max(abs(xn), eps));
        else
            E(c+1) = abs(xn - x0);
        end

        fprintf('| %4d | %10.6f | %9.3e | %8.3e | %8.3e | %14.5e |\n', ...
            c, xn, fx(c+1), dfx(c+1), d2fx(c+1), E(c+1));

        if abs(fx(c+1)) < 1e-12 || E(c+1) < Tol
            break;
        end

        x0 = xn;
        c = c + 1;
    end
    fprintf('-------------------------------------------------------------------------------\n');

    n = c;
    
    % Mensaje final
    if abs(fx(c+1)) < 1e-12
        fprintf('\n%.10f es raíz de f(x)\n', xn);
    elseif E(c+1) < Tol
        fprintf('\n%.10f es una aproximación de una raíz con tolerancia = %.10e\n', xn, Tol);
    else
        fprintf('\nEl método fracasó después de %d iteraciones\n', niter);
    end

    % === Gráfica nueva ===
    figure; % <-- fuerza una nueva ventana de figura
    xmin = x0 - 1; xmax = x0 + 1; % puedes ajustar esto si lo deseas
    fplot(f_handle, [xmin, xmax], 'b', 'LineWidth', 2); hold on;
    yline(0, 'r--');
    plot(xn, f_handle(xn), 'ro', 'MarkerFaceColor', 'r');
    grid on;
    title('Método de Raíces Múltiples');
    xlabel('x'); ylabel('f(x)');
    legend('f(x)', 'y = 0', 'Raíz aproximada');
end
