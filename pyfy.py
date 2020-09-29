import numpy_financial as fin
import PySimpleGUI as sg

class Pyfy():
    def __init__(self, my_dict={}):
        self.n = my_dict["n"] if "n" in my_dict.keys() else 0
        self.rate = my_dict["rate"] if "rate" in my_dict.keys() else 0
        self.pv = my_dict["pv"] if "pv" in my_dict.keys() else 0
        self.fv = my_dict["fv"] if "fv" in my_dict.keys() else 0
        self.pmt = my_dict["pmt"] if "pmt" in my_dict.keys() else 0

    def get_n(self):
        return fin.nper(self.rate, self.pmt, self.pv, self.fv, self.when)[0]

    def get_fv(self):
        return fin.fv(self.rate, self.n, self.pmt, self.pv, self.when)[0]

    def get_pv(self):
        return fin.pv(self.rate, self.n, self.pmt, self.fv, self.when)[0]

    def get_rate(self):
        return fin.rate(self.n, self.pmt, self.pv, self.fv, self.when)[0]

    def get_pmt(self):
        return fin.pmt(self.rate, self.n, self.pv, self.fv, self.when)[0]

    def calculate(self, my_dict):
        # options = {"n": lambda: self.get_n(), "fv": lambda: self.get_fv(), "pv": lambda: self.get_pv(),
        #            "pmt": lambda: self.get_pmt(), "rate": lambda: self.get_rate()}

        options = {"n": self.get_n, "fv": self.get_fv, "pv": self.get_pv, "pmt": self.get_pmt, "rate": self.get_rate}
        self.n = my_dict["n"] if "n" in my_dict.keys() else 0
        self.rate = my_dict["rate"] if "rate" in my_dict.keys() else 0
        self.pv = my_dict["pv"] if "pv" in my_dict.keys() else 0
        self.fv = my_dict["fv"] if "fv" in my_dict.keys() else 0
        self.pmt = my_dict["pmt"] if "pmt" in my_dict.keys() else 0
        if "when" in my_dict.keys():
            self.when = {'begin', 1} if "begin" in my_dict["when"] else {'end', 0}
        else:
            self.when = {'end', 0}
        self.pmt = my_dict["pmt"] if "pmt" in my_dict.keys() else 0
        value = options[my_dict["options"]]()
        print(f"{my_dict['options']} value is {value}")


# rate_percent = 3.75/12
# rate = rate_percent/100
# n = 360
# pmt = 1444.92
# fv = 0
# pv = -312000
# x = {"rate":rate, "n":n, "pv":pv, "pmt":pmt, "options":"fv"}
# mypy = pyfy()
# mypy.calculate(x)


if __name__ == "__main__":
    sg.theme('LightPurple')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Financial Calculator: (Enter all but one)')],
              [sg.Text('PV'), sg.InputText()],
              [sg.Text('FV'), sg.InputText()],
              [sg.Text('PMT'), sg.InputText()],
              [sg.Text('N'), sg.InputText()],
              [sg.Text('RATE'), sg.InputText()],
              [sg.Button('Calculate')]]

    # Create the Window
    window = sg.Window('Financial Calculator', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    mypy = Pyfy()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        sg.Popup("license plate", values[1], keep_on_top=True)
        inputs = ["pv", "fv", "pmt", 'n', 'rate']
        values ={}
        for i, val in inputs:
            pass


    window.close()

