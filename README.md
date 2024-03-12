# Casino Roulette
Rules : 
- For the first game, AI offers 1000€ to a the player
- Player have to bet and choose a number between 0 and 36
- AI launches the wheel
- If player's number = wheel number, player wins 36 times his stake else he losts it
- When player's money = 0, the game is over

---

## Screenshot
<div align="center">
    <img
        src="https://github.com/AyckinnLisa/PYTHON/blob/main/Games/casino_roulette/screenshot.png"
        alt="DEMO"
        style="width:40%">
</div>

---

## Usage
1. Download [Python](https://www.python.org/downloads/).
2. Open the terminal for Unix or CMD for Windows
3. Go to the game folder : ```cd /game_folder_path```
4. Run the game : ```python3 main.py```
5. To quit the game : CTRL+C

---

## Changelog
Version 1.0 - March 11' 2024
- Save money for each player in a file
    - If player's money = 0, AI removes the player's file
    - If money folder is empty, AI removes the folder
- Initial release
