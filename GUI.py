import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QLabel, QWidget
from functools import partial
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QSize

app = QApplication(sys.argv)
grid = QGridLayout()


size = 6
grid.setSpacing(90 // size)
buttons = []
start_val = None
end_val = None
root = QWidget()
walls = []
wall_count = 0
N = 10
global label
label = QLabel("Enter start Value:")
grid.addWidget(label, 0, 0)

def button_clicked(i, j, button):
    global start_val
    global end_val
    global walls
    global wall_count
    global N
    
    if start_val is None:
        button.setStyleSheet("background-color: Black")
        start_val = i, j
        label.setText("Enter end value:")
    elif end_val is None:
        button.setStyleSheet("background-color: Black")
        end_val = i, j
        label.setText("Enter "+str(N)+" wall values")
    else:
        button.setStyleSheet("background-color: gray")
        walls.append((i,j))
        wall_count += 1
        if wall_count == N:
            root.close()

screen = QGuiApplication.primaryScreen()
screen_size = screen.availableSize()
screen_height = screen_size.height()
screen_width = screen_size.width()

margin = 20
button_size = min(screen_height - margin, screen_width - margin) // size

for i in range(size):
    row = []
    for j in range(size):
        button = QPushButton()
        button.setText("")
        button_width = button_size
        button_height = button_size
        button.setFixedSize(QSize(button_width, button_height))
        button.clicked.connect(partial(button_clicked, i, j, button))
        grid.addWidget(button, i, j+10)
        row.append(button)

grid.setColumnStretch(3, 1)
root.setLayout(grid)
root.show()
app.exec_()
