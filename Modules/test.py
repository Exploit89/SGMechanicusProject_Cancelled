# Списки имен шипов
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QItemSelectionModel

from Modules import styles


mist_shiplist_name = QtGui.QStandardItem('Mist')
frost_shiplist_name = QtGui.QStandardItem('Frost')
glimmer_shiplist_name = QtGui.QStandardItem('Glimmer')

frigate_list = (mist_shiplist_name, frost_shiplist_name, glimmer_shiplist_name)

destroyer_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
cruiser_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
battlecruiser_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
battleship_list = ['ECD', 'NEF', 'RS', 'OE', 'USSH']
exclusive_ship_list = ['Frigate', 'Destroyer', 'Cruiser', 'Battlecruiser', 'Battleship']

frigate_icon = "../Images/Icons/Frig.png"
destroyer_icon = "../Images/Icons/Destr.png"
cruiser_icon = "../Images/Icons/Cruis.png"
battlecruiser_icon = "../Images/Icons/BC.png"
battleship_icon = "../Images/Icons/BS.png"

t1_icon = "../Images/Icons/T1.png"
t2_icon = "../Images/Icons/T2.png"
t3_icon = "../Images/Icons/T3.png"


class ShipTreeView(QtWidgets.QTreeView):

    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.ship_standard_item_model = QtGui.QStandardItemModel()
        self.setStyleSheet(styles.scrollbar_style)
        self.setAnimated(True)
        self.setIndentation(0)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        frigate_class = QtGui.QStandardItem(QtGui.QIcon(frigate_icon), 'Frigate')
        self.ship_standard_item_model.appendRow([frigate_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        destroyer_class = QtGui.QStandardItem(QtGui.QIcon(destroyer_icon), 'Destroyer')
        self.ship_standard_item_model.appendRow([destroyer_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        cruiser_class = QtGui.QStandardItem(QtGui.QIcon(cruiser_icon), 'Cruiser')
        self.ship_standard_item_model.appendRow([cruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battlecruiser_class = QtGui.QStandardItem(QtGui.QIcon(battlecruiser_icon), 'BattleCruiser')
        self.ship_standard_item_model.appendRow([battlecruiser_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        battleship_class = QtGui.QStandardItem(QtGui.QIcon(battleship_icon), 'BattleShip')
        self.ship_standard_item_model.appendRow([battleship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        exclusive_ship_class = QtGui.QStandardItem('Exclusive')
        self.ship_standard_item_model.appendRow([exclusive_ship_class])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t1_frigate_class = QtGui.QStandardItem(QtGui.QIcon(t1_icon), 'T1')
        frigate_class.appendRow(t1_frigate_class)
        for i in range(len(frigate_list)):
            stditem = QtGui.QStandardItem(frigate_list[i])
            t1_frigate_class.appendRow([stditem])
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t2_frigate_class = QtGui.QStandardItem(QtGui.QIcon(t2_icon), 'T2')
        frigate_class.appendRow(t2_frigate_class)
        self.header().hide()
        self.setModel(self.ship_standard_item_model)

        t3_frigate_class = QtGui.QStandardItem(QtGui.QIcon(t3_icon), 'T3')
        frigate_class.appendRow(t3_frigate_class)
        self.header().hide()
        self.setModel(self.ship_standard_item_model)
        self.setSelection(1)
        self.index = QItemSelectionModel.currentIndex()
        print(self.index)
