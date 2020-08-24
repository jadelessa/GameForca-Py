# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):		#cria a instancia da classe -> tem uma palavra do banco e duas listas (uma de letras ok  e uma de letras erradas)
									#estas listas serao preenchidas durante o jogo
		self.word = word
		self.lista_letras_error=[]
		self.lista_letras_ok=[]
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word and letter not in self.lista_letras_ok:
			self.lista_letras_ok.append(letter)
		elif letter not in self.word and letter not in self.lista_letras_error:
			self.lista_letras_error.append(letter)
		else:
			return False
		return True

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.lista_letras_error) == 6)

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '_' not in self.hide_word():
			print("Parabens!! Vc venceu!!\n")
			return True
		else:

			return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		palavra = ''
		for letter in self.word:
			if letter not in self.lista_letras_ok:
				palavra += '_'
			else:
				palavra += letter
		return palavra
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (board[len(self.lista_letras_error)])
		print ("\nPalavra: ",self.hide_word())
		print("\nLetras erradas: ",)
		for letter in self.lista_letras_error:
			print(letter,)
		print()
		print("Letras corretas: ",)
		for letter in self.lista_letras_ok:
			print(letter,)
		print()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word()) #cria objeto game que é uma instancia da classe Hangman e passa por parametro uma palavra
								#escolhida de forma aleatoria no arquivo txt

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()	# Verifica o status do jogo

		game.guess(input('\nDigite uma letra: '))

	game.print_game_status()

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
