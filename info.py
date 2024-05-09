import requests
import matplotlib.pyplot as plt
import datetime
import numpy as np
from scipy.interpolate import interp1d
import plotly.graph_objects as go




def get_thingspeak_data():
    url = 'https://api.thingspeak.com/channels/2491759/feeds.json?api_key=YPJFT7C1KL4AV1QQ&results=10000000000000'
    response = requests.get(url)
    data = response.json()
    return data



def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


def plot_thingspeak_temperature():
    data = get_thingspeak_data()

    timestamps = []
    values = []

    for entry in data['feeds']:
        try:
            timestamp = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(
                hours=3)
            value = float(entry['field1'])
            timestamps.append(timestamp)
            values.append(value)
        except:
            continue

    # Определяем интервал времени для последних 8 часов
    last_8_hours = datetime.datetime.now() - datetime.timedelta(hours=8)

    # Фильтруем данные за последние 8 часов
    filtered_timestamps = [t for t in timestamps if t >= last_8_hours]
    filtered_values = [v for i, v in enumerate(values) if timestamps[i] >= last_8_hours]

    # Применяем скользящее среднее к данным
    window_size = 6  # Размер окна для скользящего среднего
    smoothed_values = moving_average(filtered_values, window_size)

    # Создаем объект фигуры Plotly
    fig = go.Figure()

    # Добавляем линию к графику
    fig.add_trace(
        go.Scatter(x=filtered_timestamps[window_size - 1:], y=smoothed_values, mode='lines', name='Температура'))

    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Температура', range=[0, 30]))

    # Настраиваем метки осей
    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Температура'))

    fig.add_hline(y=22, line_dash="dash", line_color="red", annotation_text=" ",
                  annotation_position="bottom right")
    fig.add_hline(y=18, line_dash="dash", line_color="red", annotation_text=" ",
                  annotation_position="bottom right")

    # Сохраняем график как изображение JPEG
    fig.write_image("temperature_plot.jpg", format="jpeg", width=800, height=600)

    # Отображаем график


def plot_thingspeak_humidity():
    data = get_thingspeak_data()

    timestamps = []
    values = []

    for entry in data['feeds']:
        try:
            timestamp = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(
                hours=3)
            value = float(entry['field2'])
            timestamps.append(timestamp)
            values.append(value)
        except:
            continue

    # Определяем интервал времени для последних 8 часов
    last_8_hours = datetime.datetime.now() - datetime.timedelta(hours=8)

    # Фильтруем данные за последние 8 часов
    filtered_timestamps = [t for t in timestamps if t >= last_8_hours]
    filtered_values = [v for i, v in enumerate(values) if timestamps[i] >= last_8_hours]

    # Применяем скользящее среднее к данным
    window_size = 6  # Размер окна для скользящего среднего
    smoothed_values = moving_average(filtered_values, window_size)

    # Создаем объект фигуры Plotly
    fig = go.Figure()

    # Добавляем линию к графику
    fig.add_trace(
        go.Scatter(x=filtered_timestamps[window_size - 1:], y=smoothed_values, mode='lines', name='Влажность'))

    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Влажность', range=[0, 100]))

    # Настраиваем метки осей
    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Влажность'))

    fig.add_hline(y=40, line_dash="dash", line_color="red", annotation_text=" ",
                  annotation_position="bottom right")
    fig.add_hline(y=60, line_dash="dash", line_color="red", annotation_text=" ",
                  annotation_position="bottom right")

    # Сохраняем график как изображение JPEG
    fig.write_image("humidity_plot.jpg", format="jpeg", width=800, height=600)



