import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from dowloader_interfaice_ui import Ui_MainWindow
from pytube import YouTube

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.DOWNLOAD_BUTTON.clicked.connect(self.download_video)
    
    def download_video(self):
        try:
            url = self.ui.LINK_CHOICE.text()
            url = str(url)
            save_path = self.ui.FILE_CHOICE.text()
            save_path = str(save_path)
            self.yt = YouTube(url)
            self.video = self.yt.streams.get_highest_resolution()
            self.video.download(output_path=save_path)
            self.ui.RESULT_LABEL.setText("Valid Download!")
        except Exception as e:
            self.ui.RESULT_LABEL.setText("Invalid Download!")
            print(e)


if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())