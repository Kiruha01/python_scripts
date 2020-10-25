from cx_Freeze import setup, Executable

setup(
    name = "Ud",
    version = "0.1",
    description = "Blackjack",
    executables = [Executable("main.py")]
)