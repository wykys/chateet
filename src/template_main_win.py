# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chateen.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 544)
        self.open = QAction(MainWindow)
        self.open.setObjectName(u"open")
        self.open.setShortcutContext(Qt.WidgetShortcut)
        self.help = QAction(MainWindow)
        self.help.setObjectName(u"help")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.reduce = QAction(MainWindow)
        self.reduce.setObjectName(u"reduce")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tabwidget = QTabWidget(self.splitter)
        self.tabwidget.setObjectName(u"tabwidget")
        self.tabwidget.setEnabled(True)
        self.tabwidget.setDocumentMode(False)
        self.tabwidget.setMovable(False)
        self.tab_chats = QWidget()
        self.tab_chats.setObjectName(u"tab_chats")
        self.verticalLayout_4 = QVBoxLayout(self.tab_chats)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.table_chats = QTableWidget(self.tab_chats)
        self.table_chats.setObjectName(u"table_chats")

        self.verticalLayout_4.addWidget(self.table_chats)

        self.tabwidget.addTab(self.tab_chats, "")
        self.tab_participants = QWidget()
        self.tab_participants.setObjectName(u"tab_participants")
        self.verticalLayout_3 = QVBoxLayout(self.tab_participants)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_participants = QTableWidget(self.tab_participants)
        self.table_participants.setObjectName(u"table_participants")

        self.verticalLayout_3.addWidget(self.table_participants)

        self.tabwidget.addTab(self.tab_participants, "")
        self.tab_more = QWidget()
        self.tab_more.setObjectName(u"tab_more")
        self.tab_more.setEnabled(True)
        self.verticalLayout_7 = QVBoxLayout(self.tab_more)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.table_more = QTableWidget(self.tab_more)
        self.table_more.setObjectName(u"table_more")

        self.verticalLayout_7.addWidget(self.table_more)

        self.tabwidget.addTab(self.tab_more, "")
        self.splitter.addWidget(self.tabwidget)
        self.widget_right = QWidget(self.splitter)
        self.widget_right.setObjectName(u"widget_right")
        self.widget_right.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.widget_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.group_who = QGroupBox(self.widget_right)
        self.group_who.setObjectName(u"group_who")
        self.verticalLayout_5 = QVBoxLayout(self.group_who)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radio_button_all = QRadioButton(self.group_who)
        self.radio_button_all.setObjectName(u"radio_button_all")
        self.radio_button_all.setChecked(True)

        self.verticalLayout_5.addWidget(self.radio_button_all)

        self.radio_button_one = QRadioButton(self.group_who)
        self.radio_button_one.setObjectName(u"radio_button_one")
        self.radio_button_one.setChecked(False)

        self.verticalLayout_5.addWidget(self.radio_button_one)

        self.line_edit_participant = QLineEdit(self.group_who)
        self.line_edit_participant.setObjectName(u"line_edit_participant")
        self.line_edit_participant.setEnabled(False)

        self.verticalLayout_5.addWidget(self.line_edit_participant)


        self.verticalLayout_2.addWidget(self.group_who)

        self.group_date = QGroupBox(self.widget_right)
        self.group_date.setObjectName(u"group_date")
        self.verticalLayout_6 = QVBoxLayout(self.group_date)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_date_enable = QWidget(self.group_date)
        self.widget_date_enable.setObjectName(u"widget_date_enable")
        self.verticalLayout_9 = QVBoxLayout(self.widget_date_enable)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 9)
        self.radio_button_date_no = QRadioButton(self.widget_date_enable)
        self.radio_button_date_no.setObjectName(u"radio_button_date_no")
        self.radio_button_date_no.setChecked(True)

        self.verticalLayout_9.addWidget(self.radio_button_date_no)

        self.radio_button_date_yes = QRadioButton(self.widget_date_enable)
        self.radio_button_date_yes.setObjectName(u"radio_button_date_yes")

        self.verticalLayout_9.addWidget(self.radio_button_date_yes)


        self.verticalLayout_6.addWidget(self.widget_date_enable)

        self.widget_date_range = QWidget(self.group_date)
        self.widget_date_range.setObjectName(u"widget_date_range")
        self.widget_date_range.setEnabled(True)
        self.widget_date_range.setVisible(False)
        self.verticalLayout_8 = QVBoxLayout(self.widget_date_range)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_date_from = QWidget(self.widget_date_range)
        self.widget_date_from.setObjectName(u"widget_date_from")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_date_from)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkbox_from = QCheckBox(self.widget_date_from)
        self.checkbox_from.setObjectName(u"checkbox_from")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_from.sizePolicy().hasHeightForWidth())
        self.checkbox_from.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.checkbox_from)

        self.date_from = QDateEdit(self.widget_date_from)
        self.date_from.setObjectName(u"date_from")
        self.date_from.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.date_from)


        self.verticalLayout_8.addWidget(self.widget_date_from)

        self.widget_date_to = QWidget(self.widget_date_range)
        self.widget_date_to.setObjectName(u"widget_date_to")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_date_to)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.checkbox_to = QCheckBox(self.widget_date_to)
        self.checkbox_to.setObjectName(u"checkbox_to")
        sizePolicy.setHeightForWidth(self.checkbox_to.sizePolicy().hasHeightForWidth())
        self.checkbox_to.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.checkbox_to)

        self.date_to = QDateEdit(self.widget_date_to)
        self.date_to.setObjectName(u"date_to")
        self.date_to.setEnabled(False)
        self.date_to.setWrapping(False)
        self.date_to.setFrame(True)

        self.horizontalLayout_4.addWidget(self.date_to)


        self.verticalLayout_8.addWidget(self.widget_date_to)


        self.verticalLayout_6.addWidget(self.widget_date_range)


        self.verticalLayout_2.addWidget(self.group_date)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.group_export = QGroupBox(self.widget_right)
        self.group_export.setObjectName(u"group_export")
        self.verticalLayout = QVBoxLayout(self.group_export)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_export = QPushButton(self.group_export)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setEnabled(False)

        self.verticalLayout.addWidget(self.btn_export)


        self.verticalLayout_2.addWidget(self.group_export)

        self.splitter.addWidget(self.widget_right)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 883, 22))
        self.file = QMenu(self.menuBar)
        self.file.setObjectName(u"file")
        self.file.setToolTipsVisible(True)
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.tools = QMenu(self.menuBar)
        self.tools.setObjectName(u"tools")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.file.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.tools.menuAction())
        self.file.addAction(self.open)
        self.menuHelp.addAction(self.help)
        self.menuHelp.addAction(self.about)
        self.tools.addAction(self.reduce)

        self.retranslateUi(MainWindow)
        self.radio_button_one.toggled.connect(self.line_edit_participant.setEnabled)
        self.open.triggered.connect(MainWindow.menu_file_open)
        self.checkbox_from.toggled.connect(self.date_from.setEnabled)
        self.checkbox_to.toggled.connect(self.date_to.setEnabled)
        self.radio_button_date_no.clicked.connect(self.widget_date_range.hide)
        self.radio_button_date_yes.clicked.connect(self.widget_date_range.show)

        self.tabwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open.setText(QCoreApplication.translate("MainWindow", u"Otev\u0159\u00edt", None))
