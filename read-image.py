# Importa o módulo cv2
import cv2

# Leia a imagem
img = cv2.imread("butterfly.jpg")

# Exiba a imagem colorida
cv2.imshow("Imagem de Exibicao", img)

# Converta a imagem colorida para escala de cinza
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Exiba a imagem em escala de cinza
cv2.imshow("Escala de Cinza", gray_img)

# "printa" os pixels em array 2D
print(gray_img)

# Faz a janela esperar por um tempo indeterminado
cv2.waitKey(0)