import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QColorDialog, 
    QMenuBar, QMenu, QMessageBox, QTextEdit, QFileDialog, QTabWidget, QPushButton)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize

class Notepad(QWidget):
    def __init__(self):
        # Call the parent constructor to initialize the QWidget
        super().__init__()

        # Set up the main window title
        self.setWindowTitle("THE PERFECT Notepad")
        # Set a fixed size for the window; users can't resize it
        self.setFixedSize(QSize(600, 400))  # QSize(width, height)

        # Create a vertical layout to arrange widgets vertically
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)  # Set the layout for the main window

        # Create a Tab Widget to hold multiple tabs
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)  # Add the tab widget to the main layout

        # Add the first tab on initialization
        self.add_new_tab()

        # Create a menu bar for file-related actions
        menu_bar = QMenuBar(self)
        file_menu = QMenu("&File", self)  # Create a "File" menu

        # Add actions to the "File" menu
        new_tab_action = file_menu.addAction("&New Tab")  # New tab action
        new_action = file_menu.addAction("&New")  # New file action
        open_action = file_menu.addAction("&Open")  # Open file action
        save_action = file_menu.addAction("&Save")  # Save file action
        exit_action = file_menu.addAction("E&xit")  # Exit application action

        menu_bar.addMenu(file_menu)  # Add the file menu to the menu bar
        main_layout.setMenuBar(menu_bar)  # Set the menu bar for the main layout

        # Connect menu actions to their respective methods
        new_tab_action.triggered.connect(self.add_new_tab)
        new_action.triggered.connect(self.new_file)
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(QApplication.quit)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)  # Add button layout to the main layout

        # Create and connect action buttons
        new_button = QPushButton(QIcon("images/newicon.png"), "New Tab", self)  # New tab button with icon
        new_button.clicked.connect(self.add_new_tab)  # Connect button to add new tab
        button_layout.addWidget(new_button)  # Add button to button layout

        open_button = QPushButton(QIcon("images/openicon.png"), "Open", self)  # Open button with icon
        open_button.clicked.connect(self.open_file)  # Connect button to open file
        button_layout.addWidget(open_button)  # Add button to button layout

        save_button = QPushButton(QIcon("images/saveicon.png"), "Save", self)  # Save button with icon
        save_button.clicked.connect(self.save_file)  # Connect button to save file
        button_layout.addWidget(save_button)  # Add button to button layout

        # Adding Change Color button
        color_button = QPushButton("Change Text Color", self)
        color_button.clicked.connect(self.change_color)  # Connect the button to change_color method
        button_layout.addWidget(color_button)  # Add color change button to the layout

    def add_new_tab(self):
        """Create a new tab with a QTextEdit widget."""
        text_edit = QTextEdit(self)  # Create a new QTextEdit widget
        text_edit.setAcceptRichText(True)  # Allow rich text, including images
        text_edit.setPlaceholderText("Type here or paste images...")  # Placeholder text
        text_edit.setFont(QFont("Arial", 12))  # Set font for the text edit

        # Add the QTextEdit to a new tab
        self.tabs.addTab(text_edit, f"Tab {self.tabs.count() + 1}")  # Tab title is the count of existing tabs

    def change_color(self):
        """Open a color dialog to change the text color in the current tab."""
        color = QColorDialog.getColor()  # Show color dialog to select color
        if color.isValid():  # Check if a valid color was selected
            current_tab = self.tabs.currentWidget()  # Get the current tab
            if isinstance(current_tab, QTextEdit):  # Check if the current tab is a QTextEdit
                current_tab.setTextColor(color)  # Set the text color of the QTextEdit

    def new_file(self):
        """Clear the current text in the active tab."""
        current_tab = self.tabs.currentWidget()  # Get the current tab
        if isinstance(current_tab, QTextEdit):  # Check if the current tab is a QTextEdit
            current_tab.clear()  # Clear the content of the QTextEdit

    def open_file(self):
        """Open a file and load its content into the current tab."""
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")  # Open file dialog
        if file_name:  # If a file was selected
            with open(file_name, 'r') as file:  # Open the file for reading
                current_tab = self.tabs.currentWidget()  # Get the current tab
                if isinstance(current_tab, QTextEdit):  # Check if the current tab is a QTextEdit
                    current_tab.setPlainText(file.read())  # Load file content into the QTextEdit

    def save_file(self):
        """Save the content of the current tab to a file."""
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")  # Save file dialog
        if file_name:  # If a file name was provided
            current_tab = self.tabs.currentWidget()  # Get the current tab
            if isinstance(current_tab, QTextEdit):  # Check if the current tab is a QTextEdit
                with open(file_name, 'w') as file:  # Open the file for writing
                    file.write(current_tab.toPlainText())  # Write the content of the QTextEdit to the file
                QMessageBox.information(self, "Success", "File saved successfully!")  # Show success message


# This block checks if the script is being run directly.
# If true, it executes the code inside.
# This prevents the code from running when the script is imported as a another file in a another script.
if __name__ == "__main__":
    # Create a QApplication instance to manage the application
    app = QApplication(sys.argv)
    notepad = Notepad()  # Create an instance of the Notepad
    notepad.show()  # Show the Notepad window
    sys.exit(app.exec())  # Start the application event loop and exit when done
