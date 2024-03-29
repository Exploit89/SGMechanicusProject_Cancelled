# Основной виджет
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from Modules import shiplist, equipmentlist, styles, fitlist, ships_tuples, descriptionlist
from Modules.ships_tuples import allships_parts


class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        grid = QtWidgets.QGridLayout()  # Создаем сетку для всех элементов главного виджета
        grid.setSpacing(1)  # Расстояние между элементами сетки

        shiptree = QtWidgets.QVBoxLayout()  # Дерево шипов
        frame_shiptree = QtWidgets.QFrame()  # Рамка
        frame_shiptree.setFixedSize(200, 250)
        frame_shiptree.setLayout(shiptree)
        grid.addWidget(frame_shiptree, 2, 1, 6, 1)
        self.shiptreebox = shiplist.ShipTreeView()  # определяем виджет для добавления списка шипов
        self.shiptreebox.clicked.connect(self.on_tree_view_click)
        self.shiptreebox.doubleClicked.connect(self.on_tree_view_doubleclick)

        self.fittreebox = fitlist.FitTreeView()  # определяем виджет для добавления списка фитов
        self.fittreebox.clicked.connect(self.on_fittree_view_click)

        ship_tab = QtWidgets.QTabWidget()  # панель с вкладками - список шипов и фитов
        ship_tab.addTab(self.shiptreebox, "Ship")  # страница шипов
        ship_tab.addTab(self.fittreebox, "Fit")  # страница фитов
        shiptree.addWidget(ship_tab)  # добавляем список шипов
        ship_tab.setCurrentIndex(0)
        ship_tab.setStyleSheet(styles.tab_style)
        ship_tab.setUsesScrollButtons(False)  # прокрутка для кнопок панели с вкладками

        equipmenttree = QtWidgets.QVBoxLayout()  # Дерево эквипа
        frame_equipmenttree = QtWidgets.QFrame()  # Рамка
        frame_equipmenttree.setFixedSize(200, 230)
        frame_equipmenttree.setLayout(equipmenttree)
        grid.addWidget(frame_equipmenttree, 10, 1, 4, 1)
        self.equipmenttreebox = equipmentlist.EquipmentTreeView()

        equipmenttree.addWidget(self.equipmenttreebox)  # Добавляем кнопку

        main_image_frame = QtWidgets.QFrame()  # рамка для главной картинки
        main_image_frame.setFixedSize(250, 250)
        main_image_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(main_image_frame, 2, 3, 6, 6)

        self.pixmap = QPixmap("../Images/SGM_logo.png")  # загрузка(путь) начальной картинки шипа
        self.imagelabel = QLabel(self, alignment=Qt.AlignCenter)
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setPixmap(self.pixmap)  # установка начальной картинки
        hmain_image = QtWidgets.QHBoxLayout()
        hmain_image.addWidget(self.imagelabel)
        vmain_image = QtWidgets.QVBoxLayout(self)
        vmain_image.addLayout(hmain_image)
        vmain_image.addStretch()
        self.setLayout(hmain_image)

        main_image_frame.setLayout(vmain_image)

        self.descriptiontree = descriptionlist.DescriptionView()
        description_frame = QtWidgets.QFrame()  # рамка для показателей
        description_frame.setFixedSize(300, 500)
        description_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        description_frame.setLayout(self.descriptiontree)
        grid.addWidget(description_frame, 2, 12, 12, 1)

        self.descriptiontree.addWidget(self.descriptiontree.damage_label)
        self.descriptiontree.addLayout(self.descriptiontree.damage, QtCore.Qt.AlignTop)
        self.descriptiontree.damage.addWidget(self.descriptiontree.totaldamagelabel)
        self.descriptiontree.damage.addWidget(self.descriptiontree.totaldamagevalue)
        self.descriptiontree.damage.addWidget(self.descriptiontree.dpsdamagelabel)
        self.descriptiontree.damage.addWidget(self.descriptiontree.dpsdamagevalue)
        self.descriptiontree.damage.addWidget(self.descriptiontree.rangelabel)
        self.descriptiontree.damage.addWidget(self.descriptiontree.rangevalue)

        self.descriptiontree.addLayout(self.descriptiontree.crit, QtCore.Qt.AlignTop)
        self.descriptiontree.crit.addWidget(self.descriptiontree.crit_chancelabel)
        self.descriptiontree.crit.addWidget(self.descriptiontree.crit_chancevalue)
        self.descriptiontree.crit.addWidget(self.descriptiontree.crit_damagelabel)
        self.descriptiontree.crit.addWidget(self.descriptiontree.crit_damagevalue)

        self.splitter1 = QtWidgets.QFrame()
        self.splitter1.setFixedSize(280, 1)
        self.splitter1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.splitter1.setLayout(self.descriptiontree.crit)
        self.descriptiontree.addWidget(self.splitter1)

        self.descriptiontree.addWidget(self.descriptiontree.procpower_label)
        self.descriptiontree.addLayout(self.descriptiontree.proc, QtCore.Qt.AlignTop)
        self.descriptiontree.proc.addWidget(self.descriptiontree.processorlabel)
        self.descriptiontree.proc.addWidget(self.descriptiontree.processor_data)
        self.descriptiontree.addWidget(self.descriptiontree.processorvalue)

        self.descriptiontree.addLayout(self.descriptiontree.power, QtCore.Qt.AlignTop)
        self.descriptiontree.power.addWidget(self.descriptiontree.powerlabel)
        self.descriptiontree.power.addWidget(self.descriptiontree.power_data)
        self.descriptiontree.addWidget(self.descriptiontree.powervalue)

        self.splitter2 = QtWidgets.QFrame()
        self.splitter2.setFixedSize(280, 1)
        self.splitter2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.splitter2.setLayout(self.descriptiontree.crit)
        self.descriptiontree.addWidget(self.splitter2)

        self.descriptiontree.addWidget(self.descriptiontree.resistance_label)
        self.descriptiontree.addLayout(self.descriptiontree.shield_resistance, QtCore.Qt.AlignTop)
        self.descriptiontree.shield_resistance.addWidget(QLabel(""))  # пустой лейбл для свободного места
        self.descriptiontree.shield_resistance.addWidget(self.descriptiontree.em_shield_label)
        self.descriptiontree.shield_resistance.addWidget(self.descriptiontree.thermal_shield_label)
        self.descriptiontree.shield_resistance.addWidget(self.descriptiontree.kinetic_shield_label)
        self.descriptiontree.addLayout(self.descriptiontree.shield_resistance_graph, QtCore.Qt.AlignTop)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.shield_resistance_label)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.em_shieldvalue)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.thermal_shieldvalue)
        self.descriptiontree.shield_resistance_graph.addWidget(self.descriptiontree.kinetic_shieldvalue)
        self.descriptiontree.addLayout(self.descriptiontree.armor_resistance_graph, QtCore.Qt.AlignTop)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.armor_resistance_label)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.em_armorvalue)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.thermal_armorvalue)
        self.descriptiontree.armor_resistance_graph.addWidget(self.descriptiontree.kinetic_armorvalue)

        self.splitter3 = QtWidgets.QFrame()
        self.splitter3.setFixedSize(280, 1)
        self.splitter3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.splitter3.setLayout(self.descriptiontree.crit)
        self.descriptiontree.addWidget(self.splitter3)

        self.descriptiontree.addWidget(self.descriptiontree.capacity_label)
        self.descriptiontree.addLayout(self.descriptiontree.shield_capacitylayout, QtCore.Qt.AlignTop)
        self.descriptiontree.shield_capacitylayout.addWidget(self.descriptiontree.shield_capacitylabel)
        self.descriptiontree.shield_capacitylayout.addWidget(self.descriptiontree.shield_capacityvalue)
        self.descriptiontree.shield_capacitylayout.addWidget(self.descriptiontree.shield_rechargevalue_auto)
        self.descriptiontree.shield_capacitylayout.addWidget(self.descriptiontree.shield_rechargevalue_self)
        self.descriptiontree.shield_capacitylayout.addWidget(self.descriptiontree.shield_rechargevalue_projector)
        self.descriptiontree.addLayout(self.descriptiontree.armor_capacitylayout, QtCore.Qt.AlignTop)
        self.descriptiontree.armor_capacitylayout.addWidget(self.descriptiontree.armor_capacitylabel)
        self.descriptiontree.armor_capacitylayout.addWidget(self.descriptiontree.armor_capacityvalue)
        self.descriptiontree.armor_capacitylayout.addWidget(self.descriptiontree.armor_rechargevalue_auto)
        self.descriptiontree.armor_capacitylayout.addWidget(self.descriptiontree.armor_rechargevalue_self)
        self.descriptiontree.armor_capacitylayout.addWidget(self.descriptiontree.armor_rechargevalue_projector)
        self.descriptiontree.addLayout(self.descriptiontree.energy_capacitylayout, QtCore.Qt.AlignTop)
        self.descriptiontree.energy_capacitylayout.addWidget(self.descriptiontree.energy_capacitylabel)
        self.descriptiontree.energy_capacitylayout.addWidget(self.descriptiontree.energy_capacityvalue)
        self.descriptiontree.energy_capacitylayout.addWidget(self.descriptiontree.energy_rechargevalue_auto)
        self.descriptiontree.energy_capacitylayout.addWidget(self.descriptiontree.energy_rechargevalue_self)
        self.descriptiontree.energy_capacitylayout.addWidget(self.descriptiontree.energy_rechargevalue_projector)

        self.splitter4 = QtWidgets.QFrame()
        self.splitter4.setFixedSize(280, 1)
        self.splitter4.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.splitter4.setLayout(self.descriptiontree.crit)
        self.descriptiontree.addWidget(self.splitter4)

        self.descriptiontree.addWidget(self.descriptiontree.capastab_label)
        self.descriptiontree.addLayout(self.descriptiontree.capastablayout, QtCore.Qt.AlignTop)
        self.descriptiontree.capastablayout.addWidget(self.descriptiontree.capastab_passivelabel)
        self.descriptiontree.capastablayout.addWidget(self.descriptiontree.capastab_passivevalue)
        self.descriptiontree.capastablayout.addWidget(self.descriptiontree.capastab_activelabel)
        self.descriptiontree.capastablayout.addWidget(self.descriptiontree.capastab_activevalue)

        self.splitter5 = QtWidgets.QFrame()
        self.splitter5.setFixedSize(280, 1)
        self.splitter5.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        self.splitter5.setLayout(self.descriptiontree.crit)
        self.descriptiontree.addWidget(self.splitter5)

        self.descriptiontree.addWidget(self.descriptiontree.velocity_label)
        self.descriptiontree.addLayout(self.descriptiontree.velocity_passive_layout, QtCore.Qt.AlignTop)
        self.descriptiontree.velocity_passive_layout.addWidget(self.descriptiontree.velocity_passivelabel)
        self.descriptiontree.velocity_passive_layout.addWidget(self.descriptiontree.velocity_passivevalue)
        self.descriptiontree.addLayout(self.descriptiontree.velocity_maximum_layout, QtCore.Qt.AlignTop)
        self.descriptiontree.velocity_maximum_layout.addWidget(self.descriptiontree.velocity_maximumlabel)
        self.descriptiontree.velocity_maximum_layout.addWidget(self.descriptiontree.velocity_maximumvalue)
        self.descriptiontree.addLayout(self.descriptiontree.volumefactor_layout, QtCore.Qt.AlignTop)
        self.descriptiontree.volumefactor_layout.addWidget(self.descriptiontree.volumefactor_label)
        self.descriptiontree.volumefactor_layout.addWidget(self.descriptiontree.volumefactor_value)
        self.descriptiontree.addLayout(self.descriptiontree.warp_layout, QtCore.Qt.AlignTop)
        self.descriptiontree.warp_layout.addWidget(self.descriptiontree.warp_label)
        self.descriptiontree.warp_layout.addWidget(self.descriptiontree.warp_value)

        superdevice_frame = QtWidgets.QFrame()  # рамка для супердевайса
        superdevice_frame.setFixedSize(50, 50)
        superdevice_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(superdevice_frame, 2, 9, 1, 1)

        tactical_component_frame = QtWidgets.QFrame()  # рамка для тактического компонента
        tactical_component_frame.setFixedSize(50, 50)
        tactical_component_frame.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(tactical_component_frame, 4, 9, 1, 1)

        component_frame1 = QtWidgets.QFrame()
        component_frame1.setFixedSize(50, 50)
        component_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame1, 10, 3, 1, 1)

        component_frame2 = QtWidgets.QFrame()
        component_frame2.setFixedSize(50, 50)
        component_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame2, 10, 4, 1, 1)

        component_frame3 = QtWidgets.QFrame()
        component_frame3.setFixedSize(50, 50)
        component_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame3, 10, 5, 1, 1)

        component_frame4 = QtWidgets.QFrame()
        component_frame4.setFixedSize(50, 50)
        component_frame4.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame4, 12, 3, 1, 1)

        component_frame5 = QtWidgets.QFrame()
        component_frame5.setFixedSize(50, 50)
        component_frame5.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame5, 12, 4, 1, 1)

        component_frame6 = QtWidgets.QFrame()
        component_frame6.setFixedSize(50, 50)
        component_frame6.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame6, 12, 5, 1, 1)

        component_frame7 = QtWidgets.QFrame()
        component_frame7.setFixedSize(50, 50)
        component_frame7.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(component_frame7, 14, 3, 1, 1)

        weapon_frame1 = QtWidgets.QFrame()
        weapon_frame1.setFixedSize(50, 50)
        weapon_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(weapon_frame1, 10, 7, 1, 1)

        weapon_frame2 = QtWidgets.QFrame()
        weapon_frame2.setFixedSize(50, 50)
        weapon_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(weapon_frame2, 10, 8, 1, 1)

        weapon_frame3 = QtWidgets.QFrame()
        weapon_frame3.setFixedSize(50, 50)
        weapon_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(weapon_frame3, 10, 9, 1, 1)

        device_frame1 = QtWidgets.QFrame()
        device_frame1.setFixedSize(50, 50)
        device_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(device_frame1, 12, 7, 1, 1)

        device_frame2 = QtWidgets.QFrame()
        device_frame2.setFixedSize(50, 50)
        device_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(device_frame2, 12, 8, 1, 1)

        device_frame3 = QtWidgets.QFrame()
        device_frame3.setFixedSize(50, 50)
        device_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(device_frame3, 12, 9, 1, 1)

        ammo_frame1 = QtWidgets.QFrame()
        ammo_frame1.setFixedSize(50, 50)
        ammo_frame1.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(ammo_frame1, 14, 7, 1, 1)

        ammo_frame2 = QtWidgets.QFrame()
        ammo_frame2.setFixedSize(50, 50)
        ammo_frame2.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(ammo_frame2, 14, 8, 1, 1)

        ammo_frame3 = QtWidgets.QFrame()
        ammo_frame3.setFixedSize(50, 50)
        ammo_frame3.setFrameStyle(QtWidgets.QFrame.StyledPanel)
        grid.addWidget(ammo_frame3, 14, 9, 1, 1)

        grid.setColumnMinimumWidth(0, 1)  # ширина пустой колонки
        grid.setColumnMinimumWidth(2, 20)
        grid.setColumnMinimumWidth(6, 5)
        grid.setColumnMinimumWidth(11, 20)
        grid.setColumnMinimumWidth(13, 1)

        grid.setRowMinimumHeight(0, 1)  # высота пустой строки
        grid.setRowMinimumHeight(8, 10)
        grid.setRowMinimumHeight(15, 25)

        self.image_label = QtWidgets.QLabel("shipname")  # задаем лейбл над картинкой шип+фит
        self.image_fit_label = QtWidgets.QLabel("fit name")
        grid.addWidget(self.image_label, 1, 3, 1, 2)
        grid.addWidget(self.image_fit_label, 1, 5, 1, 3)

        description_label = QtWidgets.QLabel("Description")  # лейбл итоговых характеристик
        grid.addWidget(description_label, 1, 12, 1, 1, QtCore.Qt.AlignCenter)

        """в сетке grid по координатам 1-1-1-1 есть место для кнопок"""

        equipmenttree_label = QtWidgets.QLabel("Equipment")  # лейбл дерева эквипа
        grid.addWidget(equipmenttree_label, 9, 1, 1, 1, QtCore.Qt.AlignCenter)

        superdevice_label = QtWidgets.QLabel("S-Device")
        grid.addWidget(superdevice_label, 1, 9, 1, 1, QtCore.Qt.AlignCenter)

        tactical_component_label = QtWidgets.QLabel("Tactical")
        grid.addWidget(tactical_component_label, 3, 9, 1, 1, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        component_slot_label = QtWidgets.QLabel("Components")
        grid.addWidget(component_slot_label, 9, 3, 1, 3, QtCore.Qt.AlignCenter)

        weapon_slot_label = QtWidgets.QLabel("Weapons")
        grid.addWidget(weapon_slot_label, 9, 7, 1, 3, QtCore.Qt.AlignCenter)

        device_slot_label = QtWidgets.QLabel("Devices")
        grid.addWidget(device_slot_label, 11, 7, 1, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        ammo_slot_label = QtWidgets.QLabel("Ammo")
        grid.addWidget(ammo_slot_label, 13, 7, 1, 3, QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom)

        self.setLayout(grid)

    def on_tree_view_click(self, index):
        """Выбор корабля в списке"""
        item = self.shiptreebox.get_item(index)
        pointerQStandardItem = self.shiptreebox.ship_standard_item_model.itemFromIndex(index)
        print(f'{item.text():>5}, {pointerQStandardItem}')  # pointerQStandardItem | :>5 это размер отступа
        print(item.text())  # Имя объекта
        print(item.row())  # Номер строки объекта (возможно надо еще поработать, чтобы не было конфликтов)

        shiptuple = ships_tuples.allships_parts  # словарь с кортежами шипов
        shiptuple2 = ships_tuples.allships  # кортеж с кортежами шипов

        itemname = str(item.text()).lower()  # приводим имя объекта в строку с маленькой буквы

        for i in allships_parts.items():  # проверяем имя из списка, присваиваем значение ship_id переменной
            ship = itemname
            if i[0] == ship:
                itemrow2 = i[1][0]
            else:
                pass

        if itemname in shiptuple:
            self.newpixmap = QPixmap(shiptuple2[itemrow2][9])
            self.imagelabel.setPixmap(self.newpixmap)
            self.image_label.setText(item.text())  # Задаем название шипа над картинкой
            self.descriptiontree.processor_data.setText("0" + " / " + str(int(shiptuple2[itemrow2][10])))
            self.descriptiontree.processorvalue.setMaximum(int(shiptuple2[itemrow2][10]))
            self.descriptiontree.power_data.setText("0" + " / " + str(int(shiptuple2[itemrow2][11])))
            self.descriptiontree.powervalue.setMaximum(int(shiptuple2[itemrow2][11]))
            self.descriptiontree.energy_capacityvalue.setText(str(int(shiptuple2[itemrow2][12])))
            self.descriptiontree.energy_rechargevalue_auto.setText(str(int(shiptuple2[itemrow2][13])) + " p/s")
            self.descriptiontree.em_shieldvalue.setText(str(int(shiptuple2[itemrow2][17])) + "%")
            self.descriptiontree.kinetic_shieldvalue.setText(str(int(shiptuple2[itemrow2][18])) + "%")
            self.descriptiontree.thermal_shieldvalue.setText(str(int(shiptuple2[itemrow2][19])) + "%")
            self.descriptiontree.em_armorvalue.setText(str(int(shiptuple2[itemrow2][20])) + "%")
            self.descriptiontree.kinetic_armorvalue.setText(str(int(shiptuple2[itemrow2][21])) + "%")
            self.descriptiontree.thermal_armorvalue.setText(str(int(shiptuple2[itemrow2][22])) + "%")
            self.descriptiontree.shield_capacityvalue.setText(str(int(shiptuple2[itemrow2][23])))
            self.descriptiontree.shield_rechargevalue_auto.setText(str(int(shiptuple2[itemrow2][24])) + " p/s")
            self.descriptiontree.armor_capacityvalue.setText(str(int(shiptuple2[itemrow2][25])))
            self.descriptiontree.armor_rechargevalue_auto.setText(str(int(shiptuple2[itemrow2][26])) + " p/s")
            self.descriptiontree.volumefactor_value.setText(str(int(shiptuple2[itemrow2][27])))
            self.descriptiontree.warp_value.setText(str(int(shiptuple2[itemrow2][28])))
        else:
            pass

    def get_data_profile(self):
        """получение данных для последующей записи в файл"""
        pass

    def set_data_profile(self):
        """вставка данных из файла в программу"""
        pass

    def on_tree_view_doubleclick(self, index):
        item = self.shiptreebox.get_item(index)
        pointerQStandardItem = self.shiptreebox.ship_standard_item_model.itemFromIndex(index)
        print('double', f'{item.text():>5}, {pointerQStandardItem}')  # pointerQStandardItem | :>5 это размер отступа
        print('double', item.text())  # Имя объекта
        print('double', item.row())  # Номер строки объекта (возможно надо еще поработать, чтобы не было конфликтов)
        main = MainWidget()

        shiptuple = ships_tuples.allships_parts  # словарь с кортежами шипов
        shiptuple2 = ships_tuples.allships
        itemname = str(item.text()).lower()  # приводим имя объекта в строку с маленькой буквы

        for i in allships_parts.items():  # проверяем имя из списка, присваиваем значение ship_id переменной
            ship = itemname
            if i[0] == ship:
                itemrow2 = i[1][0]
            else:
                pass

        if itemname in shiptuple:
            newfitname, ok = QtWidgets.QInputDialog.getText(main, "New fit name", "Enter fit name", text='newfit')
            if ok:
                print(newfitname)
                newfitlist = QtGui.QStandardItem(newfitname)
                newfitlist.setData(itemname, 32)
                if shiptuple2[itemrow2][2] == 'Frigate' and shiptuple2[itemrow2][3] == 'T1':
                    self.fittreebox.t1_frigate_class.appendRow(newfitlist)
                elif shiptuple2[itemrow2][2] == 'Frigate' and shiptuple2[itemrow2][3] == 'T2':
                    self.fittreebox.t2_frigate_class.appendRow(newfitlist)
                elif shiptuple2[itemrow2][2] == 'Frigate' and shiptuple2[itemrow2][3] == 'T3':
                    self.fittreebox.t3_frigate_class.appendRow(newfitlist)
                else:
                    pass
                # добавить копирование инфы из shiplist
                # допилить условия по помещению в определенную ячейку
        else:
            pass

    def on_fittree_view_click(self, data):
        """Выбор фита в списке"""
        item = self.fittreebox.get_item(data)
        print(item.text())  # Имя объекта
        print(item.row())  # Номер строки объекта (возможно надо еще поработать, чтобы не было конфликтов)
        print(item.data(32))

        shiptuple = ships_tuples.allships_parts  # словарь с кортежами шипов
        shiptuple2 = ships_tuples.allships  # кортеж с кортежами шипов

        itemname = str(item.data(32)).lower()  # приводим имя объекта в строку с маленькой буквы

        for i in allships_parts.items():  # проверяем имя из списка, присваиваем значение ship_id переменной
            ship = itemname
            if i[0] == ship:
                itemrow2 = i[1][0]
            else:
                pass

        if itemname in shiptuple:
            self.newpixmap = QPixmap(shiptuple2[itemrow2][9])
            self.imagelabel.setPixmap(self.newpixmap)
            self.image_label.setText(item.data(32))  # Задаем название шипа над картинкой
            self.image_fit_label.setText(item.text())  # Задаем название фита над картинкой
            self.descriptiontree.processor_data.setText("0" + " / " + str(int(shiptuple2[itemrow2][10])))
            self.descriptiontree.processorvalue.setMaximum(int(shiptuple2[itemrow2][10]))
            self.descriptiontree.power_data.setText("0" + " / " + str(int(shiptuple2[itemrow2][11])))
            self.descriptiontree.powervalue.setMaximum(int(shiptuple2[itemrow2][11]))
            self.descriptiontree.energy_capacityvalue.setText(str(int(shiptuple2[itemrow2][12])))
            self.descriptiontree.energy_rechargevalue_auto.setText(str(int(shiptuple2[itemrow2][13])) + " p/s")
            self.descriptiontree.em_shieldvalue.setText(str(int(shiptuple2[itemrow2][17])) + "%")
            self.descriptiontree.kinetic_shieldvalue.setText(str(int(shiptuple2[itemrow2][18])) + "%")
            self.descriptiontree.thermal_shieldvalue.setText(str(int(shiptuple2[itemrow2][19])) + "%")
            self.descriptiontree.em_armorvalue.setText(str(int(shiptuple2[itemrow2][20])) + "%")
            self.descriptiontree.kinetic_armorvalue.setText(str(int(shiptuple2[itemrow2][21])) + "%")
            self.descriptiontree.thermal_armorvalue.setText(str(int(shiptuple2[itemrow2][22])) + "%")
            self.descriptiontree.shield_capacityvalue.setText(str(int(shiptuple2[itemrow2][23])))
            self.descriptiontree.shield_rechargevalue_auto.setText(str(int(shiptuple2[itemrow2][24])) + " p/s")
            self.descriptiontree.armor_capacityvalue.setText(str(int(shiptuple2[itemrow2][25])))
            self.descriptiontree.armor_rechargevalue_auto.setText(str(int(shiptuple2[itemrow2][26])) + " p/s")
            self.descriptiontree.volumefactor_value.setText(str(int(shiptuple2[itemrow2][27])))
            self.descriptiontree.warp_value.setText(str(int(shiptuple2[itemrow2][28])))
        else:
            pass
