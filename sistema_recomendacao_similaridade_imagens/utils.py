
"""
Este script define a função para extração de features de uma imagem.
A função será utilizada pelos notebooks de extração de features e consulta de imagem.
A conversão de uma imagem em um vetor de features serve para criar um espaço vetorial que nos
permita medir a distância entre dois pontos de dados. Desta forma, quando temos uma imagem,
podemos representá-la como um ponto no espaço vetorial criado e medir sua distância para os
demais pontos do espaço. A distância entre dois pontos é inversamente proporcional à
similaridade das imagens correspondentes.
Com isto, podemos calcular quais as n imagens mais similares à imagem consultada e retornar
tais imagens como sugestão ao usuário.
"""
import numpy as np

from keras.applications.vgg16 import preprocess_input, VGG16
from keras.utils import img_to_array, load_img

# As imagens usadas como base devem estar na mesma pasta, para facilitar o processo de treino
img_folder = 'train_images'
# Para extração de features das imagens, podemos utilizar vários métodos de vetorização.
# Neste exemplo, utilizaremos a rede neural VGG16 pretreinada com os pesos da imagenet.
# A rede VGG16 está inclusa nas aplicações do Keras e é utilizada para classificação de imagens.
# Porém, se excluírmos as camadas do topo da rede, responsáveis pela classificação, a saída da
# rede será um tensor com 512 features para cada imagem amostrada.
vgg_model = VGG16(include_top=False)


def img_features_extract(img_path, **kwargs):
    # A camada de entrada da rede VGG16 assume que as imagens são do tamanho 224x224.
    # Assim, ao carregarmos uma imagem para a rede, fazemos o redimensionamento adequado.
    img = load_img((img_path), target_size=(224, 224))
    # Precisamos converter a imagem em um tensor (244,244,3), para o processamento matemático
    img = img_to_array(img)
    # A entrada da rede neural recebe um tensor com n amostras, sendo do formato (n,224,224,3)
    # Assim, cada amostra de imagem deverá ser passada como um tensor de dimensão (1,224,224,3)
    # Utilizamos a função expand_dims do numpy para criar o eixo extra no início do tensor.
    img = np.expand_dims(img, axis=0)
    # Utilizamos a rede VGG16 para transformar cada imagem em um vetor de features
    features = vgg_model.predict(preprocess_input(img), **kwargs)
    return features[0,0,0,:]



