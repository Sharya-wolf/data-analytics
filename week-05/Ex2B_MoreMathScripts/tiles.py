
# Sha'Rya Weaver
# 5/8/2026

# You are going to tile a room whose dimensions are length by width feet. There are
# twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? 
# You can only buy full boxes, not a partial box.
# 
# You also want to buy at least 10% more tiles than you need in order to handle chips,
# breakage, and mess-ups. How many total boxes will you buy?

# Script
Length = 15
Width = 14
Tiles_each_box = 30

# Calculations
import math

Total_tiles = Length * Width
Buy_tiles = Total_tiles * 0.10
Tiles_all_together = Total_tiles + Buy_tiles
Boxes = math.ceil(Tiles_all_together / Tiles_each_box)

# Results
print(f"The area of the room is {Total_tiles} ")
print(f"The total number of boxes needed for the tiles including the extras is {Boxes}")

# Output
# The area of the room is 210
# The total number of boxes needed for the tiles including the extras is 8


