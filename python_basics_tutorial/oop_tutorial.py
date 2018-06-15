# object oriented programming (OOP)
# basically you create classes that can manipulate data (methods of functions)

''' you can d0 4 things:
		1) hiding info
		2) encapsulation
		3) inheritance
		4) polymorphism
'''
import math
# a class is a collection of attributes that are defined for any object #data members, methods
class Complex:
 	'this class simulates complex numbers'
 	def __init__(self,real = 0,imag = 0):		# this is the constructor method that initiates real and imag to 0  , note self is always placed first in contructor method									  		
 		if (type(real) not in (int, float))	or type(imag) not in(int, float): # this makes sure the input is of the right type
 			raise Exception('Args are not numbers!')							
 		self.__real = real   # the 2 underscore make real a private variable
 		self.__imag = imag
 		#you could also use the following instead of the two lines above
 		self.SetReal(real)
 		self.SetImag(imag) 


 	def GetReal(self):  # these are called getters
 		return self.__real
 	def GetImag(self):
 		return self.__imag

 	def SetReal(self, val):  # these are called setters or mutators
 		if type(val) not in (int, float):
 			raise Exception('real part must be a number')
 		self.__real = val
 	def SetImag(self, val):
 		if type(val) not in (int, float):
 			raise Exception('imag part must be a number')
 		self.__imag = val
 	def GetModulus(self):
 		return self.sqrt(self.GetReal() * self.GetReal() + self.GetImag() * self.GetImag())
 	def GetPhi(self):
 		return math.atan2(self.GetImag(), self.GetReal()) 

 	def __str__(self):
 		return str(self.GetReal()) + '+' + str(self.GetImag()) + 'i';
 	def __add__(self, other):
 		return Complex(self.GetReal() + other.GetReal(), self.GetImag() + other.GetImag())   

 	def __mul__(self, other):
 		if type(other) in (int, float):
 			return Complex(self.GetReal() * other, self.GetImag() * other)
 		else:
 			return Complex(self.GetReal() * other.GetReal() - self.GetImag() * other.GetImag(),
 				self.GetImag() * other.GetImag() + self.GetReal() * other.GetReal())

 	def __truediv__(self, other): 
 		if type(other) in (int,float):
 			return Complex(self.GetReal() / float(other), self.GetImag()/ float(other))
 		else:
 			a, b, c, d, = self.GetReal(), self.GetImag(), other.GetImag(), other.GetReal()
 			nominator = c * c + d * d
 			return Complex((a*c + b*d)/ nominator, (b*c - a *d)/ nominator)



a = Complex(5, 0.3)
b = Complex(-3,4)
print(a + b)

print( a * b)

print(a/b)

'''
c = Complex(2.5, 5.2)

print(c.GetReal(), c.GetImag())

c = Complex()
try:
	c.__real
except Exception as e:
	print(e)

c.SetImag(1)
c.SetReal(2)
print(c.GetReal(), c.GetImag())
'''


# call the class complex
'''
try:
	c = Complex(2,3)
	print(c.real, c.imag)
except	Exception as e:
	print(e)

c = Complex((1,2,3), [1,2,3])
print(c.real, c.imag)
'''

