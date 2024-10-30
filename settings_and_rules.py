dict_board = {"1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9
              }


def update_board(spots):
    print(f"|{dict_board["1"]}|{dict_board["2"]}|{dict_board["3"]}|\n"
          f"|{dict_board["4"]}|{dict_board["5"]}|{dict_board["6"]}|\n"
          f"|{dict_board["7"]}|{dict_board["8"]}|{dict_board["9"]}|\n")


def check_who_wins(spots):
    if ((dict_board["1"] == dict_board["2"]) and (dict_board["1"] == dict_board["3"]) or
            (dict_board["1"] == dict_board["4"]) and (dict_board["1"] == dict_board["7"]) or
            (dict_board["1"] == dict_board["5"]) and (dict_board["1"] == dict_board["9"]) or
            (dict_board["2"] == dict_board["5"]) and (dict_board["2"] == dict_board["8"]) or
            (dict_board["3"] == dict_board["1"]) and (dict_board["3"] == dict_board["2"]) or
            (dict_board["3"] == dict_board["5"]) and (dict_board["3"] == dict_board["7"]) or
            (dict_board["3"] == dict_board["6"]) and (dict_board["3"] == dict_board["9"]) or
            (dict_board["4"] == dict_board["5"]) and (dict_board["4"] == dict_board["6"]) or
            (dict_board["4"] == dict_board["1"]) and (dict_board["4"] == dict_board["7"]) or
            (dict_board["5"] == dict_board["1"]) and (dict_board["5"] == dict_board["9"]) or
            (dict_board["5"] == dict_board["3"]) and (dict_board["5"] == dict_board["7"]) or
            (dict_board["5"] == dict_board["4"]) and (dict_board["5"] == dict_board["6"]) or
            (dict_board["5"] == dict_board["2"]) and (dict_board["5"] == dict_board["8"]) or
            (dict_board["6"] == dict_board["3"]) and (dict_board["6"] == dict_board["9"]) or
            (dict_board["6"] == dict_board["4"]) and (dict_board["6"] == dict_board["5"]) or
            (dict_board["7"] == dict_board["1"]) and (dict_board["7"] == dict_board["4"]) or
            (dict_board["7"] == dict_board["8"]) and (dict_board["7"] == dict_board["9"]) or
            (dict_board["7"] == dict_board["5"]) and (dict_board["7"] == dict_board["3"]) or
            (dict_board["8"] == dict_board["7"]) and (dict_board["8"] == dict_board["9"]) or
            (dict_board["8"] == dict_board["5"]) and (dict_board["8"] == dict_board["2"]) or
            (dict_board["9"] == dict_board["7"]) and (dict_board["9"] == dict_board["8"]) or
            (dict_board["9"] == dict_board["1"]) and (dict_board["9"] == dict_board["5"]) or
            (dict_board["9"] == dict_board["3"]) and (dict_board["9"] == dict_board["6"])):
        return True

    else:
        return False
