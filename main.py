from PyQt5.QtWidgets import*
app = QApplication([])

window = QWidget()
window.resize(700,500)

qest_lbl = QLabel("Редагувати запитаня")

h1 = QVBoxLayout()
h2 = QVBoxLayout()
main_line = QHBoxLayout()

qest_lbl = QLabel("Список заміток")
qest_lbl1 = QLabel("Список тегів")

answer_list = QListWidget()
answer_text = QTextEdit()

answer = QLabel()

qest_btn = QPushButton("Створити замітку")
qest_btn1 = QPushButton("Видалити замітку")
qest_btn2 = QPushButton("Зберегти замітку")
qest_btn3 = QPushButton("додати до замітку")
qest_btn3 = QPushButton("Відкріпити від замітку")
qest_btn4 = QPushButton("Видалити від замітки")
qest_btn5 = QPushButton("шукати замітки по тегу")













window.setLayout(main_line)



window.show()
app.exec()
