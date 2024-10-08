# Vedic Planetary Aspectarium (Version 0.0.0.1)
#
# Copyright (C) 2024 Sithu Aung <https://github.com/SithuAung1988>
# 
# This file is part of Vedic Planetary Aspectarium.
# 
# Vedic Planetary Aspectarium is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Vedic Planetary Aspectarium is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Vedic Planetary Aspectarium.  If not, see <https://www.gnu.org/licenses/>.

import sys
import subprocess
from pathlib import Path
from init import init
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QLabel, QFileDialog, QMessageBox, QGroupBox, QStyle)

init()

class DataInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # Initialize the user interface

    def initUI(self):
        # Main layout of the window
        main_layout = QVBoxLayout()

        # Title for the window
        main_label = QLabel('Load Maitreya chart data.')
        main_label.setStyleSheet('font-weight: bold')
        main_layout.addWidget(main_label)

        # Natal chart data section
        natal_group = QGroupBox('Natal Chart Data:')
        natal_vbox_layout = QVBoxLayout()
        natal_hbox_layout = QHBoxLayout()
        self.natal_field = QLineEdit()  # Text field to display the selected file path
        self.natal_button = QPushButton('Load')  # Button to load the natal chart file
        self.natal_button.clicked.connect(self.openFileDialog)  # Connect the button to openFileDialog method
        natal_hbox_layout.addWidget(self.natal_field)
        natal_hbox_layout.addWidget(self.natal_button)
        natal_vbox_layout.addLayout(natal_hbox_layout)
        natal_group.setLayout(natal_vbox_layout)
        main_layout.addWidget(natal_group)

        # Transit chart data section
        transit_group = QGroupBox('Transit Chart Data:')
        transit_vbox_layout = QVBoxLayout()
        transit_hbox_layout = QHBoxLayout()
        self.transit_field = QLineEdit()  # Text field to display the selected file path
        self.transit_button = QPushButton('Load')  # Button to load the transit chart file
        self.transit_button.clicked.connect(self.openFileDialog)  # Connect the button to openFileDialog method
        transit_hbox_layout.addWidget(self.transit_field)
        transit_hbox_layout.addWidget(self.transit_button)
        transit_vbox_layout.addLayout(transit_hbox_layout)
        transit_group.setLayout(transit_vbox_layout)
        main_layout.addWidget(transit_group)

        # Continue button to process the files
        continue_button = QPushButton('Continue')
        continue_button.clicked.connect(self.processFiles)  # Connect the button to processFiles method
        main_layout.addWidget(continue_button)

        self.setLayout(main_layout)
        self.setWindowTitle('Data Input')  # Set the window title
        self.resize(400, 200)  # Set the window size

    def openFileDialog(self):
        # Open file dialog to load natal and transit chart data
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)')

        # Check which button was clicked and assign the file path to the appropriate field
        if file_path:
            sender = self.sender()  # Get the button that triggered the file dialog
            if sender == self.natal_button:
                self.natal_field.setText(file_path)
            elif sender == self.transit_button:
                self.transit_field.setText(file_path)

    def processFiles(self):
        # Get the file paths from the text fields
        file_path_natal = self.natal_field.text()
        file_path_transit = self.transit_field.text()

        # Check if both files have been loaded
        if not file_path_natal or not file_path_transit :
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('')  # macOS does not support window title
            msg_box.setText('Please enter PROJECT NAME and load both NATAL and TRANSIT chart data.')
            icon = app.style().standardPixmap(QStyle.StandardPixmap.SP_MessageBoxCritical)
            msg_box.setIconPixmap(icon)
            msg_box.exec()  # Display the message box
            return

        # Call the data cleaning script with natal and transit file paths as arguments
        # Passing file_path_natal = natal.txt , file_path_transit = transit.txt
        subprocess.Popen([sys.executable, str(Path(__file__).with_name('dataCleanUp.py')), file_path_natal, file_path_transit],
                         creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
        self.close()  # Close the current window

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Create the application instance
    window = DataInputWindow()  # Create the main window
    window.show()  # Display the window
    sys.exit(app.exec())  # Start the event loop
