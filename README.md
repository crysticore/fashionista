# NAO + CNN FashionMNIST Classifier

## 1. Objetivo
Este proyecto integra visión por computadora con un robot NAO. El objetivo es que NAO pueda identificar prendas de vestir usando una cámara, enviar la imagen a una computadora vía sockets TCP, y decir en voz alta lo que ha reconocido gracias a un modelo CNN entrenado con FashionMNIST.

## 2. Arquitectura
```
[NAO Robot] --TCP--> [PC Cliente]
    |                     |
 [Cámara]            [Modelo CNN PyTorch (FashionMNIST)]
    |                     |
[Sintetizador de voz] <-- Predicción traducida
```

## 3. Instrucciones de uso

### Requisitos
- Python 3.x
- torch
- torchvision
- pillow

```bash
pip install torch torchvision pillow
```

### Entrenamiento del modelo
```python
# train_fashion_cnn.py
# (incluye entrenamiento, validación, métricas y guardado del modelo CNN)
```

### Código cliente (PC)
```python
# client_predictor.py
# - Espera imagen vía socket
# - Procesa con CNN entrenado
# - Devuelve predicción al NAO
```

### Código servidor (NAO)
```python
# nao_server.py
# - Captura imagen
# - Envía por socket TCP
# - Recibe predicción
# - Usa text-to-speech para decir resultado
```

### Cómo ejecutar
1. Asegúrate de haber entrenado y guardado el modelo como `fashionista.pth`.
2. Ejecuta en la PC:
```bash
python3 client_predictor.py
```
3. Ejecuta en el NAO (vía SSH o desde su entorno con Python 2.7):
```bash
python2.7 nao_server.py
```

## 4. Ejemplo de resultado
> El robot dice: "Lo que veo es zapatilla" (con acento gringo)

## 5. Resultados del modelo

Accuracy en test: **91.12%**

### Classification Report
```
              precision    recall  f1-score   support

 T-shirt/top     0.8421    0.8850    0.8630      1000
     Trouser     0.9939    0.9770    0.9854      1000
    Pullover     0.8086    0.9040    0.8536      1000
       Dress     0.9066    0.9220    0.9142      1000
        Coat     0.8855    0.8040    0.8428      1000
      Sandal     0.9909    0.9760    0.9834      1000
       Shirt     0.7855    0.7140    0.7480      1000
     Sneaker     0.9389    0.9840    0.9609      1000
         Bag     0.9763    0.9880    0.9821      1000
  Ankle boot     0.9835    0.9530    0.9680      1000

    accuracy                         0.9107     10000
```

## 6. Créditos
Proyecto desarrollado por **Daniella Vargas** para el curso de Machine Learning. Integración hardware-software con robot NAO, visión por computadora y deep learning en PyTorch.
