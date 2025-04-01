# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:00:25 2024

@author: jfrui
"""

import numpy as np
from PIL import Image

def leer_imagen(ruta_imagen):
    """
    Lee una imagen a partir de una ruta y retorna el objeto imagen usando PIL.
    
    Parámetros:
    ruta_imagen (str): Ruta de la imagen a leer.
    
    Retorna:
    img: objeto tipo Image de PIL
    """
    try:
        img = Image.open(ruta_imagen).convert("RGB")  # Asegura que la imagen sea RGB
        return img
    except Exception as e:
        print(f"Error al leer la imagen: {e}")
        return None

def obtener_info_imagen(img):
    """
    Recibe una imagen y retorna el número de canales y las dimensiones.
    
    Parámetros:
    img: objeto tipo Image de PIL
    
    Retorna:
    tuple: (num_canales, dimensiones)
    """
    if img is None:
        return None, None
    
    modo = img.mode
    num_canales = {'L': 1, 'RGB': 3, 'RGBA': 4}.get(modo, len(modo))
    dimensiones = img.size  # (ancho, alto)
    
    return num_canales, dimensiones

def imagen_a_arreglo(img):
    """
    Convierte una imagen PIL a un arreglo NumPy.
    
    Parámetros:
    img (PIL.Image): Imagen a convertir.
    
    Retorna:
    np.ndarray: Arreglo de NumPy con los datos de la imagen.
    """
    if img is None:
        return None
    return np.array(img)

def estadisticas_intensidad(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles.
    
    Parámetros:
    arreglo_img (np.ndarray): Imagen representada como arreglo de NumPy.
    
    Retorna:
    tuple: (promedio, desviación_estándar)
    """
    if arreglo_img is None:
        return None, None
    return arreglo_img.mean(), arreglo_img.std()

def estadisticas_por_canal(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles por canal.
    
    Parámetros:
    arreglo_img (np.ndarray): Imagen representada como arreglo de NumPy.
    
    Retorna:
    dict: Diccionario con el promedio y la desviación estándar por canal.
    """
    if arreglo_img is None:
        return None
    
    if len(arreglo_img.shape) == 2:  # Imagen en escala de grises
        return {
            'Canal_1': {
                'Promedio': np.mean(arreglo_img),
                'Desviación Estándar': np.std(arreglo_img)
            }
        }
    
    num_canales = arreglo_img.shape[2]
    resultados = {}
    
    for canal in range(num_canales):
        resultados[f'Canal_{canal+1}'] = {
            'Promedio': np.mean(arreglo_img[:, :, canal]),
            'Desviación Estándar': np.std(arreglo_img[:, :, canal])
        }
    
    return resultados