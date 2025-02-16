from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()

notes_text = QTextEdit()

notes_list_lbl = QLabel("список заміток")
notes_list = QListWidget()
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

new_teg_lbl = ("Введіть тег...")
new_teg_input = QLineEdit()

v1.addWidget(new_teg_lbl)
v1.addWidget(new_teg_input)



main_line.addLayout(v1)

window.setLayout(main_line)
window.show()
app.exec()