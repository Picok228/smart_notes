import json

from PyQt5.QtWidgets import *

notes ={}
app = QApplication([])
window = QWidget()
window.setWindowTitle("Розумні замітки")
window.resize(900, 600)

textEdit = QTextEdit()
text1 = QLabel("Список заміток")
listNotes = QListWidget()

createBtn = QPushButton("Створити замітку")
deleteBtn = QPushButton("Видалити замітку")
changeBtn = QPushButton("Змінити замітку")
addBtn = QPushButton("Додати до замітки")
vidkripBtn = QPushButton("Відкріпити від замітки")
poshukBtn = QPushButton("Пошук за тегом")

text2 = QLabel("Список тегів")
listTag = QListWidget()
lineEdit = QLineEdit()


mainLine = QHBoxLayout()
column1 = QVBoxLayout()
column1.addWidget(textEdit)
mainLine.addLayout(column1)
column2 = QVBoxLayout()
column2.addWidget(text1)

column2.addWidget(listNotes)
column2.addWidget(createBtn)

column2.addWidget(deleteBtn)
column2.addWidget(changeBtn)
column2.addWidget(text2)
column2.addWidget(listTag)
column2.addWidget(lineEdit)
column2.addWidget(addBtn)
column2.addWidget(vidkripBtn)
column2.addWidget(poshukBtn)


mainLine.addLayout(column2)

window.setLayout(mainLine)


def read_data():
    global notes
    with open("database.json", "r", encoding="utf-8") as file:
        notes = json.load(file,)

def write_data():
    global notes
    with open("database.json", "w", encoding="utf-8") as file:
       json.dump(notes, file, ensure_ascii=False, indent=4)
read_data()
listNotes.addItems(notes)

def vmist_note():
    name = listNotes.selectedItems()[0].text()
    textEdit.setText(notes[name]["вміст"])
    listTag.clear()
    listTag.addItems(notes[name]["теги"])

listNotes.itemClicked.connect(vmist_note)

def change_note():
    name = listNotes.selectedItems()[0].text()
    notes[name]["вміст"] = textEdit.toPlainText()
    write_data()

changeBtn.clicked.connect(change_note)

def add_tag():
    name = listNotes.selectedItems()[0].text()
    tag = lineEdit.text()
    notes[name]["теги"].append(tag)
    listTag.clear()
    listTag.addItems(notes[name]["теги"])
    write_data()
def delete_tag():
    name_note = listNotes.selectedItems()[0].text()
    name_tag = listTag.selectedItems()[0].text()
    notes[name_note]["теги"].remove(name_tag)
    listTag.clear()
    listTag.addItems(notes[name_note]["теги"])
    write_data()




addBtn.clicked.connect(add_tag)
vidkripBtn.clicked.connect(delete_tag)



def delete_note():
    res, ok = QInputDialog.getText(window,"Введеня","Введіть назву замітки")
    if ok:
        notes.pop(res)
        listNotes.clear()
        listNotes.addItems(notes)
        write_data()

deleteBtn.clicked.connect(delete_note)

def add_note():
    res, ok = QInputDialog.getText(window, "Введення", "Введіть назву замітки")
    print(ok)
    if ok:
        notes[res] ={
            "вміст": "",
            "теги": []

        }
        write_data()

def search_tag():
    button_text = poshukBtn.text()
    tag = lineEdit.text ()
    if button_text == "Пошук за тегом":
        apply_tag_search(tag)
    if button_text == "Скинути пошук":
        print("Функція для скидання пошуку")


        text2.clear()
        listNotes.clear()
        listNotes.addItems(notes)
        poshukBtn.setText("Пошук за тегом")


def apply_tag_search(tag):
    notes_filtered = {}
    for note, value in notes.items():
        if tag in value["теги"]:
            notes_filtered[note] = value
    poshukBtn.setText("Скинути пошук")
    listTag.clear()
    lineEdit.clear()
    listTag.addItems(notes_filtered)

poshukBtn.clicked.connect(search_tag)




app.setStyleSheet("""
    QWidget
    {
        background-color: #3a784e;
        border-radius: 4px;
    }


    QPushButton
    {
        min-height: 25px;
        border-style: double;
        border-width: 2px;
        border-color: bleck;
        background-color: #d9d9d9;
        font-size:16px;
    }
    QTextEdit
    {
        background-color: #d9d9d9;
        border-radius: 4px;
    }

    QListWidget
    {
        background-color: #d9d9d9;
        border-radius: 4px;
    }

    QLineEdit
    {
        background-color: #d9d9d9;
        border-radius: 4px;
        border-width: 7px;
        min-height: 20px;
    }



""")


deleteBtn.clicked.connect(delete_note)

createBtn.clicked.connect(add_note)
window.show()
app.exec_()