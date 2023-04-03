import tkinter as tk
from textblob import TextBlob

class SentimentAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sentiment Analyzer")

        self.label = tk.Label(master, text="Enter text:")
        self.label.pack()

        self.text_entry = tk.Entry(master)
        self.text_entry.pack()

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_text)
        self.analyze_button.pack()

        self.sentiment_label = tk.Label(master, text="")
        self.sentiment_label.pack()

    def analyze_text(self):
        text = self.text_entry.get()
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            self.sentiment_label.config(text="Positive")
        elif sentiment < 0:
            self.sentiment_label.config(text="Negative")
        else:
            self.sentiment_label.config(text="Neutral")

root = tk.Tk()
app = SentimentAnalyzerGUI(root)
root.mainloop()
