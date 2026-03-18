import numpy as np
from matplotlib import pyplot as plt


def generate_data(n_points=100, noise_level=0.15, seed=42) -> dict:
    np.random.seed(seed)
    datasets = {}

    # Конфигурация линий
    configs = [
        {'name': 'line_1', 'type': 'linear', 'params': (2, 1)},          # k, b
        {'name': 'line_2', 'type': 'linear', 'params': (-0.5, 5)},       # k, b
        {'name': 'parabola_1', 'type': 'poly2', 'params': (0.1, -2, 10)} # a, b, c
    ]

    for conf in configs:
        name = conf['name']
        l_type = conf['type']
        params = conf['params']

        # Чистые данные
        x_clean = np.linspace(-10, 10, n_points)

        if l_type == 'linear':
            k, b = params
            y_clean = k * x_clean + b
        elif l_type == 'poly2':
            a, b, c = params
            y_clean = a * x_clean ** 2 + b * x_clean + c
        else:
            continue

        # Расчет величины шума
        range_val = max(y_clean.max() - y_clean.min(), x_clean.max() - x_clean.min())
        noise_magnitude = range_val * noise_level

        # 1. Данные для Матричного и Взвешенного МНК (Шум ТОЛЬКО в Y)
        noise_y_matrix = np.random.normal(0, noise_magnitude, n_points)
        x_matrix = x_clean.copy()
        y_matrix = y_clean + noise_y_matrix

        # 2. Данные для Полного МНК (Шум в X и Y)
        noise_x_total = np.random.normal(0, noise_magnitude, n_points)
        noise_y_total = np.random.normal(0, noise_magnitude, n_points)
        x_total = x_clean + noise_x_total
        y_total = y_clean + noise_y_total

        datasets[name] = {
            'type': l_type,
            'params': params,
            'clean': (x_clean, y_clean),
            'matrix': (x_matrix, y_matrix),
            'total': (x_total, y_total)
        }

    return datasets


def matrix_mnk(x, y, degree=1):
    if degree == 1:
        X_mat = np.column_stack((np.ones(len(x)), x))
    elif degree == 2:
        X_mat = np.column_stack((np.ones(len(x)), x, x ** 2))
    else:
        raise ValueError("Поддерживаются только степени 1 и 2")

    # Формула: theta = (X^T * X)^-1 * X^T * Y
    Xt = X_mat.T
    Xt_X = Xt @ X_mat
    Xt_X_inv = np.linalg.inv(Xt_X)
    Xt_Y = Xt @ y

    theta = Xt_X_inv @ Xt_Y
    return theta


