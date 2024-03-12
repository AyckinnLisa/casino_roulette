# - GAME FUNCTIONS -

import os, pathlib
import colortx as ctx


def last_numbers(list, rollnb):
    if len(list) >= 10:
        list.clear()
        list.append(rollnb)
    else:
        list.append(rollnb)

    return list


def player_money(total, bet, usernb, list, rollnb):
    os.system('clear')
    print("", ("-" * 60))
    print(f"              ARGENT : {ctx.green(total)}€")
    print(f"       DERNIERE MISE : {ctx.magenta(bet)}€")
    print(f"      DERNIER NUMERO : {ctx.blue(usernb)}")
    
    if not list:  # - If list not empty -
        print(f"   DERNIERES SORTIES : {ctx.yellow("*")}")
    else:
        print(f"   DERNIERES SORTIES : {ctx.yellow(list)}")
    print("", ("-" * 60))


def game_folder_path():
    return pathlib.Path(__file__).parent.absolute()


def money_folder():
    return str(game_folder_path()) + "/money"


def money_file(uname):
    return str(game_folder_path()) + "/money/" + uname


def this_is_not_a_number():
    print(ctx.red(" Ceci n'est pas un nombre... "))


def save_money(pname, money):
    if not os.path.exists(money_folder()):
        os.mkdir(money_folder())
        
    with open(money_file(pname), 'w') as mf:
        mf.write(str(money))
    print(f"\n Montant sauvegardé : {ctx.green(money)}€.")

