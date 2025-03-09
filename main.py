from PyQt6.QtWidgets import *
from help_file import *

notes = read_from_file()


app = QApplication([])
window = QWidget()

notes_text = QTextEdit()

notes_list_lbl = QLabel("список заміток")

notes_list = QListWidget()
notes_list.addItems(notes)
teg_list_lbl = QLabel("Список тегів")
teg_list = QListWidget()

main_line = QHBoxLayout()
main_line.addWidget(notes_text)

v1 =QVBoxLayout()
v1.addWidget(notes_list_lbl)
v1.addWidget(notes_list)


create_notes_btn = QPushButton("Створити замітку")
delet_notes_btn = QPushButton("Видалити замітку")
save_notes_btn = QPushButton("Зберегти замітку")




h1 = QHBoxLayout()
h1.addWidget(create_notes_btn)
h1.addWidget(delet_notes_btn)
v1.addLayout(h1)
v1.addWidget(save_notes_btn)


v1.addWidget(teg_list_lbl)
v1.addWidget(teg_list)

new_teg_input = QLineEdit()
new_teg_input.setPlaceholderText("Введіть тег...")
#v1.addWidget(new_teg_lbl)
v1.addWidget(new_teg_input)

add_to_notes_btn = QPushButton("Додати до замітки")



main_line.addLayout(v1)

def show_note():
    key = notes_list.currentItem().text()
    notes_text.setText(notes[key]["текст"])
    teg_list.clear()
    teg_list.addItems(notes[key]["теги"])
def add_notes():
    note_name, ok = QInputDialog.getText(window, "Нова нотатка", "Введіть назву нотатку")
    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": [

            ]
        }
        notes_list.clear()
        notes_list.addItems(notes)
        write_in_file(notes)

def save_note_funs():
    text = notes_text.toPlainText()
    note_key = notes_list.currentItem().text()
    notes[note_key]["текст"] = text
    write_in_file(notes)

def notes_delet():
    note_key = notes_list.currentItem().text()
    notes.pop(note_key)
    notes_list.clear()
    notes_list.addItems(notes)


delet_notes_btn.clicked.connect(notes_delet)
save_notes_btn.clicked.connect(save_note_funs)
create_notes_btn.clicked.connect(add_notes)
notes_list.itemClicked.connect(show_note)
window.setLayout(main_line)
window.show()
app.exec()