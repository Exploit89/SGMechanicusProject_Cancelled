# Основное окно приложения

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QPixmap, QIcon

from Modules.implant_window import ImplantWindow
from Modules.academy_window import AcademyWindow
from Modules.research_window import ResearchWindow
from Modules.recruit_window import RecruitWindow
from Modules.mainwidget import MainWidget
from Modules import styles


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent, flags=QtCore.Qt.Window | QtCore.Qt.MSWindowsFixedSizeDialogHint |
                                       QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.setFixedSize(1000, 600)
        self.settings = QtCore.QSettings("Kate Simons", "SG Mechanicus")
        self.SGM = MainWidget()
        self.setCentralWidget(self.SGM)
        self.setStyleSheet(styles.window_style)
        self.SGM.setStyleSheet(styles.window_style)

        menubar = self.menuBar()  # главное меню
        menubar.setStyleSheet(styles.menu_style)
        menubar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)  # убираем меню вызываемое правой кнопкой
        file_menu = menubar.addMenu("File")
        settings_menu = menubar.addMenu("Settings")  # добавить кнопки в меню настроек
        about_menu = menubar.addMenu("Help")

        save_action = QtWidgets.QAction("Save Profile", self)
        # добавить функцию выполнения в эту строку
        save_action.triggered.connect(self.saving_profile)
        file_menu.addAction(save_action)

        load_action = QtWidgets.QAction("Load Profile", self)
        # добавить функцию выполнения в эту строку
        file_menu.addAction(load_action)

        file_menu.addSeparator()  # разделитель в меню

        exit_action = QtWidgets.QAction("Quit", self)  # Кнопка выхода - переместить в конец, добавить диалог -> Save
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        about_action = about_menu.addAction("About", self.aboutInfo)

        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)  # блок панели инструментов (кнопки настроек профиля)
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        toolbar.setFixedHeight(30)
        toolbar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        open_implant = toolbar.addAction("Implant", self.open_implant_window)
        open_academy = toolbar.addAction("Academy", self.open_academy_window)
        open_research = toolbar.addAction("Research", self.open_research_window)
        open_recruit = toolbar.addAction("Recruit", self.open_recruit_window)
        do_screenshot = toolbar.addAction("Screenshot", self.take_screenshot)

        if self.settings.contains("X") and self.settings.contains("Y"):  # проверка и загрузка сохраненных координат
            self.move(self.settings.value("X"), self.settings.value("Y"))

        self.label = QLabel(self)  # Новый лейбл для окна без рамки
        self.label.setText("SG Mechanicus by [INQ]Kate Simons v.0.0.1 alpha")
        self.label.setStyleSheet(styles.label_style)
        self.label.setGeometry(330, 1, 650, 20)

        quit_button = QtWidgets.QPushButton(QIcon("../Images/Icons/Window/close.png"), "", self)  # кнопка закрытия окна
        quit_button.setStyleSheet(styles.tab_style)
        quit_button.setFixedSize(20, 20)
        quit_button.move(980, 0)
        quit_button.setFlat(True)
        quit_button.clicked.connect(self.close)

        minimize_button = QtWidgets.QPushButton(QIcon("../Images/Icons/Window/minimize.png"), "", self)  # свернуть
        minimize_button.setFixedSize(20, 20)
        minimize_button.move(960, 0)
        minimize_button.setFlat(True)
        minimize_button.clicked.connect(self.showMinimized)

        self.pressing = False

    def take_screenshot(self):
        """копирует в буфер обмена скриншот по кнопке"""
        screen = QApplication.primaryScreen()
        winid = self.winId()
        pixmap = screen.grabWindow(winid, 240, 50, 750, 530)
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(pixmap)

    def closeEvent(self, evt):
        """при закрытии - сохранение координат положения окна и диалог сохранения"""
        g = self.geometry()
        self.settings.setValue("X", g.left())
        self.settings.setValue("Y", g.top())

        result = QtWidgets.QMessageBox.question(self.SGM, "Closing confirmation",
                                                "Do you really want to close window?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            evt.accept()
            QtWidgets.QWidget.closeEvent(self.SGM, evt)
        else:
            evt.ignore()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.pressing = False

    def aboutInfo(self):
        """Информация о программе"""
        QtWidgets.QMessageBox.about(self, "About app",
                                    "<center>\"SG Mechanicus\" v0.0.1 alpha<br><br>"
                                    "(c) [INQ]Kate Simons 2020-2021")

    def open_implant_window(self):

        implantWindow = ImplantWindow(self)
        implantWindow.show()

    def open_academy_window(self):

        academyWindow = AcademyWindow(self)
        academyWindow.show()

    def open_research_window(self):

        researchWindow = ResearchWindow(self)
        researchWindow.show()

    def open_recruit_window(self):

        recruitWindow = RecruitWindow(self)
        recruitWindow.show()

    def saving_profile(self):
        # Допилить что откуда и куда сохранять
        file = QtWidgets.QFileDialog.getSaveFileName(parent=self.SGM, caption='Save profile to...',
                                                     directory=QtCore.QDir.currentPath(),
                                                     filter='All (*);;Python Code (*.py *.pyw)')
        fileName = file[0]
        file = QtWidgets.QFileDialog.getSaveFileUrl(parent=self.SGM, caption='Save profile to...',
                                                    filter='All (*);;Python Code (*.py *.pyw)')
        fileName = file[0].toLocalFile()
