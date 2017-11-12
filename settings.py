class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        self.bullet_speed_factor = 10
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20

        self.alien_speed_factor = 2
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
