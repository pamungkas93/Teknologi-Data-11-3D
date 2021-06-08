import tkinter as tk
# Matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Pandas
import pandas as pd


class PenampilDiagram:

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.geometry('600x400')
        self.__window.title('Penampil Diagram')
        # Gambar widget-widget di Window
        self.__init_widgets()

    def __init_widgets(self):
        data = self.get_data()
        self.__lbl_nama = tk.Label(master=self.__window, text='1941723014 - Dhuta Pamungkas Ibnusiqin')
        self.__lbl_nama.pack()
        self.__gambar_plot(data)

    def get_data(self):
        # Data
        data = {
            'negara': ['USA', 'Canada', 'Germany', 'UK', 'France'],
            'gdp': [45000, 42000, 52000, 49000, 47000]
        }
        df = pd.DataFrame(data, columns=['negara', 'gdp'])
        return df

    def __gambar_plot(self, data: pd.DataFrame):
        print('Menggambar plot..')
        # 1. Buat Figure
        figure = Figure(figsize=(6, 5), dpi=100)
        # # 2. Dari Figure, buat Axes (Yang merender plot)
        axes = figure.add_subplot(1, 1, 1)
        axes.set_title('Negara Vs. GDP Per Kapita')
        # 3. Gambar bar chart dengan menggunakan Axes tadi
        #axes.bar(data['negara'], data['gdp'], color=['red', 'green', 'cyan', 'blue', 'gray'])
        #axes.plot(data['negara'], data['gdp'])
        axes.plot(data['negara'], data['gdp'])
        # 4. Membuat Canvas dari Figure
        canvas = FigureCanvasTkAgg(figure, self.__window)
        # 5. Mengubah Canvas menjadi Widget Tkinter
        canvas_widget = canvas.get_tk_widget()
        # 6. Pack!
        canvas_widget.pack(side=tk.LEFT, fill=tk.BOTH)

    def show(self):
        self.__window.mainloop()
