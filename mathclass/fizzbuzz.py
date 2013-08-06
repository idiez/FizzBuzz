FIZZ = "Fizz"
BUZZ = "Buzz"

class FizzBuzz():

	@staticmethod
	def getFizzBuzz():
		result = ''
		for i in range(1,101):
			if isFizz(i) and isBuzz(i):
				result = result+FIZZ+BUZZ
			elif isFizz(i):
				result = result+FIZZ
			elif isBuzz(i):
				result = result+BUZZ
			else:
				result = result+str(i)
			result = result+'\n'
		return result

def isFizz(num):
	if isDivisibleByThree(num) or containsThree(num):
		return True
	else:
		False

def isBuzz(num):
	if isDivisibleByFive(num) or containsFive(num):
		return True
	else:
		return False

def isDivisibleByThree(num):
	return num%3 == 0

def isDivisibleByFive(num):
	return num%5 == 0

def containsThree(num):
	return '3' in str(num)

def containsFive(num):
	return '5' in str(num)	