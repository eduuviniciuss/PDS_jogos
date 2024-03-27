def jogar():
    print("***")
    print("Bem vindo Eduardo")
    print("***")
    
    palavra_secreta = "eduardo".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas2 = []
    
    for letra in (palavra_secreta):
        letras_acertadas2.append("_")
        
    
        enforcou = False
        acertou = False
        erros = 0
        
        print(letras_acertadas)
        
        while (not enforcou and not acertou):
            chute = input("qual letra? ")
            chute = chute.strip().upper()
            
        if (chute in palavra_secrets):
                index = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas[index] = letra 
                    else:
                        erros += 1
                        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if (acertou):
        print ("voce ganhou!!")
    else:
        print("voce perdeu!!")
    print("fim de jogo")
    
    
if (__name__== "__main__"):
    jogar()
            
    
                
                
        
        
        
        
        
        