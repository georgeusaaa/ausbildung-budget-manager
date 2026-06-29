import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QLineEdit, QPushButton
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ausbildung Budget Manager 🇩🇪")
        self.resize(350, 450)

        # 1. Поля ввода с подсказками (Placeholder)
        self.label_1 = QLabel("<b>1. Ваш месячный лимит / Стипендия (€):</b>")
        self.input_1 = QLineEdit()
        self.input_1.setText("1100") # Сразу ставим дефолтную стипендию в Германии

        self.label_2 = QLabel("Еда (€):")
        self.input_2 = QLineEdit()
        self.input_2.setPlaceholderText("Например: 250")

        self.label_3 = QLabel("Жилье (Аренда комнаты) (€):")
        self.input_3 = QLineEdit()
        self.input_3.setPlaceholderText("Например: 450")

        self.label_4 = QLabel("Транспорт (€):")
        self.input_4 = QLineEdit()
        self.input_4.setPlaceholderText("Например: 50")

        self.label_5 = QLabel("Инвестиции (Акции/ETF) (€):")
        self.input_5 = QLineEdit()
        self.input_5.setPlaceholderText("Например: 200")

        # 2. Кнопка расчета
        self.button = QPushButton("Проверить баланс")
        self.button.setMinimumHeight(40)
        self.button.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.button.clicked.connect(self.count)

        # Метка статуса
        self.label_6 = QLabel("Введите расходы и нажмите 'Проверить баланс'")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True) # Чтобы длинный текст красиво переносился
        self.label_6.setStyleSheet("font-size: 13px; color: #34495e; padding: 10px; background-color: #ecf0f1; border-radius: 5px;")

        # 3. Компоновка макета
        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.input_1)
        layout.addSpacing(10)
        layout.addWidget(QLabel("<b>Внесите ваши расходы за месяц:</b>"))
        layout.addWidget(self.label_2)
        layout.addWidget(self.input_2)
        layout.addWidget(self.label_3)
        layout.addWidget(self.input_3)
        layout.addWidget(self.label_4)
        layout.addWidget(self.input_4)
        layout.addWidget(self.label_5)
        layout.addWidget(self.input_5)
        layout.addSpacing(15)
        layout.addWidget(self.button)
        layout.addWidget(self.label_6)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 4. Логика
    def count(self):
        try:
            val2 = float(self.input_2.text().strip() or 0)
            val3 = float(self.input_3.text().strip() or 0)
            val4 = float(self.input_4.text().strip() or 0)
            val5 = float(self.input_5.text().strip() or 0)
            max_val = float(self.input_1.text().strip() or 0)

            if max_val <= 0 or val2 < 0 or val3 < 0 or val4 < 0 or val5 < 0:
                self.label_6.setText("❌ Ошибка: Значения не могут быть отрицательными!")
                self.label_6.setStyleSheet("color: #c0392b; background-color: #fadbd8; padding: 10px; border-radius: 5px;")
                return

            total_expenses = val2 + val3 + val4 + val5
            remainder = max_val - total_expenses

            # Проверка превышения бюджета
            if total_expenses > max_val:
                overdraft = total_expenses - max_val
                self.label_6.setText(f"🛑 Запрещено! Предел превышен на {overdraft:.2f} €")
                self.label_6.setStyleSheet("color: #c0392b; background-color: #fadbd8; font-weight: bold; padding: 10px; border-radius: 5px;")
            else:
                # Встраиваем датчик безопасности: предупреждаем, если осталось меньше 150 евро
                if remainder < 150:
                    self.label_6.setText(f"⚠️ Внимание! Остаток: {remainder:.2f} €.\nВы вошли в опасную финансовую зону (менее 150 €)!")
                    self.label_6.setStyleSheet("color: #d35400; background-color: #fdebd0; font-weight: bold; padding: 10px; border-radius: 5px;")
                else:
                    self.label_6.setText(f"✅ Всё отлично! Бюджет стабилен. До предела еще {remainder:.2f} €")
                    self.label_6.setStyleSheet("color: #27ae60; background-color: #d4efdf; font-weight: bold; padding: 10px; border-radius: 5px;")

        except ValueError:
            self.label_6.setText("❌ Ошибка: В полях должны быть только числа!")
            self.label_6.setStyleSheet("color: #c0392b; background-color: #fadbd8; padding: 10px; border-radius: 5px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
