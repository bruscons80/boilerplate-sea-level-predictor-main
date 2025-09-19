import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Ler os dados do .csv
    df = pd.read_csv('epa-sea-level.csv')

    # Cria o Grafico
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Cria primeira linha de melhor ajuste
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    line = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, line, color='red', label='Best Fit Line (All Data)')

    # Cria segunda linha de melhor ajuste (desde 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = np.arange(2000, 2051)
    line_recent = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, line_recent, color='green', label='Best Fit Line (Since 2000)')

    # Adiciona as labels e titulo
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Salva o grafico e retorna a data para testes
    plt.savefig('sea_level_plot.png')
    return plt.gca()


    draw_plot()
