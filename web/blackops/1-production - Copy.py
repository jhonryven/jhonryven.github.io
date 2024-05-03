import tkinter as tk
from tkinter import filedialog, simpledialog, ttk
from PIL import Image, ImageDraw, ImageTk
import os

class ScrollableCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_configure)
        self.frame = tk.Frame(self)
        self.vertical_scroll = ttk.Scrollbar(parent, orient="vertical", command=self.yview)
        self.config(yscrollcommand=self.vertical_scroll.set)
        self.vertical_scroll.pack(side="right", fill="y")
        self.create_window((0, 0), window=self.frame, anchor="nw")

    def on_configure(self, event):
        self.config(scrollregion=self.bbox("all"))

class ImageSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Splitter")

        self.scrollable_canvas = ScrollableCanvas(self.root)
        self.scrollable_canvas.pack(fill=tk.BOTH, expand=True)

        self.image = None
        self.photo = None
        self.split_lines = {"rows": [], "columns": []}
        self.save_count = 0

        self.used_filenames = set()  # Set to keep track of used filenames

        self.scrollable_canvas.bind("<Button-1>", self.add_row)
        self.scrollable_canvas.bind("<Button-3>", self.add_column)
        self.root.bind("<KeyPress-s>", self.save)
        self.root.bind("<Control-z>", self.undo)

        self.undo_stack = []

        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open Image", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_sections)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.scrollable_canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.scrollable_canvas.config(scrollregion=self.scrollable_canvas.bbox("all"))
            self.root.geometry(f"{self.image.width}x{self.image.height}")

    def add_row(self, event):
        if self.image:
            y = event.y
            self.split_lines["rows"].append(y)
            self.undo_stack.append(("rows", y))
            self.draw_lines()

    def add_column(self, event):
        if self.image:
            x = event.x
            self.split_lines["columns"].append(x)
            self.undo_stack.append(("columns", x))
            self.draw_lines()

    def draw_lines(self):
        if self.photo:
            self.canvas.delete("lines")
            for y in self.split_lines["rows"]:
                self.canvas.create_line(0, y, self.image.width, y, fill="red", tags="lines")

            for x in self.split_lines["columns"]:
                self.canvas.create_line(x, 0, x, self.image.height, fill="blue", tags="lines")

    def undo(self, event):
        if self.undo_stack:
            action, value = self.undo_stack.pop()
            self.split_lines[action].remove(value)
            self.draw_lines()

    def save(self, event):
        self.save_sections()

    def save_sections(self):
        if self.image:
            start_number = simpledialog.askinteger("Starting Number", "Enter the starting number for filenames:")
            if start_number is None:
                return

            for i, (row_start, row_end) in enumerate(zip([0] + self.split_lines["rows"], self.split_lines["rows"] + [self.image.height])):
                for col_start, col_end in zip([0] + self.split_lines["columns"], self.split_lines["columns"] + [self.image.width]):
                    section = self.image.crop((col_start, row_start, col_end, row_end))

                    base_filename = str(start_number + (i // 2))
                    if i % 2 == 1:
                        filename = self.generate_unique_filename(base_filename + "a.png")
                    else:
                        filename = self.generate_unique_filename(base_filename + ".png")

                    section.save(filename)
                    self.used_filenames.add(filename)

    def generate_unique_filename(self, filename):
        # Generate a unique filename by appending a number if the filename already exists
        base_name, ext = os.path.splitext(filename)
        unique_name = filename
        counter = 1
        while unique_name in self.used_filenames:
            unique_name = f"{base_name}_{counter}{ext}"
            counter += 1
        return unique_name

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ImageSplitterApp(root)
        root.mainloop()
    except Exception as e:
        with open("error_log.txt", "w") as f:
            f.write(str(e))