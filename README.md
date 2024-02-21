# Tetris

![cover of the tetris game](/imgs/cover.png)

This is a tetris game made with pygame module in Python. The game aims to kill boredom and help relieve stress. This is a portfolio project done as the last project in ALX software engineering course foundation phase. This project came to be because of my love for games and it was also inspired by an X user [John Crickett](https://twitter.com/johncrickett), a software engineer who puts up coding challenges weekly for software engineers to use in gaining more experience coding. This game utilises the power of Object Oriented Programming(OOP) in order to make each blocks or tetraminoes have unique attributes and behavior. Also, cx_Freeze was used in other to make an executable of the game, this way even those who are not programmers can easily get it and have fun with it. Believe it or not I struggled with choosing the right colors for the blocks, I still don't feel the current colors are a good fit. Another area of struggle currently, is creating a game menu so that users can choose difficulty level, toggle game sound, and get their high score displayed after exiting the game. These are some features to look out for in upcoming releases.

## Installation

If you'd like to install or use this code for your own learning sake, you can clone or fork the repo.
This project was done on a windows operating system using visual studio code as the code editor
Make sure pygame module is installed on your system, run `pip install pygame` in your terminal. This will install the pygame module.
After cloning or forking the repo, if you'd like to run the program:
`python -u "c:\Users\HP\name_of_folder_cloned_to\Tetris\src\main.py"`.
If you're using a code editor like visual studio codes, you can just hit the run button and it'll be done automatically for you.
Once you get the feel on how it works, if you like, for developers, you can tweak it to your liking.
If you'd like to create your own executable after tweaking to your liking, you can use this command in the folder where everything is cloned to
`python src\setup.py bidst_msi`.
This would create an msi executable that can be installed by anyone.
If you'd just like to create the executable for your use only, then run:
`python src\setup.py build`.

On a recent development, an executable has been made for this game, though it'll only work on windows, so if you'd like to download the executable without compiling the full code, you download the build file and double click on main.
Currently cx_Freeze only compiles per operating system, so if you're a mac or linux user, you'd have to get the full code, compile and build it using the setup.py with little adjustment.

### Installing using the executable

- From the Github, click on the **dist** folder
- Click on **Tetris-win64.msi**
  ![screenshot of github showing where the dist folder is](/imgs/git1.png)
- Click on view raw or the download icon to download the raw file
  ![screenshot of the msi file to click on](/imgs/git2.png)
- Wait for download to complete
  ![screenshot of download in progress](/imgs/git3.png)

- Go to the folder where the raw file has been downloaded and double click on the file
  ![screenshot of file explorer showing downloaded msi file](/imgs/setup1.png)
- A setup window appears asking where you'd like to install the game, choose your desired folder and click next.
  ![screenshot of setup window for installing of executable](/imgs/setup2.png)
- After installation, click on finish.
- Locate the directory the installation was done on
  ![screenshot of directory installation was done on](/imgs/setup3.png)
- Look for main and double click it, the game window will open up, now you enjoy
  ![screenshot of the tetris game after successful execution](/imgs/tetris.png)

## How to play

It's a simple game of tetris that carries the usual tetris rule, only that some weird or unfamiliar blocks were added to make it fun and challenging. All you have to do is stack your tetraminoes or blocks, and try to clear as much lines as possible. Clearing more than one line at once increases your score.
Use the left &#8592; arrow key to move the tetramino left, the right &#8594; arrow key to move the tetramino right, the down &#8595; to drop the tetramino, and the up &#8593; arrow key to rotate the block.
Try your best to hang in there and not fill up the tiles to the top in order to avoid **_Game Over_**.
To continue or restart the game after getting **_Game Over_**, hit the Enter/Return key &#x23CE;. The game can be paused and unpaused using the spacebar

![Screenshot of the tetris game showing the user interface](/imgs/tetris.png)

![Screenshot of the tetris game when the blocks or tetraminoes get to the top of the grid](/imgs/gameover.png)

## Releases

[version 0](/dist/Tetris-win64.msi)
[version 0.2](/dist/Tetris-0.2-win64.msi)

## Colloborators

Keme-ebi Remember Bolou - email `kelvin6bolou@gmail.com` - X [@keme_bolou](https://twitter.com/@keme_bolou) - linkedin [Keme-ebi Remember Bolou](https://www.linkedin.com/in/keme-ebi)
