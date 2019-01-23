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
        

    def defense(self, game_state):

    def attack(self, game_state):


if __name__ == "__main__":
    algo = Mark1Bot()
    algo.start()
