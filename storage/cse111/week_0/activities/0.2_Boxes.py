import math

items = 0
items_per_boxes = 0
boxes = 0


items = int(input("How many items do you have? "))
items_per_boxes = int(input("How many items per boxes "))


boxes = items / items_per_boxes 
result_boxes = math.ceil(boxes)
#More efficient num_boxes = math.ceil(num_items / items_per_box)


print(f"For {items} items, packing {items_per_boxes} items in each box, you will need {result_boxes} boxes.")