function [X, errores] = SOR(x0, A, b, Tol, niter, w, tipo_error)
    % Método SOR robusto con selección de error, tabla formateada y gráfica de evolución

    % ---------------- Validaciones de entrada ----------------
    if nargin < 7
        error('Faltan argumentos. Se requieren: x0, A, b, Tol, niter, w, tipo_error.');
    end

    if ~isnumeric(A) || ~ismatrix(A)
        error('A debe ser una matriz numérica.');
    end

    [n, m] = size(A);
    if n ~= m
        error('La matriz A debe ser cuadrada.');
    end

    if ~isvector(b) || length(b) ~= n
        error('b debe ser un vector columna con la misma longitud que A.');
    end

    if ~isvector(x0) || length(x0) ~= n
        error('x0 debe ser un vector con la misma longitud que b.');
    end

    if Tol <= 0
        error('La tolerancia debe ser positiva.');
    end

    if niter <= 0 || floor(niter) ~= niter
        error('niter debe ser un entero positivo.');
    end

    if w <= 0 || w >= 2
        warning('El valor de w está fuera del rango típico (0 < w < 2), puede no converger.');
    end

    if ~(strcmpi(tipo_error, 'relativo') || strcmpi(tipo_error, 'absoluto'))
        error('El tipo de error debe ser ''relativo'' o ''absoluto''.');
    end

    % ---------------- Inicialización ----------------
    fprintf('\n==============================================\n');
    fprintf('Método SOR (Forma Matricial)\n');
    fprintf('w (factor de relajación): %.2f\n', w);
    fprintf('Tolerancia: %.4e\n', Tol);
    fprintf('Tipo de error: %s\n', tipo_error);
    fprintf('Iteración inicial: X0 = [%s]\n', num2str(x0));
    fprintf('==============================================\n\n');

    D = diag(diag(A));
    L = tril(A, -1);
    U = triu(A, 1);

    try
        T = inv(D - w*L) * ((1 - w)*D + w*U);
        C = w * inv(D - w*L) * b;
    catch
        error('Error al invertir la matriz D - wL. Puede que sea singular o mal condicionada.');
    end

    X = x0(:); % Asegura vector columna
    errores = [];
    historial = X';  % Guardamos la primera iteración como fila

    % ---------------- Impresión de tabla ----------------
    fprintf('---------------------------------------------------------------------------------\n');
    fprintf('| Iter |%12s|%12s|%12s|     Error (%s)     |\n', 'x1', 'x2', 'x3', tipo_error);
    fprintf('---------------------------------------------------------------------------------\n');

    for k = 1:niter
        X_old = X;
        X = T * X_old + C;

        if strcmpi(tipo_error, 'relativo')
            divisor = max(abs(X), eps);  % Protección contra división por cero
            Err = norm((X - X_old) ./ divisor, inf);
        else
            Err = norm(X - X_old);
        end

        errores(k) = Err;
        historial(end+1, :) = X';  % Guardar nueva iteración como fila

        % Imprimir fila de tabla
        fprintf('| %4d | %11.6f | %11.6f | %11.6f | %18.10e |\n', ...
                k, X(1), X(2), X(3), Err);

        if Err < Tol
            fprintf('---------------------------------------------------------------------------------\n');
            fprintf('Convergencia alcanzada en %d iteraciones.\n', k);
            fprintf('Solución aproximada: [%s]\n', num2str(X', '%.6f '));
            break;
        end
    end

    if k == niter && Err >= Tol
        fprintf('---------------------------------------------------------------------------------\n');
        fprintf('No se alcanzó la tolerancia después de %d iteraciones.\n', niter);
        fprintf('Última solución calculada: [%s]\n', num2str(X', '%.6f '));
    end

    % ---------------- Gráfica de evolución de variables ----------------
    figure;
    plot(0:k, historial(:,1), '-o', 'LineWidth', 1.5);
    hold on;
    plot(0:k, historial(:,2), '-s', 'LineWidth', 1.5);
    plot(0:k, historial(:,3), '-^', 'LineWidth', 1.5);
    grid on;
    xlabel('Iteración');
    ylabel('Valor de las variables');
    title('Evolución de las variables por iteración (Método SOR)');
    legend('x1', 'x2', 'x3', 'Location', 'best');
end
