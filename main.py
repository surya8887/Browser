from PyQt5.QtCore import QUrl, QSettings
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QTabWidget, \
    QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Browser")

        # Set up the main window and tabs
        self.browser_tabs = QTabWidget()
        self.setCentralWidget(self.browser_tabs)

        self.create_new_tab()  # Create the first tab

        # Buttons for navigation
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.backward)

        self.forward_button = QPushButton("Forward", self)
        self.forward_button.clicked.connect(self.forward)

        self.new_tab_button = QPushButton("New Tab", self)
        self.new_tab_button.clicked.connect(self.create_new_tab)

        self.address_bar = QLineEdit(self)
        self.address_bar.setPlaceholderText("Enter URL here...")
        self.address_bar.returnPressed.connect(self.load_url)

        # Layout for buttons and address bar
        layout = QHBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)
        layout.addWidget(self.new_tab_button)
        layout.addWidget(self.address_bar)

        container = QWidget()
        container.setLayout(layout)
        self.setMenuWidget(container)

        self.show()

    def create_new_tab(self):
        """Create a new tab and set the homepage."""
        browser = QWebEngineView()
        browser.setUrl(QUrl("https://www.google.com"))  # Default homepage
        self.browser_tabs.addTab(browser, "New Tab")
        self.browser_tabs.setCurrentWidget(browser)

    def backward(self):
        """Navigate back in the current tab's history."""
        current_browser = self.browser_tabs.currentWidget()
        if current_browser.history().canGoBack():
            current_browser.back()

    def forward(self):
        """Navigate forward in the current tab's history."""
        current_browser = self.browser_tabs.currentWidget()
        if current_browser.history().canGoForward():
            current_browser.forward()

    def load_url(self):
        """Load URL from the address bar."""
        url = self.address_bar.text()
        current_browser = self.browser_tabs.currentWidget()
        current_browser.setUrl(QUrl(url))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
