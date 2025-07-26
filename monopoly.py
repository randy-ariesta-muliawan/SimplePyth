
class Settings:
	
	def __init__(self):
		#game_settings
		self.title = 'Monopoly All You Can Do ... and Take Profit'

		#board_settings
		self.board_len = 800
		self.board_hei = 600

class Board:

	def __init__(self, settings):
		self.settings = settings
		self.length = self.settings.board_len
		self.height = self.settings.board_hei

class Player:

	def __init__(self):
		pass

class Monopoly:

	def __init__(self, number_players=3):
		self.settings = Settings()
		self.title = self.settings.title
		
		self.board = Board(self.settings)
		self.number_players = number_players

		self.players = []
		self.build_players(self.number_players)

	def build_players(self, number_players):
		for i in range(number_players):
			player = Player() 
			self.players.append(player)

my_game = Monopoly()
print(my_game.board.length)