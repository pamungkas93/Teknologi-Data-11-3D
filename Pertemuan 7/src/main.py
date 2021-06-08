# from window.kalkulatorgui import KalkulatorGUI
from window.penampildiagram import PenampilDiagram
# from window.hellogui import HelloGUI

class Main:
    @staticmethod
    def main():
        # main_window = KalkulatorGUI()
        main_window = PenampilDiagram()
        # main_window = HelloGUI()

        main_window.show()


Main.main()