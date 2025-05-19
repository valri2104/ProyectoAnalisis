function [E, s] = GaussSeidel(x0, A, b, Tol, niter, tipoError)
    E = [];
    s = [];

    try
        % Validaciones de entrada
        if nargin < 6
            error('Faltan argumentos. Debes ingresar: x0, A, b, Tol, niter, tipoError');
        end

        if ~ismatrix(A) || size(A,1) ~= size(A,2)
            error('La matriz A debe ser cuadrada.');
        end

        if ~isvector(x0) || ~isvector(b)
            error('x0 y b deben ser vectores.');
        end

        if length(x0) ~= size(A,1) || length(b) ~= size(A,1)
            error('Las dimensiones de x0 o b no coinciden con A.');
        end

        if Tol <= 0
            error('La tolerancia debe ser positiva.');
        end

        if niter <= 0 || floor(niter) ~= niter
            error('El número de iteraciones debe ser un entero positivo.');
        end

        if ~strcmpi(tipoError, 'relativo') && ~strcmpi(tipoError, 'absoluto')
            error('El tipo de error debe ser "relativo" o "absoluto".');
        end

        % Verificación de diagonal dominante (sugerida para convergencia)
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

        try
            T = inv(D - L) * U;
            C = inv(D - L) * b;
        catch
            error('Error al invertir D - L. Verifica que no sea singular.');
        end

        c = 0;
        error_val = Tol + 1;
        n = length(x0);

        % Tabla de iteraciones (opcional: puedes eliminarla si no deseas salida visual)
        fprintf('--------------------------------------------------------------------------------------------------\n');
        fprintf('| Iter |');
        for i = 1:n
            fprintf('      x(%d)       |', i);
        end
        fprintf('     Error (%s)     |\n', tipoError);
        fprintf('--------------------------------------------------------------------------------------------------\n');

        % Primera fila
        fprintf('| %4d |', c);
        for i = 1:n
            fprintf(' %14.6f |', x0(i));
        end
        fprintf('         ---         |\n');

        % Iteraciones
        while error_val > Tol && c < niter
            x1 = zeros(n,1);
            for i = 1:n
                suma1 = A(i,1:i-1) * x1(1:i-1);
                suma2 = A(i,i+1:n) * x0(i+1:n);
                x1(i) = (b(i) - suma1 - suma2) / A(i,i);
            end

            if strcmpi(tipoError, 'relativo')
                error_val = norm(x1 - x0, inf) / max(norm(x1, inf), eps);
            else
                error_val = norm(x1 - x0, inf);
            end

            E(c + 1) = error_val;
            x0 = x1;
            c = c + 1;

            fprintf('| %4d |', c);
            for i = 1:n
                fprintf(' %14.6f |', x0(i));
            end
            fprintf(' %18.10e |\n', E(c));
        end

        fprintf('--------------------------------------------------------------------------------------------------\n');

        % Salida final
        s = x0;
        if error_val < Tol
            fprintf('\nGauss-Seidel: El método convergió. Solución aproximada con tolerancia %.2e:\n', Tol);
            disp(s');
        else
            fprintf('\nGauss-Seidel: El método fracasó después de %d iteraciones.\n', niter);
        end

    catch ME
        fprintf('Error en Gauss-Seidel: %s\n', ME.message);
    end
end
