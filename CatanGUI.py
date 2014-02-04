"""
Catan Board Randomiser - GUI
Stuart Bradley	
23/01/2014
"""

import kivy 
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy.graphics as graphics
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView

from math import sin, cos, pi, sqrt
from CatanBackend import CatanBoard, CatanHex
############
#Main Class#
############

class CatanGUI(GridLayout):
	
	#################
	#Build GUI class#
	#################

	def __init__(self, **kwargs):
		super(CatanGUI, self).__init__(**kwargs)

		self.board = CatanBoard()
		self.mode = 'Thin'
		self.board.grid = self.board.ini_Grid()
		self.hexSize = 40
		
		self.hexHeight = self.hexSize * 2
		self.hexVert = 0.75 * self.hexHeight

		self.hexWidth = sqrt(3)/2 * self.hexHeight

		self.rows = 2
		self.gridCanvas = Widget()
		self.gridCanvas.bind(pos=self.update_gridCanvas)
		self.gridCanvas.bind(size=self.update_gridCanvas)
		
		self.UI = GridLayout(cols=2, size_hint_y=0.2)
		self.randomiseButton = Button(text='Randomise')
		self.randomiseButton.bind(on_press=self.randomise_Grid)	
		self.list_Adapter = ListAdapter(data=['Coastal', 'Thin Land Mass', 'Large Land Mass', 'Large Islands', 'Small Islands', 'Random'], cls=ListItemButton, selection_mode='single', allow_empty_selection=True)
		self.list_Adapter.bind(on_selection_change=self.item_Selected)
		self.random_Type = ListView(adapter=self.list_Adapter)
		self.UI.add_widget(self.random_Type)
		self.UI.add_widget(self.randomiseButton)

		self.add_widget(self.gridCanvas)
		self.add_widget(self.UI)

		self.startingX = self.gridCanvas.center_x 
		self.startingY = self.gridCanvas.center_y + (self.gridCanvas.height * 6)

	def item_Selected(self, *args):
		try:
			self.mode = self.list_Adapter.selection[0].text
		except IndexError:
			pass

	def randomise_Grid(self, *args):
		self.board.grid = self.board.ini_Grid()
		self.board.colour_Grid(self.mode)
		self.update_gridCanvas()

	def update_gridCanvas(self, *args):
		self.gridCanvas.canvas.clear()
		xPos = self.startingX
		yPos = self.startingY
		with self.gridCanvas.canvas:
			for i in range(self.board.gridWidth):
				for j in range(self.board.gridHeight):	
					if self.board.grid[i][j] != 'b':
						graphics.Color(self.board.grid[i][j].colour[0],self.board.grid[i][j].colour[1], self.board.grid[i][j].colour[2])
						if j & 1: 
							#Why 0.8655? I don't fucking know is why.
							self.build_mesh(self.hexSize, xPos+(self.hexSize*0.8655), yPos)
							self.board.grid[i][j].x = xPos+(self.hexSize*0.8655)
							self.board.grid[i][j].y = yPos
						else:
							self.build_mesh(self.hexSize, xPos, yPos)
							self.board.grid[i][j].x = xPos
							self.board.grid[i][j].y = yPos
					yPos -= self.hexVert
				yPos = self.startingY
				xPos += self.hexWidth

	def build_mesh(self, size, centre_x, centre_y):
		vertices = []
		indices = []
		for i in range(6):
			istep = (pi * 2) / 6 * (i + 0.5)
			x = centre_x + size * cos(istep) 
			y = centre_y + size * sin(istep) 
			vertices.extend([x, y, 0, 0])
			indices.append(i)
		return graphics.Mesh(vertices=vertices, indices=indices, mode='triangle_fan')


class CatanGUIApp(App):
	title = 'Catan Board Randomiser'
	def build(self):
		Config.set('graphics', 'height', '700')
		Config.set('graphics','resizable',0)
		return CatanGUI()

if __name__ == '__main__':
	CatanGUIApp().run()