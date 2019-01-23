import gamelib

class Mark1Bot(gamelib.AlgoCore):
    def on_game_start(self, config):
        self.config = config
        global FILTER, ENCRYPTOR, DESTRUCTOR, PING, EMP, SCRAMBLER, UNIT_TO_ID
        FILTER, ENCRYPTOR, DESTRUCTOR, PING, EMP, SCRAMBLER, UNIT_TO_ID = [config['unitInformation'][idx]["shorthand"] for idx in range(6)]

    def on_turn(self, turn_state):
        game_state = gamelib.GameState(self.config, turn_state)
        # maybe set to True later
        game_state.enable_warnings = False

        self.defense(game_state)
        self.attack(game_state)

        game_state.submit_turn()

    def build_defenses(self, location_list, firewall_unit, game_state, row=None):
        for location in location_list:
            if not type(location) == list:
                location = [location, row]

            if game_state.can_spawn(firewall_unit, location):
                game_state.attempt_spawn(firewall_unit, location)
                gamelib.debug_write(f"{firewall_unit} deployed at {location}")
                game_state._player_resources[0]['cores'] -= game_state.type_cost(firewall_unit)
            elif not game_state.contains_stationary_unit(location):
                return False
        
        return True


    def defense(self, game_state):
        # placing filters
        filters = [[0, 13], [27, 13], [1, 12], [26, 12]]
        if not self.build_defenses(filters, FILTER, game_state):
            return
        
        row = 11
        destructors = [2, 25, 6, 21, 11, 16]

        if not self.build_defenses(destructors, DESTRUCTOR, game_state, row=row):
            return

        filters = [3, 24, 4, 23, 5, 22, 7, 20, 8, 19, 9, 18, 10, 17, 12, 15]

        if not self.build_defenses(filter, FILTER, game_state):
            return


    def attack(self, game_state):


if __name__ == "__main__":
    algo = Mark1Bot()
    algo.start()
