import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import threading
import time
import os

class Story2ComicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Story2Comic Desktop App")
        self.root.geometry("400x200")

        # Title
        title_label = tk.Label(root, text="Story2Comic Generator", font=("Arial", 16))
        title_label.pack(pady=20)

        # Start Button
        self.start_button = tk.Button(root, text="Launch Web Interface", command=self.launch_app, font=("Arial", 12))
        self.start_button.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(root, text="Click to start the application", font=("Arial", 10))
        self.status_label.pack(pady=10)

        self.process = None

    def launch_app(self):
        try:
            self.status_label.config(text="Starting Streamlit server...")
            self.start_button.config(state="disabled")

            # Start Streamlit in a separate thread
            thread = threading.Thread(target=self.run_streamlit)
            thread.daemon = True
            thread.start()

            # Wait a bit for server to start
            time.sleep(3)

            # Open browser
            webbrowser.open("http://localhost:8501")

            self.status_label.config(text="Application running! Check your browser.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to start application: {str(e)}")
            self.start_button.config(state="normal")

    def run_streamlit(self):
        try:
            # Change to the correct directory
            os.chdir(r"E:\updated project\Story2Comic-main\Story2Comic-main")

            # Run streamlit
            self.process = subprocess.Popen(
                ["streamlit", "run", "src/app_streamlit.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # Keep the process running
            self.process.wait()

        except Exception as e:
            print(f"Error running Streamlit: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Story2ComicApp(root)
    root.mainloop()