def total_mnk(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_centered = x - x_mean
    y_centered = y - y_mean

    A = np.column_stack((x_centered, y_centered))

    # Сингулярное разложение (SVD)
    # A = U * S * Vt
    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    normal = Vt[-1, :]
    vx, vy = normal

    k = -vx / vy
    b = y_mean - k * x_mean

    return k, b


def weighted_mnk(x, y, degree=1):
    x_norm = (x - x.min()) / (x.max() - x.min() + 1e-9)
    weights = np.exp(-((x_norm - 0.5) ** 2) / (2 * 0.2 ** 2))
    weights = 0.5 + 0.5 * weights

    W = np.diag(weights)

    if degree == 1:
        X_mat = np.column_stack((np.ones(len(x)), x))
    elif degree == 2:
        X_mat = np.column_stack((np.ones(len(x)), x, x ** 2))
    else: return None, None

    # Формула: theta = (X^T * W * X)^-1 * X^T * W * Y
    Xt = X_mat.T
    Xt_W_X = Xt @ W @ X_mat
    Xt_W_Y = Xt @ W @ y

    try:
        theta = np.linalg.inv(Xt_W_X) @ Xt_W_Y
        return theta, weights
    except np.linalg.LinAlgError:
        return None, weights


def calculate_mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def get_predicted_y(x, theta, degree):
    if degree == 1:
        b, k = theta
        return k * x + b
    elif degree == 2:
        c, b, a = theta
        return a * x ** 2 + b * x + c
    else: return None


def plot_results(name, data, results):
    x_clean, y_clean = data['clean']
    x_matrix, y_matrix = data['matrix']
    x_total, y_total = data['total']
    l_type = data['type']
    true_params = data['params']

    plt.figure(figsize=(12, 8))

    plt.scatter(x_matrix, y_matrix, color='gray', alpha=0.5, label='Шум (только Y)', s=20, edgecolors='none')
    plt.scatter(x_total, y_total, color='lightgray', alpha=0.3, label='Шум (X и Y)', s=20, marker='x')

    if l_type == 'linear':
        k_true, b_true = true_params
        y_true_line = k_true * x_clean + b_true
        label_true = f"Истинная: y={k_true}x + {b_true}"
    else:
        a_true, b_true, c_true = true_params
        y_true_line = a_true * x_clean ** 2 + b_true * x_clean + c_true
        label_true = f"Истинная: y={a_true}x² + {b_true}x + {c_true}"

    plt.plot(x_clean, y_true_line, 'k-', linewidth=2.5, label=label_true, zorder=10)
    styles_config = {
        'matrix': {'color': 'b', 'linestyle': '--', 'label_prefix': 'Матричный'},
        'total': {'color': 'r', 'linestyle': '-.', 'label_prefix': 'Полный'},
        'weighted': {'color': 'g', 'linestyle': ':', 'label_prefix': 'Взвешенный'}
    }

    for method_key, res_data in results.items():
        if method_key not in styles_config:
            continue

        cfg = styles_config[method_key]
        mse = res_data['mse']

        if method_key == 'total':
            k_pred, b_pred = res_data['params']
            y_pred = k_pred * x_clean + b_pred
        else:
            theta = res_data['theta']
            if l_type == 'linear':
                b_pred, k_pred = theta
                y_pred = k_pred * x_clean + b_pred
            else:
                c_pred, b_pred, a_pred = theta
                y_pred = a_pred * x_clean ** 2 + b_pred * x_clean + c_pred

        label = f"{cfg['label_prefix']} МНК (MSE={mse:.4f})"

        fmt_string = f"{cfg['color']}{cfg['linestyle']}"

        plt.plot(x_clean, y_pred, fmt_string, linewidth=2, label=label)

    plt.title(f"Сравнение методов МНК: {name}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def main():
    print("Генерация данных...")
    datasets = generate_data(n_points=100, noise_level=0.15)

    report = []

    for name, data in datasets.items():
        print(f"\n--- Обработка: {name} ---")
        l_type = data['type']
        x_matrix, y_matrix = data['matrix']
        x_total, y_total = data['total']
        x_clean, y_clean = data['clean']

        results = {}

        # 1. Матричный МНК (используем данные с шумом только в Y)
        theta_matrix = matrix_mnk(x_matrix, y_matrix, degree=1 if l_type == 'linear' else 2)
        y_pred_matrix = get_predicted_y(x_clean, theta_matrix, 1 if l_type == 'linear' else 2)
        mse_matrix = calculate_mse(y_clean, y_pred_matrix)
        results['matrix'] = {'theta': theta_matrix, 'mse': mse_matrix}
        print(f"Матричный МНК: Параметры={theta_matrix}, MSE={mse_matrix:.6f}")

        # 2. Полный МНК (используем данные с шумом в X и Y)
        if l_type == 'linear':
            k_tls, b_tls = total_mnk(x_total, y_total)
            if k_tls is not None:
                y_pred_tls = k_tls * x_clean + b_tls
                mse_tls = calculate_mse(y_clean, y_pred_tls)
                results['total'] = {'params': (k_tls, b_tls), 'mse': mse_tls}
                print(f"Полный МНК:    Параметры=k={k_tls:.4f}, b={b_tls:.4f}, MSE={mse_tls:.6f}")

        # 3. Взвешенный МНК (используем данные с шумом только в Y)
        theta_weighted, _ = weighted_mnk(x_matrix, y_matrix, degree=1 if l_type == 'linear' else 2)
        if theta_weighted is not None:
            y_pred_weighted = get_predicted_y(x_clean, theta_weighted, 1 if l_type == 'linear' else 2)
            mse_weighted = calculate_mse(y_clean, y_pred_weighted)
            results['weighted'] = {'theta': theta_weighted, 'mse': mse_weighted}
            print(f"Взвешенный МНК: Параметры={theta_weighted}, MSE={mse_weighted:.6f}")

        report.append({
            'name': name,
            'matrix_mse': mse_matrix,
            'total_mse': results.get('total', {}).get('mse', None),
            'weighted_mse': mse_weighted
        })

        plot_results(name, data, results)

main()
