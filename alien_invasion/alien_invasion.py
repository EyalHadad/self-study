import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import  Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #make the ship
    ship = Ship(screen, ai_settings)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    bullets = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings,screen,stats)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets,stats,play_button,aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, ship, screen,stats,sb)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)
        gf.update_screen(ai_settings, screen,ship,bullets, aliens, play_button, stats, sb)




if __name__ == '__main__':
    print ("Module name:")
    print (pygame.__name__)
    run_game()
