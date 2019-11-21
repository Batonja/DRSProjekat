from PyQt5.QtWidgets import QMainWindow,QLabel,QApplication;
import sys;

class theMainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.initUI();

    def initUI(self):
        self.setGeometry(200,200,500,500);
        self.label = QLabel("Press space to play");
        self.label.move(250,250);
        self.label.show();
        self.show();


if __name__ == "__main__":
    app = QApplication(sys.argv);
    mainWindow = theMainWindow();
    sys.exit(app.exec_())
