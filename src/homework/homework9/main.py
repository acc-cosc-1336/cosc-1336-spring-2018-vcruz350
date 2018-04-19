#write import statements for Player and Die class
from src.homework.homework9.die import Die
from src.homework.homework9.player import Player

#Create an instance of the Main class and call/execute the roll_doubles method
class Main:
    
    def start(self):
        player = Player()
        player.roll_doubles()

main = Main()
main.start()
