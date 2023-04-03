import unittest
from tkinter import Tk, Entry, Button

from sentitest import SentimentAnalyzerGUI

class TestSentimentAnalyzerGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.gui = SentimentAnalyzerGUI(self.root)
        self.text_entry = self.gui.text_entry
        self.analyze_button = self.gui.analyze_button
        
    def test_text_entry(self):
        self.assertIsInstance(self.text_entry, Entry)
        
    def test_analyze_button(self):
        self.assertIsInstance(self.analyze_button, Button)
        
    def test_analyze_text(self):
        self.text_entry.insert(0, "I love this product!")
        self.analyze_button.invoke()
        message = self.root._nametowidget(self.root.winfo_children()[2]).cget('message')
        self.assertEqual(message, "The sentiment of the text is positive")
        
if __name__ == '__main__':
    unittest.main()
