class CaseError(Exception):
	def __init__(self, message='Case is not defined.'):
		super().__init__(message)

class TrigonometryError(Exception):
	def __init__(self, message='No such valid triangle.'):
		super().__init__(message)
		
class NegativeDiscriminantError(Exception):
	def __init__(self, message='Type \'Discriminant\' is less than Zero. Therefore, equation has no real roots.'):
		super().__init__(message)

class VariableError(Exception):
	def __init__(self, message='Variable is more than 0.'):
		super().__init__(message)
	
class ComparisonError(Exception):
	def __init__(self, message='Comparison operand not found.'):
		super().__init__(message)
		
class ConstantError(Exception):
	def __init__(self, message='Invalid constant.'):
		super().__init__(message)
		
class DataError(Exception):
	def __init__(self, message='Data cannot be used.'):
		super().__init__(message)
		
class ModeError(Exception):
	pass
