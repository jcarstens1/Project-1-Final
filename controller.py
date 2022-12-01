from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


def calculate(food: float, drink: float, dessert: float, tip: list) -> tuple:
    """
    Function to compute the total amount of the bill
    :param food: Food total
    :param drink: Drink total
    :param dessert: Dessert Total
    :param tip: Tip Total
    :return: grand total, total tip, total tax
    """
    tax = 0.1
    total_tax = (food + drink + dessert) * tax
    if 'percent' in tip[0]:
        total_tip = (food + drink + dessert + total_tax) * tip[1]
    else:
        total_tip = tip[1]
    grand_total = food + drink + dessert + total_tax + total_tip
    return total_tax, total_tip, grand_total


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class to represent app logic
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor to add methods to buttons on application
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.Submit_Button.clicked.connect(lambda: self.submit())
        self.Clear_Button.clicked.connect(lambda: self.clear())
        self.Radio_Custom.clicked.connect(lambda: self.custom_switch())
        self.Radio_10.clicked.connect(lambda: self.custom_switch())
        self.Radio_15.clicked.connect(lambda: self.custom_switch())
        self.Radio_20.clicked.connect(lambda: self.custom_switch())
        self.Split_Checkbox.clicked.connect(lambda: self.split_switch())

    def split_switch(self) -> None:
        """
        Method to turn split check input on and off
        :return: none
        """
        if self.Split_Checkbox.isChecked() is True:
            self.Split_Entry.setReadOnly(False)
            self.Split_Entry.setValue(2)
            self.Split_Entry.setMinimum(2)
        else:
            self.Split_Entry.setMinimum(1)
            self.Split_Entry.setValue(1)
            self.Split_Entry.setReadOnly(True)

    def custom_switch(self) -> None:
        """
        Method to turn custom tip input on and off
        :return: none
        """
        if self.Radio_Custom.isChecked() is True:
            self.Custom_Entry.setReadOnly(False)
        else:
            self.Custom_Entry.setReadOnly(True)
            self.Custom_Entry.setText('')

    def clear(self) -> None:
        """
        Method to clear input and place app into default status
        :return: none
        """
        self.Food_Entry.setText('')
        self.Drink_Entry.setText('')
        self.Dessert_Entry.setText('')
        self.Radio_10.click()
        self.Summary_Label.setText('')
        self.Custom_Entry.setText('')
        self.Split_Entry.setMinimum(1)
        self.Split_Entry.setValue(1)
        self.Custom_Entry.setReadOnly(True)
        self.Split_Checkbox.setChecked(False)
        self.Split_Entry.setReadOnly(True)

    def submit(self) -> None:
        """
        Method to display billing details
        :return: bill details
        """
        try:
            food = float(self.Food_Entry.text())
            drink = float(self.Drink_Entry.text())
            dessert = float(self.Dessert_Entry.text())
            if self.Radio_10.isChecked():
                tip = ['percent', .1]
            elif self.Radio_15.isChecked():
                tip = ['percent', .15]
            elif self.Radio_20.isChecked():
                tip = ['percent', .2]
            elif self.Radio_Custom.isChecked():
                tip = ['amount', float(self.Custom_Entry.text())]
            else:
                tip = 0
            total_tax, total_tip, grand_total = calculate(food, drink, dessert, tip)
            if self.Split_Checkbox.isChecked():
                individual_amount = grand_total / self.Split_Entry.value()
                self.Summary_Label.setText(
                    f'{" " * 25}SUMMARY\n\nFood:\t\t${food:.2f}\nDrink:\t\t${drink:.2f}\nDessert:\t\t${dessert:.2f}\nTax:\t\t${total_tax:.2f}\nTip:\t\t${total_tip:.2f}\n\nTOTAL:\t\t${grand_total:.2f}\nPer  Person:\t${individual_amount:.2f}')
            else:
                self.Summary_Label.setText(
                    f'{" " * 25}SUMMARY\n\nFood:\t\t${food:.2f}\nDrink:\t\t${drink:.2f}\nDessert:\t\t${dessert:.2f}\nTax:\t\t${total_tax:.2f}\nTip:\t\t${total_tip:.2f}\n\nTOTAL:\t\t${grand_total:.2f}')
        except ValueError:
            self.Summary_Label.setText(
                f'\n\n\n{" " * 15}Food drink, and dessert\n{" " * 15}need to be numeric\n{" " * 15}e.g. 10.25 not $10.25')
