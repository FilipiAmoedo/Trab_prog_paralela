import pandas as pd
import multiprocessing as mp
import time
import matplotlib.pyplot as plt
from datetime import datetime

def read_csv():
    df = pd.read_excel('cdi.xlsx')
    return df

# if __name__ == '__main__':
#     print(read_csv())


def is_valid_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def valid_date_min_max(start_date: str, end_date: str):
    data_min = '2000-01-03'
    data_max = '2024-02-29'
    if not (is_valid_date_format(start_date) and is_valid_date_format(end_date)):
        raise ValueError("As datas devem estar no formato yyyy-mm-dd")
    if not (data_min <= start_date <= data_max) or not (data_min <= end_date <= data_max):
        raise ValueError(f"As datas devem estar entre {data_min} e {data_max}")
    if start_date > end_date:
        raise ValueError("A data de início deve ser anterior ou igual à data de fim")


def cdi_acumulado(start_date: str, end_date: str) -> pd.Series:
    df = read_csv()
    valid_date_min_max(start_date, end_date)
    df = df.loc[(df['data'] >= start_date) & (df['data'] <= end_date)]
    df.loc[0, 'retorno'] = 0
    df['cdi_acumulado'] = ((1 + df['retorno']).cumprod() - 1) * 100
    df['cdi_acumulado'] = df['cdi_acumulado'].round(2)
    df.set_index('data', inplace=True)
    df.drop(columns='retorno', inplace=True)
    return df


# if __name__ == '__main__':
#     start_date = '2020-01-02'
#     end_date = '2024-02-29'
#     print(cdi_acumulado(start_date, end_date))


def cdi_anual(start_date: str, end_date: str) -> pd.Series:
    df = read_csv()
    valid_date_min_max(start_date, end_date)
    df = df.loc[(df['data'] >= start_date) & (df['data'] <= end_date)]
    df['cdi_anual'] = (((1 + df['retorno']) ** 252) - 1) * 100
    df['cdi_anual'] = df['cdi_anual'].round(2)
    df.set_index('data', inplace=True)
    df.drop(columns='retorno', inplace=True)
    return df

# if __name__ == '__main__':
#     start_date = '2020-01-02'
#     end_date = '2024-02-29'
#     print(cdi_anual(start_date, end_date))


def media_selic(start_date: str, end_date: str) -> pd.Series:
    valid_date_min_max(start_date, end_date)
    df = cdi_anual(start_date, end_date)
    df.index = pd.to_datetime(df.index)
    df['year'] = df.index.year
    df.set_index('year', inplace=True)
    media_anual = df.groupby('year').mean().round(2)
    return media_anual


# if __name__ == '__main__':
#     start_date = '2020-01-02'
#     end_date = '2024-02-29'
#     print(media_selic(start_date, end_date))


def parallel_process(function, start_date: str, end_date: str):
    pool = mp.Pool(mp.cpu_count())
    result = pool.apply_async(function, args=(start_date, end_date))
    pool.close()
    pool.join()
    return result.get()


def measure_time_sequential(functions, start_date, end_date):
    start_time = time.time()
    results = [func(start_date, end_date) for func in functions]
    end_time = time.time()
    return results, end_time - start_time


def measure_time_parallel(functions, start_date, end_date):
    start_time = time.time()
    with mp.Pool(mp.cpu_count()) as pool:
        results = [pool.apply_async(func, args=(start_date, end_date)) for func in functions]
        results = [res.get() for res in results]
    end_time = time.time()
    return results, end_time - start_time


if __name__ == '__main__':
    start_date = '2000-01-03'
    end_date = '2024-02-29'

    functions = [cdi_acumulado, cdi_anual, media_selic]

    seq_results, seq_time = measure_time_sequential(functions, start_date, end_date)
    print(f"Tempo de execução sequencial total: {seq_time:.4f} segundos")
    # for i, result in enumerate(seq_results):
    #     print(f"Resultado da função {i + 1}:\n{result}")

    par_results, par_time = measure_time_parallel(functions, start_date, end_date)
    print(f"\nTempo de execução paralelo total: {par_time:.4f} segundos")
    # for i, result in enumerate(par_results):
    #     print(f"Resultado da função {i + 1}:\n{result}")

    # performance_data = {
    #     'Execução': ['Sequencial', 'Paralelo'],
    #     'Tempo (s)': [seq_time, par_time]
    # }
    #
    # df_performance = pd.DataFrame(performance_data)
    # df_performance.plot(kind='bar', x='Execução', y='Tempo (s)', legend=False, rot=0)
    # plt.ylabel('Tempo (segundos)')
    # plt.title('Comparação de Desempenho')
    # plt.show()