import re


class Game(object):
    def __init__(self, string):
        self.string = string
        self.vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    def get_all_substrings(self):
        length = len(self.string)
        return set([self.string[i:j + 1] for i in range(length) for j in range(i, length)])

    def count_substring(self, sub_string):
        match = re.findall('(?=' + sub_string + ')', self.string)
        return len(match)

    def count_score(self):
        sub_strings = self.get_all_substrings()
        score_dict = {}
        for sub_str in sub_strings:
            score = self.count_substring(sub_str)
            if sub_str.startswith(self.vowels):
                score_dict['Kevin'] = score_dict.setdefault('Kevin', 0) + score
            else:
                score_dict['Stuart'] = score_dict.setdefault('Stuart', 0) + score
        return score_dict


def minion_game(string):
    # your code goes here
    game_instance = Game(string)
    scores = game_instance.count_score()
    max_ = max(scores, key=lambda x: scores[x])
    print("{} {}".format(max_, scores[max_]))


if __name__ == '__main__':
    s = input()
    minion_game(s)