#if QT_CONFIG(tooltip)
        self.open.setToolTip(QCoreApplication.translate("MainWindow", u"Otev\u0159\u00edt soubor JSON s daty o va\u0161ich konverzac\u00edch.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.help.setText(QCoreApplication.translate("MainWindow", u"N\u00e1pov\u011bda programu", None))
#if QT_CONFIG(tooltip)
        self.help.setToolTip(QCoreApplication.translate("MainWindow", u"Z\u00edskejte informace o  programu.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.help.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.about.setText(QCoreApplication.translate("MainWindow", u"O projektu", None))
        self.reduce.setText(QCoreApplication.translate("MainWindow", u"Fejka\u0159 Otto", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_chats), QCoreApplication.translate("MainWindow", u"Chaty", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_participants), QCoreApplication.translate("MainWindow", u"\u00da\u010dastn\u00edci", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_more), QCoreApplication.translate("MainWindow", u"V\u00edce", None))
        self.group_who.setTitle(QCoreApplication.translate("MainWindow", u"Kdo poskytene data?", None))
        self.radio_button_all.setText(QCoreApplication.translate("MainWindow", u"V\u0161ichni \u00fa\u010dastn\u00edci", None))
        self.radio_button_one.setText(QCoreApplication.translate("MainWindow", u"J\u00e1", None))
#if QT_CONFIG(tooltip)
        self.line_edit_participant.setToolTip(QCoreApplication.translate("MainWindow", u"\u00da\u010dastn\u00edku, zadejte sv\u00e9 jm\u00e9no.", None))
#endif // QT_CONFIG(tooltip)
        self.group_date.setTitle(QCoreApplication.translate("MainWindow", u"\u010casov\u011b omezit data?", None))
        self.radio_button_date_no.setText(QCoreApplication.translate("MainWindow", u"Ne", None))
        self.radio_button_date_yes.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.checkbox_from.setText(QCoreApplication.translate("MainWindow", u"Od", None))
        self.date_from.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.checkbox_to.setText(QCoreApplication.translate("MainWindow", u"Do", None))
        self.date_to.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.group_export.setTitle(QCoreApplication.translate("MainWindow", u"P\u0159isp\u011bte na olt\u00e1\u0159 v\u011bdy.", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Exportovat", None))
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"Soubor", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"N\u00e1pov\u011bda", None))
        self.tools.setTitle(QCoreApplication.translate("MainWindow", u"N\u00e1stroje", None))
    # retranslateUi

