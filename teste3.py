import cv2

def main():
    # Inicialize a captura de vídeo a partir da webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Exiba o frame capturado
        cv2.imshow('Webcam', frame)

        # Aguarde por uma tecla pressionada
        key = cv2.waitKey(1)

        # Se a tecla 'b' for pressionada, salve a imagem e saia do loop
        if key == ord('b'):
            cv2.imwrite('D:/Desktop/CG/Atividade5/teste.png', frame)
            break

    # Libere a captura de vídeo e feche todas as janelas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