def plot_thingspeak_light():
    data = get_thingspeak_data()

    timestamps = []
    values = []

    for entry in data['feeds']:
        try:
            timestamp = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=3)
            value = float(entry['field4'])
            timestamps.append(timestamp)
            values.append(value)
        except:
            continue

    # Определяем интервал времени для последних 8 часов
    last_8_hours = datetime.datetime.now() - datetime.timedelta(hours=8)

    # Фильтруем данные за последние 8 часов
    filtered_timestamps = [t for t in timestamps if t >= last_8_hours]
    filtered_values = [v for i, v in enumerate(values) if timestamps[i] >= last_8_hours]

    # Применяем скользящее среднее к данным
    window_size = 6  # Размер окна для скользящего среднего
    smoothed_values = moving_average(filtered_values, window_size)

    # Создаем объект фигуры Plotly
    fig = go.Figure()

    # Добавляем линию к графику
    fig.add_trace(
        go.Scatter(x=filtered_timestamps[window_size - 1:], y=smoothed_values, mode='lines', name='Освещенность'))

    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Освещенность', range=[0, 100]))

    # Настраиваем метки осей
    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Освещенность'))

    fig.add_hline(y=5, line_dash="dash", line_color="red", annotation_text=" ",
                  annotation_position="bottom right")
    # Сохраняем график как изображение JPEG
    fig.write_image("light_plot.jpg", format="jpeg", width=800, height=600)



def plot_thingspeak_noise():
    data = get_thingspeak_data()

    timestamps = []
    values = []

    for entry in data['feeds']:
        try:
            timestamp = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(
                hours=3)
            value = float(entry['field5'])
            timestamps.append(timestamp)
            values.append(value)
        except:
            continue

    # Определяем интервал времени для последних 8 часов
    last_8_hours = datetime.datetime.now() - datetime.timedelta(hours=8)

    # Фильтруем данные за последние 8 часов
    filtered_timestamps = [t for t in timestamps if t >= last_8_hours]
    filtered_values = [v for i, v in enumerate(values) if timestamps[i] >= last_8_hours]

    # Применяем скользящее среднее к данным
    window_size = 6  # Размер окна для скользящего среднего
    smoothed_values = moving_average(filtered_values, window_size)

    # Создаем объект фигуры Plotly
    fig = go.Figure()

    # Добавляем линию к графику
    fig.add_trace(
        go.Scatter(x=filtered_timestamps[window_size - 1:], y=smoothed_values, mode='lines', name='Уровень шума'))

    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Уровень шума', range=[200, 10000
                                                                                         ]))


    # Настраиваем метки осей
    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Уровень шума'))


    # Сохраняем график как изображение JPEG
    fig.write_image("noise_plot.jpg", format="jpeg", width=800, height=600)


def plot_thingspeak_gases():
    data = get_thingspeak_data()

    timestamps = []
    values = []

    for entry in data['feeds']:
        try:
            timestamp = datetime.datetime.strptime(entry['created_at'], "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(
                hours=3)
            value = float(entry['field6'])
            timestamps.append(timestamp)
            values.append(value)
        except:
            continue

    # Определяем интервал времени для последних 8 часов
    last_8_hours = datetime.datetime.now() - datetime.timedelta(hours=8)

    # Фильтруем данные за последние 8 часов
    filtered_timestamps = [t for t in timestamps if t >= last_8_hours]
    filtered_values = [v for i, v in enumerate(values) if timestamps[i] >= last_8_hours]

    # Применяем скользящее среднее к данным
    window_size = 6  # Размер окна для скользящего среднего
    smoothed_values = moving_average(filtered_values, window_size)

    # Создаем объект фигуры Plotly
    fig = go.Figure()

    # Добавляем линию к графику
    fig.add_trace(
        go.Scatter(x=filtered_timestamps[window_size - 1:], y=smoothed_values, mode='lines', name='Уровень шума'))

    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Уровень шума', range=[0, 10000]))

    # Настраиваем метки осей
    fig.update_layout(xaxis=dict(title='Время'), yaxis=dict(title='Уровень шума'))



    # Сохраняем график как изображение JPEG
    fig.write_image("gases_plot.jpg", format="jpeg", width=800, height=600)






