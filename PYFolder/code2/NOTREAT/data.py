from datetime import datetime
import pytz

# Definindo o fuso horário para BRT (Brasília)
brt = pytz.timezone('Brazil/East')

# Lista de datas fornecidas
datas = [
    "10 de set. de 2024, 04:00:00 BRT",
    "11 de set. de 2024, 04:00:00 BRT",
    "12 de set. de 2024, 04:00:00 BRT",
    "13 de set. de 2024, 04:00:00 BRT",
    "14 de set. de 2024, 04:00:00 BRT",
    "15 de set. de 2024, 04:00:00 BRT",
    "16 de set. de 2024, 04:00:00 BRT",
    "17 de set. de 2024, 04:00:00 BRT",
    "18 de set. de 2024, 04:00:00 BRT",
    "19 de set. de 2024, 04:00:00 BRT",
    "20 de set. de 2024, 04:00:00 BRT",
    "21 de set. de 2024, 04:00:00 BRT",
    "22 de set. de 2024, 04:00:00 BRT",
    "23 de set. de 2024, 04:00:00 BRT",
    "24 de set. de 2024, 04:00:00 BRT",
    "25 de set. de 2024, 04:00:00 BRT",
    "26 de set. de 2024, 04:00:00 BRT",
    "27 de set. de 2024, 04:00:00 BRT",
    "28 de set. de 2024, 04:00:00 BRT",
    "29 de set. de 2024, 04:00:00 BRT",
    "30 de set. de 2024, 04:00:00 BRT",
    "1 de out. de 2024, 04:00:00 BRT",
    "2 de out. de 2024, 04:00:00 BRT",
    "3 de out. de 2024, 04:00:00 BRT",
    "4 de out. de 2024, 04:00:00 BRT",
    "5 de out. de 2024, 04:00:00 BRT",
    "6 de out. de 2024, 04:00:00 BRT",
    "7 de out. de 2024, 04:00:00 BRT",
    "8 de out. de 2024, 04:00:00 BRT",
    "9 de out. de 2024, 04:00:00 BRT",
    "10 de out. de 2024, 04:00:00 BRT",
    "11 de out. de 2024, 04:00:00 BRT",
    "12 de out. de 2024, 04:00:00 BRT",
    "13 de out. de 2024, 04:00:00 BRT",
    "14 de out. de 2024, 04:00:00 BRT",
    "15 de out. de 2024, 04:00:00 BRT",
    "16 de out. de 2024, 04:00:00 BRT",
    "17 de out. de 2024, 04:00:00 BRT",
    "18 de out. de 2024, 04:00:00 BRT",
    "19 de out. de 2024, 04:00:00 BRT",
    "20 de out. de 2024, 04:00:00 BRT",
    "21 de out. de 2024, 04:00:00 BRT",
    "22 de out. de 2024, 04:00:00 BRT",
    "23 de out. de 2024, 04:00:00 BRT",
    "24 de out. de 2024, 04:00:00 BRT",
    "25 de out. de 2024, 04:00:00 BRT",
    "26 de out. de 2024, 04:00:00 BRT",
    "27 de out. de 2024, 04:00:00 BRT",
    "28 de out. de 2024, 04:00:00 BRT",
    "29 de out. de 2024, 04:00:00 BRT",
    "30 de out. de 2024, 04:00:00 BRT",
    "31 de out. de 2024, 04:00:00 BRT",
    "1 de nov. de 2024, 04:00:00 BRT",
    "2 de nov. de 2024, 04:00:00 BRT",
    "3 de nov. de 2024, 04:00:00 BRT",
    "4 de nov. de 2024, 05:00:00 BRT",
    "5 de nov. de 2024, 05:00:00 BRT",
    "6 de nov. de 2024, 05:00:00 BRT",
    "7 de nov. de 2024, 05:00:00 BRT",
    "8 de nov. de 2024, 05:00:00 BRT",
    "9 de nov. de 2024, 05:00:00 BRT",
    "10 de nov. de 2024, 05:00:00 BRT",
    "11 de nov. de 2024, 05:00:00 BRT",
    "12 de nov. de 2024, 05:00:00 BRT",
    "13 de nov. de 2024, 05:00:00 BRT",
    "14 de nov. de 2024, 05:00:00 BRT",
    "15 de nov. de 2024, 05:00:00 BRT",
    "16 de nov. de 2024, 05:00:00 BRT",
    "17 de nov. de 2024, 05:00:00 BRT",
    "18 de nov. de 2024, 05:00:00 BRT",
    "19 de nov. de 2024, 05:00:00 BRT",
    "20 de nov. de 2024, 05:00:00 BRT",
    "21 de nov. de 2024, 05:00:00 BRT",
    "22 de nov. de 2024, 05:00:00 BRT",
    "23 de nov. de 2024, 05:00:00 BRT",
    "24 de nov. de 2024, 05:00:00 BRT",
    "25 de nov. de 2024, 05:00:00 BRT",
    "26 de nov. de 2024, 05:00:00 BRT",
    "27 de nov. de 2024, 05:00:00 BRT",
    "28 de nov. de 2024, 05:00:00 BRT",
    "29 de nov. de 2024, 05:00:00 BRT",
    "30 de nov. de 2024, 05:00:00 BRT",
    "1 de dez. de 2024, 05:00:00 BRT",
    "2 de dez. de 2024, 05:00:00 BRT",
    "3 de dez. de 2024, 05:00:00 BRT",
    "4 de dez. de 2024, 05:00:00 BRT",
    "5 de dez. de 2024, 05:00:00 BRT",
    "6 de dez. de 2024, 05:00:00 BRT",
    "7 de dez. de 2024, 05:00:00 BRT",
    "8 de dez. de 2024, 05:00:00 BRT",
    "9 de dez. de 2024, 05:00:00 BRT",
    "10 de dez. de 2024, 05:00:00 BRT",
    "11 de dez. de 2024, 05:00:00 BRT",
    "12 de dez. de 2024, 05:00:00 BRT",
    "13 de dez. de 2024, 05:00:00 BRT",
    "14 de dez. de 2024, 05:00:00 BRT",
    "15 de dez. de 2024, 05:00:00 BRT",
    "16 de dez. de 2024, 05:00:00 BRT",
    "17 de dez. de 2024, 05:00:00 BRT",
    "18 de dez. de 2024, 05:00:00 BRT",
    "19 de dez. de 2024, 05:00:00 BRT",
    "20 de dez. de 2024, 05:00:00 BRT",
    "21 de dez. de 2024, 05:00:00 BRT",
    "22 de dez. de 2024, 05:00:00 BRT",
    "23 de dez. de 2024, 05:00:00 BRT",
    "24 de dez. de 2024, 05:00:00 BRT",
    "25 de dez. de 2024, 05:00:00 BRT",
    "26 de dez. de 2024, 05:00:00 BRT",
    "27 de dez. de 2024, 05:00:00 BRT",
    "28 de dez. de 2024, 05:00:00 BRT",
    "29 de dez. de 2024, 05:00:00 BRT",
    "30 de dez. de 2024, 05:00:00 BRT",
    "31 de dez. de 2024, 05:00:00 BRT",
    "1 de jan. de 2025, 05:00:00 BRT",
    "2 de jan. de 2025, 05:00:00 BRT",
    "3 de jan. de 2025, 05:00:00 BRT",
    "4 de jan. de 2025, 05:00:00 BRT",
    "5 de jan. de 2025, 05:00:00 BRT",
    "6 de jan. de 2025, 05:00:00 BRT",
    "7 de jan. de 2025, 05:00:00 BRT",
    "8 de jan. de 2025, 05:00:00 BRT",
    "9 de jan. de 2025, 05:00:00 BRT"
]

# Corrigindo o formato para aceitar o ponto no mês
for data in datas:
    # Remover o ponto após a abreviação do mês
    data_corrigida = data.replace(" set.", " set")  # Substitua "set." por "set"
    
    try:
        # Convertendo a data para datetime
        data_obj = datetime.strptime(data_corrigida, "%d de %b de %Y, %H:%M:%S BRT")
        data_obj = brt.localize(data_obj)  # Localizando a data no fuso horário BRT
        print(data_obj)
    except ValueError as e:
        print(f"Erro ao processar a data: {data} -> {e}")