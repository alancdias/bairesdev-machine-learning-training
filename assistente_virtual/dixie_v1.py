# Requirements:
# pip install SpeechRecognition
# pip install pyaudio
# pip install gTTS
# pip install playsound3

#Importações
import speech_recognition as sr #biblioteca para converter fala em texto
import webbrowser #biblioteca para abrir páginas da web
from datetime import datetime #biblioteca de data/hora
from gtts import gTTS #biblioteca para converter texto em fala
from playsound3 import playsound #biblioteca para reproduzir arquivos mp3



def speak(msg):
    """Converte um texto para áudio e o reproduz

    Args:
        msg (str): texto a ser convertido em áudio
    """
    print(msg)
    tts = gTTS(msg, lang='pt', tld='com.br')
    tts.save('msg.mp3')
    playsound('msg.mp3')

    

print('Tudo certo com as importações')
r = sr.Recognizer() #cria instância de reconhecedor de fala
with sr.Microphone(device_index=1) as mic: # abre o microfone para entrada de áudio
    print('Pode falar...')
    r.adjust_for_ambient_noise(mic, duration=0.8) #Tira um tempo para se habituar ao ruído ambiente
    audio = r.listen(mic, timeout=6) #grava o áudio recebido pelo microfone
try:
    text = r.recognize_google(audio, language='pt-BR').lower() #transforma o áudio em texto

    print(f'Google acha que você falou "{text}"') #exibe o texto reconhecido
    if text: #se houver texto reconhecido:
        # Pesquisa de termo na internet:
        if 'pesquisa' in text: #se a palavra 'pesquisa' foi falada:
            query = text[text.index('pesquisa')+len('pesquisa'):] #encontra o termo a ser pesquisado
            msg = f'Pesquisando {query}'
            speak(msg)
            # Abrir pesquisa sobre o termo no Navegador
            webbrowser.open("https://www.google.com/search?q=" + query)

        # Exibição de data e hora
        if 'horas' in text: #se a palavra horas foi falada:
            # Exibe hora e data atuais
            msg = f'Agora são {datetime.strftime(datetime.now(), "%X")} de {datetime.strftime(datetime.now(), "%d/%m/%Y")}'
            speak(msg)
            
        # Adição de item em lista de compras
        if 'coloca' in text and 'lista de compra' in text: #se as palavras 'coloca' e 'lista de compra' fora faladas:
            item = text[text.index('coloca')+7:text.index('na lista')].strip() #item a ser incluso na lista
            with open('lista_compras.txt', 'a') as file: #abre o arquivo da lista de compras
                file.write(item+'\n') #adiciona o item à lista
            msg = f'{item} adicionado à lista de compras.'
            speak(msg) #informa da inclusão

        # Adição de item em lista de tarefas
        if 'coloca' in text and 'lista de tarefa' in text: #se as palavras 'coloca' e 'lista de tarefa' fora faladas:
            item = text[text.index('coloca')+7:text.index('na lista')].strip() #item a ser incluso na lista
            with open('lista_tarefas.txt', 'a') as file: #abre o arquivo da lista de tarefas
                file.write(item+'\n') #adiciona o item à lista
            msg = f'{item} adicionado à lista de tarefas.'
            speak(msg) #informa a inclusão
except sr.UnknownValueError: # se o texto do áudio não foi reconhecido:
    print('Não entendi o que foi dito')
except Exception as exc: # se outra exceção ocorreu:
    print('Algo deu errado.', type(exc), exc)
