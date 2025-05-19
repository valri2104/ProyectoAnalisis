function [E, s] = Jacobi(x0, A, b, Tol, niter, tipoError)
    E = [];
    s = [];

    try
        % Validaciones
        if nargin < 6
            error('Faltan argumentos. Debes ingresar: x0, A, b, Tol, niter, tipoError');
        end

        if ~ismatrix(A) || size(A,1) ~= size(A,2)
            error('La matriz A debe ser cuadrada.');
        end

        if length(b) ~= size(A,1) || length(x0) ~= size(A,1)
            error('Las dimensiones de x0, A y b no son compatibles.');
        end

        if Tol <= 0
            error('La tolerancia debe ser un número positivo.');
        end

        if niter <= 0 || floor(niter) ~= niter
            error('niter debe ser un entero positivo.');
        end

        if ~strcmpi(tipoError, 'relativo') && ~strcmpi(tipoError, 'absoluto')
            error('tipoError debe ser "relativo" o "absoluto".');
        end

        % Verificar diagonal dominante
        isDD = true;
        for i = 1:size(A,1)
            diagElem = abs(A(i,i));
            offDiagSum = sum(abs(A(i,:))) - diagElem;
            if diagElem <= offDiagSum
                isDD = false;
                break;
            end
        end
        if ~isDD
            warning('La matriz A no es diagonalmente dominante. El método podría no converger.');
        end

        % Inicialización
        D = diag(diag(A));
        L = -tril(A, -1);
        U = -triu(A, 1);
        T = inv(D) * (L + U);
        C = inv(D) * b;
        c = 0;
        error_val = Tol + 1;
        n = length(x0);

        X = zeros(n, niter + 1); % Matriz para guardar evolución de las variables
        X(:, 1) = x0;

        % Encabezado de tabla
        fprintf('--------------------------------------------------------------------------------------------------\n');
        fprintf('| Iter |');
        for i = 1:n
            fprintf('      x(%d)       |', i);
        end
        fprintf('     Error (%s)     |\n', tipoError);
        fprintf('--------------------------------------------------------------------------------------------------\n');

        % Primera fila (x0)
        fprintf('| %4d |', c);
        for i = 1:n
            fprintf(' %14.6f |', x0(i));
        end
        fprintf('         ---         |\n');

        % Iteraciones
        while error_val > Tol && c < niter
            x1 = T * x0 + C;

            if strcmpi(tipoError, 'relativo')
                error_val = norm(x1 - x0, inf) / max(norm(x1, inf), eps);
            else
                error_val = norm(x1 - x0, inf);
            end

            E(c + 1) = error_val;
            c = c + 1;
            x0 = x1;
            X(:, c + 1) = x0; % almacenar siguiente aproximación

            fprintf('| %4d |', c);
            for i = 1:n
                fprintf(' %14.6f |', x0(i));
            end
            fprintf(' %18.10e |\n', E(c));
        end

        fprintf('--------------------------------------------------------------------------------------------------\n');

        % Salida
        s = x0;
        if error_val < Tol
            fprintf('\nJacobi: El método convergió. Solución aproximada con tolerancia %.2e:\n', Tol);
            disp(s');
        else
            fprintf('\nJacobi: El método fracasó después de %d iteraciones.\n', niter);
        end

        % Gráfica de evolución de variables
        figure;
        plot(0:c, X(:, 1:c+1)', '-o', 'LineWidth', 1.5);
        xlabel('Iteración');
        ylabel('Valor de las variables');
        legend(arrayfun(@(i) sprintf('x(%d)', i), 1:n, 'UniformOutput', false));
        title('Evolución de las variables (Jacobi)');
        grid on;

    catch ME
        fprintf('Error en Jacobi: %s\n', ME.message);
    end
end
