from controller import *


def main():
    """
    Function to run main program
    :return: main program
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
