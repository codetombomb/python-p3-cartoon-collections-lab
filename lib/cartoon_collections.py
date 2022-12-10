def roll_call_dwarves(list):
    for idx, d in enumerate(list):
        print(f"{idx + 1}. {d}")

def summon_captain_planet(list):
    return [f"{name.capitalize()}!" for name in list]

def long_planeteer_calls(list):
    for word in list:
        if len(word) > 4:
            return True
    return False

def find_the_cheese(list):
    cheeses = ["cheddar", "gouda","camembert"]
    for cheese in list:
        if cheese in cheeses:
            return cheese

