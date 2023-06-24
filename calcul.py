from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Calculatot .AMJAD.')
mw.resize(100, 500)

# Layouts
ml = QVBoxLayout()
hl = QHBoxLayout()

# Variables
current_value = 0
result = 0
operator = None

# Widgets
lbl = QLabel('0')
lbl.setFont(QFont('Arial', 20, 500))
btn_numbers = []
for i in range(10):
    btn_numbers.append(QPushButton(str(i)))

btn_decimal = QPushButton('.')
btn_plus = QPushButton('+')
btn_minus = QPushButton('-')
btn_multiply = QPushButton('*')
btn_divide = QPushButton('/')
btn_equals = QPushButton('=')
btn_clear = QPushButton('C')

# Functions
def update_label():
    lbl.setText(str(current_value))

def number_click():
    global current_value
    sender = mw.sender()
    digit = int(sender.text())
    current_value = current_value * 10 + digit
    update_label()

def decimal_click():
    global current_value
    if '.' not in str(current_value):
        current_value = float(str(current_value) + '.')
        update_label()

def operator_click():
    global current_value, result, operator
    sender = mw.sender()
    op = sender.text()
    if operator is None:
        result = current_value
    else:
        calculate()
    current_value = 0
    operator = op

def equals_click():
    global operator
    calculate()
    operator = None

def calculate():
    global current_value, result, operator
    if operator == '+':
        result += current_value
    elif operator == '-':
        result -= current_value
    elif operator == '*':
        result *= current_value
    elif operator == '/':
        result /= current_value
    current_value = result
    update_label()

def clear_click():
    global current_value, result, operator
    current_value = 0
    result = 0
    operator = None
    update_label()

# Connect events
for i in range(10):
    btn_numbers[i].clicked.connect(number_click)

btn_decimal.clicked.connect(decimal_click)
btn_plus.clicked.connect(operator_click)
btn_minus.clicked.connect(operator_click)
btn_multiply.clicked.connect(operator_click)
btn_divide.clicked.connect(operator_click)
btn_equals.clicked.connect(equals_click)
btn_clear.clicked.connect(clear_click)

# Add widgets to layouts
for i in range(1, 10):
    hl.addWidget(btn_numbers[i], alignment=Qt.AlignCenter)
    if i % 3 == 0:
        ml.addLayout(hl)
        hl = QHBoxLayout()

hl.addWidget(btn_numbers[0], alignment=Qt.AlignCenter)
hl.addWidget(btn_decimal, alignment=Qt.AlignCenter)
ml.addLayout(hl)

operators_layout = QVBoxLayout()
operators_layout.addWidget(btn_plus)
operators_layout.addWidget(btn_minus)
operators_layout.addWidget(btn_multiply)
operators_layout.addWidget(btn_divide)
operators_layout.addWidget(btn_equals)
operators_layout.addWidget(btn_clear)

ml.addLayout(operators_layout)
ml.addWidget(lbl, alignment=Qt.AlignCenter)

# Set main layout
mw.setLayout(ml)
mw.show()
app.exec_()


button.clicked.connect(show_text)
mw.setLayout(ly)
mw.show()
app.exec_()