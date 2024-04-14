from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, \
    QHBoxLayout, QButtonGroup
from random import shuffle


class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


# Создание списка вопросов состоящего из объектов класса Question
question_list = []
question_list.append(Question('Какой национальности не сущетсвует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
question_list.append(
    Question('Государственный язык Португалии?', 'Португальский', 'Английский', 'Испанский', 'Французский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Белый', 'Синий', 'Красный'))


# Функция, которая формирует вопрос
def ask(q):
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    text_answer.setText('Правильный ответ:' + q.right_answer)
    RadioGroupBox.show()


# Функция проверяющая провильность ответа
def check_answer():
    if answer[0].isChecked():
        RadioGroupBox.hide()
        text_answer.setText('Правильно!')
        RadioGroupBoxAnswer.show()
    else:
        RadioGroupBox.hide()
        text_answer.setText('Правильный ответ: ' + answer[0].text())
        RadioGroupBoxAnswer.show()
    button.setText('Следующий вопрос')


# Функция для показывания следующего вопроса из списка
def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(question_list):
        main_win.cur_question = 0
    question = question_list[main_win.cur_question]
    ask(question)


# Функция обрабатывающая нажатие на кнопку
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        RadioGroup.setExclusive(True)
        RadioGroupBoxAnswer.hide()
        RadioGroupBox.show()
        button.setText('Ответить')
        next_question()


# Создание главного окна
app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1

# Создание кнопки и вопроса
text = QLabel()
button = QPushButton('Ответить')

# Создание GroupBox и кнопок для ответов
RadioGroup = QButtonGroup()
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answer)

# Объявление лайотов для GroupBox
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

# Формирование GroupBox
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

# Создание GroupBox для проверки ответа
RadioGroupBoxAnswer = QGroupBox('Результат теста')
text_answer = QLabel('Правильно/Неправильно')
layout_for_answer = QVBoxLayout()
layout_for_answer.addWidget(text_answer)
RadioGroupBoxAnswer.setLayout(layout_for_answer)

# Создание лайотов для главного окна
layout_main1 = QHBoxLayout()
layout_main2 = QHBoxLayout()
layout_main3 = QHBoxLayout()
layout_main4 = QVBoxLayout()

# Размещение наших объектов в лайоты для отображения в главном окне
layout_main1.addWidget(text, alignment=Qt.AlignCenter)
layout_main2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
layout_main2.addWidget(RadioGroupBoxAnswer, alignment=Qt.AlignCenter)
layout_main3.addWidget(button, alignment=Qt.AlignCenter)
layout_main4.addLayout(layout_main1)
layout_main4.addLayout(layout_main2)
layout_main4.addLayout(layout_main3)

# Скрытие GroupBox с вариантами ответов
RadioGroupBoxAnswer.hide()

# Добавление главного лайота в окно
main_win.setLayout(layout_main4)

# Создание объекта класса с вопросом
q = Question('Какой национальности не сущетсвует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты')

# Вызов функции ask() с аргументом - объект класса вопроса
next_question()
button.clicked.connect(click_ok)

main_win.resize(400, 400)
main_win.show()
app.exec_()
