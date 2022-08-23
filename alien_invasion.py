""" Tools in sys module will help when player quits """
import sys

""" PyGame contains functionality we need to make the game. """
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	""" Overall class to manage game assets and behavior. """

	def __init__(self):
		""" Initialize the game, and create game resources. """
		pygame.init()
		self.settings = Settings()
		
		# screen is a surface on which things can be displayed 
		# this surface will be redrawn at any loop of the while 
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))

		# This will make the game go full screen.
		"""
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		"""


		pygame.display.set_caption("Alien Invasion - hit Q to quit")

		self.ship = Ship(self)

		# Set the background color.
		self.bg_color = (self.settings.bg_color)

	def run_game(self):
		""" Start the main loop for the game. """
		while True:
			""" 
			the 2 methods below are what it looks like to call a method from inside a class
			these are called helper methods
			"""
			self._check_events() 
			self._update_screen()
			self.ship.update()


	def _check_events(self):
		# Respond to keypresses and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
				

	def _check_keydown_events(self, event):
		# Respond to keypresses
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# Move the ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		# Respond to keypresses and mouse events
		if event.key == pygame.K_RIGHT:
			# Stop moving the ship to the right
			self.ship.moving_right = False	
		elif event.key == pygame.K_LEFT:
			# Stop moving the ship to the left
			self.ship.moving_left = False

	def _update_screen(self):
		# Update images on screen, and flip to the new screen	
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		# Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	# Make a game instance and run the game.
	ai = AlienInvasion()
	ai.run_game()