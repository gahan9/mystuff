class Game(object):
    def __init__(self, string):
        self.string = string
        self.string_length = len(self.string)
        self.vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    def count_score(self):
        stuart, kevin = 0, 0
        for i in range(self.string_length):
            if s[i] in self.vowels:
                kevin += self.string_length - i
            else:
                stuart += self.string_length - i
        return stuart, kevin


def minion_game(string):
    # your code goes here
    game_instance = Game(string)
    stuart, kevin = game_instance.count_score()
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
