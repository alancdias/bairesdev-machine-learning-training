## 💻 Desafio de Projeto: Criação de Uma Base de Dados e Treinamento da Rede YOLO
<p>Este desafio faz parte do Bootcamp "BairesDev - Machine Learning Training", da DIO.
<p>O desafio consiste coletar e rotular imagens e, com base nestas, personalizar a rede YOLO para detectar e classificar um conjunto de classes nas imagens.
<p>A rede YOLO é uma rede neural de código aberto que utiliza Deep Learning para detectar e classificar classes em imagens. Neste projeto foi utilizada a rede YOLOV7, cujo funcionamento o estrutura podem ser vistos <a href="https://github.com/WongKinYiu/yolov7/blob/main/paper/yolov7.pdf">neste artigo</a> e a implementação pode ser vista no <a href="https://github.com/WongKinYiu/yolov7">github</a>.
<p>Para base de dados, foram coletadas imagens de peças de xadrez, rotuladas com as seguintes classes:


  - torre
  - cavalo
  - bispo
  - rainha
  - rei
  - peão

<p>A anotação das imagens foi feita com a ferramenta mlabelImg e as imagens foram divididas em dois conjuntos, sendo um de treino e um de validação. Um terceiro conjunto de imagens não rotuladas foi utilizado para teste.
<p>

### 💡 Habilidades e Recursos Utilizados


- ![](https://img.shields.io/badge/python-170888?logo=python&labelColor=170888)
- ![](https://img.shields.io/badge/yolov7-detecção_e_classificação_de_imagens-blue?logo=yolo&labelColor=170888)
- ![](https://img.shields.io/badge/pytorch-treinamento_de_redes_em_gpu-blue?logo=pytorch&labelColor=170888)


