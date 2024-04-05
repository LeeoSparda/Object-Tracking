import cv2
import sys
from random import randint

# Lista dos tipos de trackers disponíveis no OpenCV
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

# Escolha do tipo de tracker a ser utilizado (neste caso, MIL)
tracker_type = tracker_types[6]

# Criação do tracker específico baseado no tipo selecionado
if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
elif tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()
elif tracker_type == 'CSRT':
    tracker = cv2.TrackerCSRT_create()

# Inicialização da captura de vídeo da webcam
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('D:/Desktop/CG/Atividade5/race.mp4')
# video = cv2.imwrite("D:/Desktop/CG/Atividade5/teste.png")
if not video.isOpened():
    print('Erro ao carregar a webcam!')
    sys.exit()

# Leitura do primeiro quadro da webcam
ok, frame = video.read()
if not ok:
    print('Erro ao carregar o quadro!')
    sys.exit()

# Seleção da região de interesse (ROI) na webcam
bbox = cv2.selectROI(frame)  # Retorna as coordenadas da região selecionada (x, y, largura, altura)
print(bbox)

# Inicialização do tracker com a região de interesse selecionada
ok = tracker.init(frame, bbox)
print(ok)

# Geração de uma cor aleatória para desenhar o retângulo de rastreamento
colors = (randint(0, 255), randint(0,255), randint(0, 255))  # RGB -> BGR

# Loop principal para capturar e rastrear os quadros da webcam
while True:
    # Captura de um novo quadro da webcam
    ok, frame = video.read()
    if not ok:
        break

    # Atualização do tracker para rastrear a região de interesse no novo quadro
    ok, bbox = tracker.update(frame)
    if ok:
        # Se o rastreamento for bem-sucedido, desenha um retângulo na região rastreada
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors, 2)
    else:
        # Se o rastreamento falhar, exibe uma mensagem de falha
        cv2.putText(frame, 'Falha no rastreamento!', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255))

    # Exibe o tipo de tracker sendo utilizado no canto superior esquerdo do quadro
    cv2.putText(frame, tracker_type, (100, 20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255))

    # Exibe o quadro atual com o retângulo de rastreamento
    cv2.imshow('Rastreamento', frame)
    
    # Aguarda a tecla 'Esc' ser pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == 27:  # Tecla Esc
        break

# Libera os recursos da captura de vídeo e fecha todas as janelas
# video.release()
# cv2.destroyAllWindows()
