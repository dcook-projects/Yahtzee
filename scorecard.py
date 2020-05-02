class Scorecard:

    def __init__(self):
        self.scores = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "3k": None,
            "4k": None,
            "fh": None,
            "ss": None,
            "ls": None,
            "yahtzee": None,
            "yb": None,
            "chance": None
        }

    def __str__(self):
        score_string = ""
        for key, value in self.scores.items():
            score_string += "{} = {}\n".format(key, value)

        return score_string

    def print_scorecard(self):
        print(self, flush=True)

    def is_category_valid(self, name, player_dice):
        category = name.lower()
        if category not in self.scores:
            return False

        if category == "yb":
            if self.scores["yahtzee"] != 50:
                return False

            if not player_dice.is_valid_yahtzee():
                return False

        if self.scores[category] is not None:
            return False

        return True

    @staticmethod
    def print_registration_message(category):
        if category == "3k":
            print("Three of a kind registered")
        elif category == "4k":
            print("Four of a kind registered")
        elif category == "fh":
            print("Full house registered")
        elif category == "ss":
            print("Small straight registered")
        elif category == "ls":
            print("Large straight registered")
        else:
            print("{} registered".format(category))

        print(flush=True)

    def update_scorecard(self, category, value):
        # Need to check yahtzee bonus separately since it is the only category that can be used multiple times
        if category == "yb":
            if self.scores[category] is None:
                self.scores[category] = 100
            else:
                self.scores[category] += 100

            print("Yahtzee bonus registered", flush=True)
        else:
            self.scores[category] = value
            self.print_registration_message(category)

    def calculate_final_total(self):
        for key, value in self.scores.items():
            if value is None:
                self.scores[key] = 0

        upper_total = self.scores["ones"] + self.scores["twos"] + self.scores["threes"] + self.scores["fours"] + \
            self.scores["fives"] + self.scores["sixes"]

        if upper_total >= 63:
            upper_total += 35

        lower_total = self.scores["3k"] + self.scores["4k"] + self.scores["fh"] + self.scores["ss"] + self.scores["ls"] + \
            self.scores["yahtzee"] + self.scores["chance"] + self.scores["yb"]

        grand_total = upper_total + lower_total

        self.print_scorecard()
        print("Your upper total score is: {}".format(upper_total))
        print("Your lower total score is: {}".format(lower_total))
        print("Your grand total is: {}".format(grand_total))
