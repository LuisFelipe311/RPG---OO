import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "src"))
sys.path.insert(0, os.path.join(BASE_DIR, "gui"))

from app import App # pyright: ignore[reportMissingImports]

if __name__ == "__main__":
    app = App()
    app.mainloop()