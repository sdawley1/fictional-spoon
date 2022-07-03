# fictional-spoon

Inputs to perform a Scholar's Mate: 
1. e4 e5
2. Qh5 Nc6
3. Bc4 Nf6
4. Qxf7

Inputs to perform a Fool's Mate:
1. f3 e6
2. g4 Qh4

## Dependencies
* [python-chess](https://python-chess.readthedocs.io/en/latest/index.html)
* [stockfish](https://github.com/zhelyabuzhsky/stockfish)

## Stockfish Engine
* [Stockfish](https://github.com/official-stockfish/Stockfish)

## Installing stockfish
### For Mac
1. Go here: [stockfish download](https://stockfishchess.org/download/)
  - For Mac users, follow the link at the bottom of the page under to `Linux > See all Linux Binaries`. I've installed the BMI2 version, though, choose whichever version suits your machine.
2. Installing one of these binaries will download a zip file to your computer. Unzip it and navigate to `/stockfish_15_linux_x64_bmi2/stockfish_15_src/src/` within the terminal/command prompt. This is where the engine itself is to be compiled.
3. Within the same directory, run the commands
  - `$ make net`
  - `$ make build ARCH=x86-64`
to compile the engine.
4. Ta-da! You've installed Stockfish to your machine!

### For Windows
Your life sadly isn't quite as easy as the Mac user's. You'll have to follow the instructions [here](https://github.com/ppigazzini/fishtest/wiki/Building-stockfish-on-Windows) to build the application. I recommend installing MSYS2 and then building Stockfish with GCC. Use the executable in \stockfish_15_win_x64_avx2/stockfish_x86-64-bmi2.exe. This is what I ended up with on my computer, but I'm sure you can specify further in the bash script that you copy from the Github linked above.
