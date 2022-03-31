class Result:
	def __init__(self,me,filename):
		self.filename = filename
		self.NumberOfOperators = me.numberOfOperators()
		self.NumberOfOperands = me.numberOfOperands()
		self.TotalNumberOfOperators = me.totalNumberOfOperators()
		self.TotalNumberOfOperands = me.totalNumberOfOperands()
		self.HalsteadProgramLength = me.halsteadProgramLength()
		self.LinesOfCode = me.linesOfCode()
		self.McCabeCyclomaticComplexity = me.cyclomaticComplexity()
		self.LinesOfComments = me.linesOfComments()
		self.volume = me.volume()
		self.effort = me.effort()
		
        