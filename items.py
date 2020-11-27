import unittest
class testMethods(unittest.TestCase):

	def test1(self):
		items=[{"id":"S64","name":"Samsung Galaxy S64","cost":20000},
		{"id":"I6S","name":"I phone 6S","cost":80000},
		{"id":"OR1","name":"Oppo Realme1","cost":10000},
		{"id":"L70","name":"LG L70","cost":8000},
		{"id":"PEI9","name":"Panasonic Elugai9","cost":7000}]

		t=[{'id': 'I6S', 'name': 'I phone 6S', 'cost': 80000},
		 {'id': 'L70', 'name': 'LG L70', 'cost': 8000},
		 {'id': 'OR1', 'name': 'Oppo Realme1', 'cost': 10000},
		 {'id': 'PEI9', 'name': 'Panasonic Elugai9', 'cost': 7000},
		 {'id': 'S64', 'name': 'Samsung Galaxy S64', 'cost': 20000}]
		
		items.sort(key=lambda itm:itm["name"])
		self.assertEqual(items,t)

	def test2(self):
		#same name sorting
		items=[{"id":"S","name":"Samsung Galaxy S64","cost":20000},
		{"id":"OR1","name":"Oppo Realme1","cost":10000},
		{"id":"L70","name":"LG L70","cost":8000},
		{"id":"S","name":"Samsung Galaxy S64","cost":10000}]

		t=[{'id': 'L70', 'name': 'LG L70', 'cost': 8000},
		 {'id': 'OR1', 'name': 'Oppo Realme1', 'cost': 10000},
		 {'id': 'S', 'name': 'Samsung Galaxy S64', 'cost': 20000},
		 {'id': 'S', 'name': 'Samsung Galaxy S64', 'cost': 10000}]
		
		items.sort(key=lambda itm:itm["name"])
		self.assertEqual(items,t)

	def test3(self):
		#caps vs small
		items=[{"id":"S","name":"Samsung Galaxy S64"},
		{"id":"OR1","name":"oppo Realme1"},
		{"id":"L70","name":"LG L70"},
		{"id":"SG","name":"Samsung Galaxy Note"}]

		t=[{'id': 'L70', 'name': 'LG L70'},
		 {'id': 'SG', 'name': 'Samsung Galaxy Note'},
		 {'id': 'S', 'name': 'Samsung Galaxy S64'},
		 {'id': 'OR1', 'name': 'oppo Realme1'}]
		
		items.sort(key=lambda itm:itm["name"])
		self.assertEqual(items,t)

	

def main():

	items=[{"id":"S64","name":"Samsung Galaxy S64","cost":20000},
		{"id":"I6S","name":"I phone 6S","cost":80000},
		{"id":"OR1","name":"Oppo Realme1","cost":10000},
		{"id":"L70","name":"LG L70","cost":8000},
		{"id":"PEI9","name":"Panasonic Elugai9","cost":7000}]
	print("The items are:\n",items)
	items.sort(key=lambda itm:itm["name"])
	print(f"List of items in ascending order:\n {items}")




if __name__=="__main__":
	main()
	unittest.main()
