class GameStats:
	""" Track statistics for Alien Invasion """

	def __init__(self, ai_game):
		""" Initialize statistics """
		self.settings = ai_game.settings
		self.reset_stats()
		# Start Alien Invasion in an active state.

		# Start game in an inactive state
		self.game_active = False
		
		# High score should never be reset
		self.high_score = 0
		with open('high_score_file.txt') as file_object:
			self.previous_high_score = file_object.read()
			self.previous_high_score = int(self.previous_high_score)
			self.high_score = self.previous_high_score

	def reset_stats(self):
		""" Initialize statistics than can change during the game """
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level= 1
