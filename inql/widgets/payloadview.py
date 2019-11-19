import platform

if platform.system() != "Java":
    print("Load this file inside Burp Suite/jython, if you need the stand-alone tool run: inql")
    exit(-1)

from javax.swing import JFrame, JPanel, JLabel, JScrollPane, JTextArea
from java.awt import BorderLayout, Color

class PayloadView:
    def __init__(self, payload=None, label=None):
    	if not label: label = "PayloadView"

        self.this = JPanel()
        self.this.setLayout(BorderLayout())

        # Add a label
        self.this.add(BorderLayout.PAGE_START, JLabel(label))

        # Create textarea here and add to the JPanel
        scrollPane = JScrollPane()
        self.textarea = JTextArea()
        self.textarea.setColumns(20)
        self.textarea.setRows(5)
        self.textarea.setLineWrap(True)
        self.textarea.setWrapStyleWord(True)
        self.textarea.setEditable(False)
        self.textarea.setName("TextArea")
        self.textarea.setSelectionColor(Color(255, 153, 51))
        self.textarea.requestFocus()
        scrollPane.setViewportView(self.textarea)
        self.this.add(BorderLayout.CENTER, scrollPane)

        self.refresh(payload)

    def refresh(self, payload):
    	if payload:
    		self.textarea.setText(payload)

if __name__ == "__main__":
    frame = JFrame("PayloadView")
    frame.setForeground(Color.black)
    frame.setBackground(Color.lightGray)
    cp = frame.getContentPane()
    ft = PayloadView(payload='Payload')
    cp.add(ft.this)
    frame.pack()
    frame.setVisible(True)
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)