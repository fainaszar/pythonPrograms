import types
import inspect



def createClass(classname ,inherants=None,others=None):

	if inherants and others:
		print("Createing with inherants and others")
		return type(classname,inherants,others)
	elif inherants:
		print ("Creating with inherangts")
		return type(classname,inherants,{})
	elif others:
		print ("Creating with others")
		return type(classname,(),others)
	else:
		print("Creating with name only")
		return type(classname,(),{})


def initialize(*args):	
	argNames = ""
	argSpecs = ""
	for arg in args:
		argSpecs += "self.{arg} = {arg}\n".format(arg=arg)
		argNames += arg + ","

	print argNames.rstrip(",")
	print argSpecs



	exec("""def init(self,{}):
					{}""".format(argNames,argSpecs))




def create_function(name,*args):
	# arguments = ",".join([arg for arg in args])

	def y(self,args):
		
		for arg in args:
			print arg
			self.arg = arg


		


	y_code = types.CodeType(len(args),
                            y.func_code.co_nlocals,
                            y.func_code.co_stacksize,
                            y.func_code.co_flags,
                            y.func_code.co_code,
                            y.func_code.co_consts,
                            y.func_code.co_names,
                            y.func_code.co_varnames,
                            y.func_code.co_filename,
                            name,
                            y.func_code.co_firstlineno,
                            y.func_code.co_lnotab)

	return types.FunctionType(y_code,y.func_globals,name)


def create(name,*args):
	print args
	def func(self,*arg):

		arg = args 
		print arg
		for a in arg:
			print a
			self.a = a

		

	
	return func 


#init = create_function("init","name","course")
	



init = create("init","name","course")


Student = createClass("Student",None,{'__init__' : init})

std = Student("Faizan","Naseer")
print repr(std)

