#!usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================
# =   CASINO ROULETTE                                  =
# =      - Version   : 1.0                             =
# =      - Author    : Ayckinn                         =
# =      - Mail      : ayckinn@pm.me                   =
# =      - Release   : March 11' 2024                  =
# =      - Github    : https://github.com/AyckinnLisa  =
# =      - Copyright : ©2020-2024                      =
# ======================================================

import os, time, random

import colortx as ctx
import gamefuncs as gf


def main():
    user_bet = 0
    user_nb = 0
    roll_list = []
    roll = ""    

    try:
        print(ctx.green(''' 
 # ==================================== #
 # =          CASINO ROULETTE         = #
 # =               v1.0               = #
 # =       ©2020-2024 - @Ayckinn      = #
 # =           ayckinn@pm.me          = #
 # =  https://github.com/AyckinnLisa  = #
 # ==================================== #\n'''))
        player = input(" Quel est ton nom ? ")

        if os.path.exists(gf.money_file(player)):
            print(f"\n Contente de te revoir {ctx.magenta(player.title())} ! ^^")
            time.sleep(2)

            with open(gf.money_file(player), 'r') as mf:
                money_data = mf.readlines()
                print(f" Tu reprends la partie avec : {ctx.green(money_data[0].strip())}€")
                time.sleep(2)
                user_money = int(money_data[0])
                gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
        else:                
            print(f"\n Bonjour {ctx.blue(player.title())}", end = "")
            print(f". Je suis {ctx.red("Lisa")}.")
            print(f"\n Bienvenue dans le jeu \"{ctx.magenta("CASINO ROULETTE")}\"")
            time.sleep(3)

            print(f'''
 ----------------------------------------------------------------------------
    Règle du jeu :     
      - Je vais te demander de choisir un numéro entre 0 et 36. 
      - Tu vas miser et je vais lancer la boule.
      - Si tu trouves le numéro de la boule, tu gagnes 36 fois ta mise...
      - Sinon, tu la perds.
                  
      Pour ta première partie, je t'offre {ctx.green(1000)}€  ^^
 ----------------------------------------------------------------------------\n
 {ctx.red("/!\\")}  Pour quitter le jeu, appuies sur {ctx.red("CTRL+C  /!\\")}.\n''')

            input(f" Appuies sur {ctx.red("Entree")} quand tu es prêt(e)... ")
            user_money = 1000
            print(f"\n Très bien ! Je charge la roulette... {ctx.yellow("BON JEU")} !!")
            time.sleep(3)
        
        # - Game loop -
        while True:
            gf.player_money(user_money, user_bet, user_nb, roll_list, roll)

            while user_money >= 0:
                try:
                    user_bet = int(input("\n Choisis ta mise : "))

                    if user_bet == 0:
                        print(ctx.red("\n ERREUR ! La mise minimum est de 1€"))
                        time.sleep(3)
                        gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
                        break
                    elif user_bet > user_money:
                        print(ctx.red("\n ERREUR ! Tu n'as pas assez d'argent."))
                        user_bet = 0
                        time.sleep(3)
                        gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
                        break
                    else:
                        user_money = (user_money - user_bet)
                        gf.player_money(user_money, user_bet, user_nb, roll_list, roll)

                except ValueError:
                    print(ctx.red("\n ERREUR ! Mise invalide..."))
                    time.sleep(3)
                    gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
                    break

                # - Loop : player choose a number -
                while True: 
                    try:
                        roll = random.randrange(37)
                        user_nb = int(input("\n Choisis un numéro entre 0 et 36 : "))

                        if user_nb > 36:
                            print(ctx.red("\n ERREUR ! Le numéro ne doit pas dépasser 36."))
                            time.sleep(3)
                            user_nb = 0
                            gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
                        else:
                            break
                    except ValueError:
                        print(ctx.red("\n ERREUR ! Choix invalide..."))
                        time.sleep(3)
                        gf.player_money(user_money, user_bet, user_nb, roll_list, roll)

                if user_nb <= 36:
                    print(ctx.red("\n LES JEUX SONT FAITS.... RIEN NE VA PLUS !\n"))
                    time.sleep(3)
                    print(f" La boule s'est arrêtée sur le : {ctx.yellow(roll)}")
                    time.sleep(2)

                    if user_nb == roll:
                        user_profit = (user_bet * 36)
                        user_money = (user_money + user_profit)
                        print(ctx.green(f"\n BRAVO {player} !"), f"Tu gagnes {ctx.yellow(user_profit)}€")
                        time.sleep(3)
                        gf.last_numbers(roll_list, roll)
                        gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
                    else:
                        print(ctx.red(f"\n DESOLE ! Tu as perdu {user_bet}€ ..."))
                        time.sleep(3)
                        gf.last_numbers(roll_list, roll)
                        gf.player_money(user_money, user_bet, user_nb, roll_list, roll)
                   
                if user_money == 0:
                    if os.path.exists(gf.money_file(player)):
                        os.remove(gf.money_file(player))
                        # - If folder is empty, remove it -
                        if len(os.listdir(gf.money_folder())) == 0:
                            os.rmdir(gf.money_folder())

                    print(ctx.red(f"\n Désolée {ctx.magenta(player)}"), end = "")
                    print(ctx.red(", tu n\'as plus d\'argent..."))
                    time.sleep(2)
                    print("\n LA PARTIE EST FINIE... A BIENTOT :) ...\n")
                    exit()

    except KeyboardInterrupt:
        print(ctx.red("\n\n Game Over !"))
        gf.save_money(player, user_money)


if __name__ == "__main__":
    os.system('clear')
    main()

# ====================================================================== #
# = - Si c'est difficile à expliquer, alors c'est une mauvaise idée  - = #
# = - If it's hard to explain, it's a bad idea                       - = #
# ====================================================================== #
    