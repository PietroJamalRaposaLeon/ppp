import os
import shutil

pasta_inicial = r'C:\Users\pietr\OneDrive\Área de Trabalho\AulasPython\PRO_1-4_C111_AtividadeDaProfessora2-main\downloads'
pasta_final = r'C:\Users\pietr\OneDrive\Área de Trabalho\AulasPython\PRO_1-4_C111_AtividadeDaProfessora2-main\images'
 

lista_de_arquivos = os.listdir(pasta_inicial)
print(lista_de_arquivos)

for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(arquivo)
    #print(extensao)

    if extensao == '':
        continue
    if extensao in['.png','.jpg', '.jfif']:
        pasta1 = pasta_inicial + '/' + arquivo
        pasta2 = pasta_final + '/' + arquivo

        print("Movendo " + arquivo + '...')
        shutil.move(pasta1, pasta2) 

    if extensao in ['.gif']:
        pasta3 = 'Gifs'
        pasta1 = pasta_inicial + '/' + arquivo

        if os.path.exists(pasta3):
            print("Movendo " + arquivo + '...')
            shutil.move(pasta1, pasta3)                    
        
        else:
            os.makedirs(pasta3)
            print("movendo " + arquivo+ 'para' + '...')
            shutil.move(pasta1,pasta3)
