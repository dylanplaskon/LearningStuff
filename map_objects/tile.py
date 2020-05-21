
class Tile:
	#map tiles
	def __init__(self, blocked, block_sight=None):
		self.blocked = blocked
		
		#by default, if a tile is blocked it also blocks light
		
		if block_sight is None:
			block_sight = blocked
			
		self.block_sight = block_sight
		