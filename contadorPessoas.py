import cv2

# Carrega o classificador Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializa a captura de vídeo da câmera
video = cv2.VideoCapture(1)  # 0 para câmera padrão, 1 para câmera externa

contador = 0
liberado = False

while True:
    ret, img = video.read()
    img = cv2.resize(img, (1100, 720))  # Redimensiona a imagem conforme necessário
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta faces na imagem usando o classificador Haar Cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    num_cabecas = len(faces)

    cv2.putText(img, f'Cabeças: {num_cabecas}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('video original', img)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

