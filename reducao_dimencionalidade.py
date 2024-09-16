from PIL import Image
import matplotlib.pyplot as plt

def rgb_to_grayscale(image):
    # Converte uma imagem RGB para escala de cinza
    grayscale_image = []
    for y in range(image.height):
        grayscale_row = []
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            grayscale_row.append(gray)
        grayscale_image.append(grayscale_row)
    return grayscale_image

def grayscale_to_binary(image, threshold=128):
    # Converte uma imagem em tons de cinza para uma imagem binária
    binary_image = []
    for row in image:
        binary_row = []
        for gray in row:
            binary_value = 255 if gray > threshold else 0
            binary_row.append(binary_value)
        binary_image.append(binary_row)
    return binary_image

def display_image(image, title):
    # Exibe uma imagem 2D usando matplotlib
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')  # Desativa os eixos
    plt.show()

# Caminho da imagem JPG
jpg_filename = "Rosto.jpg"

# Carrega a imagem JPG
image = Image.open(jpg_filename)

# Converte a imagem RGB para tons de cinza
grayscale_image = rgb_to_grayscale(image)

# Converte a imagem em tons de cinza para binária
binary_image = grayscale_to_binary(grayscale_image)

# Exibe as duas imagens
display_image(grayscale_image, "Imagem em Tons de Cinza")
display_image(binary_image, "Imagem Binarizada")