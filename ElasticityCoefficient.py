import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ElasticityCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Elasticity Calculator")
        self.setGeometry(100, 100, 400, 200)  # Adjust dimensions as needed

        # Create input fields and labels
        self.q1_label = QLabel("Q1:")
        self.q1_input = QLineEdit()

        self.q2_label = QLabel("Q2:")
        self.q2_input = QLineEdit()

        self.p1_label = QLabel("P1:")
        self.p1_input = QLineEdit()

        self.p2_label = QLabel("P2:")
        self.p2_input = QLineEdit()

        # Create a button
        self.calculate_button = QPushButton("Calculate Elasticity Coefficient")
        self.calculate_button.clicked.connect(self.calculate_coefficient)

        # Create a label to display the result
        self.result_label = QLabel("")

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter values for the following variables:"))
        layout.addWidget(self.q1_label)
        layout.addWidget(self.q1_input)
        layout.addWidget(self.q2_label)
        layout.addWidget(self.q2_input)
        layout.addWidget(self.p1_label)
        layout.addWidget(self.p1_input)
        layout.addWidget(self.p2_label)
        layout.addWidget(self.p2_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_coefficient(self):
        try:
            q1 = float(self.q1_input.text())
            q2 = float(self.q2_input.text())
            p1 = float(self.p1_input.text())
            p2 = float(self.p2_input.text())

            dq = q2 - q1
            dp = p2 - p1

            # Check if the denominator (change in price) is zero
            if dp == 0 or q1 == 0:
                self.result_label.setText("Error: Division by zero.")
            else:
                eq = (dq / dp) * (p1 / q1)
                self.result_label.setText(f"Elasticity Coefficient: {eq:.4f}")
        except ValueError:
            self.result_label.setText("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ElasticityCalculator()
    window.show()
    sys.exit(app.exec_())
