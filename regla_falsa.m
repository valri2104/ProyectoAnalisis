function [n, xn, fm, E] = regla_falsa(f, a, b, Tol, niter, error_type)
    % regla_falsa: Método de la Regla Falsa con control de errores y gráfica
    % Entradas:
    %   f          -> función (anónima o simbólica)
    %   a, b       -> extremos del intervalo
    %   Tol        -> tolerancia
    %   niter      -> número máximo de iteraciones
    %   error_type -> 'relativo' o 'absoluto'
    % Salidas:
    %   n   -> número de iteraciones
    %   xn  -> aproximaciones sucesivas
    %   fm  -> valores de f(xn)
    %   E   -> errores por iteración

    % Validaciones
    if nargin < 6
        error('Faltan argumentos. Debes ingresar: f, a, b, Tol, niter, error_type');
    end
    if Tol <= 0
        error('La tolerancia debe ser positiva.');
    end
    if niter <= 0 || floor(niter) ~= niter
        error('niter debe ser un entero positivo.');
    end
    if ~(strcmpi(error_type, 'relativo') || strcmpi(error_type, 'absoluto'))
        error('El tipo de error debe ser ''relativo'' o ''absoluto''.');
    end
    if isa(f, 'sym')
        f = matlabFunction(f);
    elseif ~isa(f, 'function_handle')
        error('f debe ser función anónima o simbólica.');
    end

    % Evaluar extremos
    fa = f(a); fb = f(b);
    if fa == 0
        xn = a; n = 0; fm = 0; E = 0;
        fprintf('%f es raíz exacta.\n', a); return;
    elseif fb == 0
        xn = b; n = 0; fm = 0; E = 0;
        fprintf('%f es raíz exacta.\n', b); return;
    elseif fa * fb > 0
        error('El intervalo no encierra una raíz. f(a)*f(b) > 0.');
    end

    % Inicialización
    xn = []; fm = []; E = []; c = 0;

    fprintf('\n---------------------------------------------------------------------\n');
    fprintf('| Iter |      Xn      |     f(Xn)     |     Error (%s)    |\n', error_type);
    fprintf('---------------------------------------------------------------------\n');

    % Iteraciones
    while c < niter && (c == 0 || E(c) > Tol)
        x_new = (a * fb - b * fa) / (fb - fa);
        f_new = f(x_new);

        xn(c + 1) = x_new;
        fm(c + 1) = f_new;

        if c > 0
            if strcmpi(error_type, 'relativo')
                E(c + 1) = abs((xn(c + 1) - xn(c)) / max(abs(xn(c + 1)), eps));
            else
                E(c + 1) = abs(xn(c + 1) - xn(c));
            end
        else
            E(1) = Tol + 1;
        end

        fprintf('|  %3d  |  %10.6f  |  %10.6f  |  %14.5e  |\n', ...
                c, x_new, f_new, E(c + 1));

        if fa * f_new < 0
            b = x_new; fb = f_new;
        else
            a = x_new; fa = f_new;
        end

        c = c + 1;
    end

    fprintf('---------------------------------------------------------------------\n');

    % Resultado final
    n = c;
    if abs(fm(end)) < 1e-12
        fprintf('%f es una raíz exacta.\n', xn(end));
    elseif E(end) < Tol
        fprintf('%f es una aproximación de la raíz con tolerancia %f.\n', xn(end), Tol);
    else
        fprintf('El método fracasó después de %d iteraciones.\n', niter);
    end

    % Gráfica
    figure;
    fplot(f, [a b], 'LineWidth', 1.5); hold on;
    plot(xn, fm, 'ro-', 'MarkerFaceColor', 'r');
    xlabel('x'); ylabel('f(x)');
    title('Método de la Regla Falsa');
    grid on;
    legend('f(x)', 'Aproximaciones xn');
end
