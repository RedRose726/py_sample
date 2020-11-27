import unittest
class testMethods(unittest.TestCase):
	
	def test1(self):
		first="This is what"
		message="Test value is none"
		self.assertIsNotNone(first,message)

	def test2(self):
		#if taking empty strings
		first=" "
		message="Test value is not an empty string"
		self.assertTrue(first.isspace(),message)

	
	def test3(self):
		#if counting repeated words
		first="This is what is"
		l=first.split(" ")
		words=set(l)
		self.assertEqual(len(words),3)

	def test4(self):
		#if counting tailing white spaces as words
		first="This is what is "
		l=first.split(" ")
		words=set(l)
		message="white space is not contained in word-set"
		self.assertIn("",words,message)

	

def main():
	s=input("Input a statement:\n")
	l=s.split(" ")
	words=set(l)
	if "" in words:
		print(f"No.of unique words in the statement is: {len(words)-1}")
	else:
		print(f"No.of unique words in the statement is: {len(words)}")


if __name__=="__main__":
	main()
	unittest.main()
	



