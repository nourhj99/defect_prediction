from predef_v2.metric_extractor.Metric_Extractor import Metric_Extractor
from predef_v2.git_cloner.Cloner import Cloner
from predef_v2.file_explorer.file_explorer_module import exploreFiles
import uuid
from predef_v2.driver.Result import Result
from predef_v2.driver.GlobalResults import GlobalResult
import json 
import torch
from sklearn.preprocessing import StandardScaler
class Project(object):
	"""docstring for Driver"""
	def __init__(self,git_url):
		super(Project, self).__init__()
		self.git_url = git_url
		self.files = []
		self.per_module_results = []
		self.id = str(uuid.uuid1())
		self.path = "predef_v2/projects/"+ self.id
		self.global_result = GlobalResult()
	
	def clone(self):
		cloner = Cloner(self.git_url,self.id,"./predef_v2/projects")
		cloner.clone()

	def explore_project(self):
		self.files =  exploreFiles(self.path)
		print(self.files)

	def analyze(self):
		for file in self.files:
			self.per_module_results.append(Result(Metric_Extractor(file),file))

	def compute_overall_results(self):
		for result in self.per_module_results:
			self.global_result.NumberOfOperators = self.global_result.NumberOfOperators + result.NumberOfOperators
			self.global_result.NumberOfOperands = self.global_result.NumberOfOperands + result.NumberOfOperands
			self.global_result.TotalNumberOfOperators = self.global_result.TotalNumberOfOperators + result.TotalNumberOfOperators
			self.global_result.TotalNumberOfOperands = self.global_result.TotalNumberOfOperands + result.TotalNumberOfOperands
			self.global_result.HalsteadProgramLength = self.global_result.HalsteadProgramLength + result.HalsteadProgramLength
			self.global_result.LinesOfCode = self.global_result.LinesOfCode + result.LinesOfCode
			self.global_result.McCabeCyclomaticComplexity = self.global_result.McCabeCyclomaticComplexity + result.McCabeCyclomaticComplexity/len(self.per_module_results)
			self.global_result.LinesOfComments = self.global_result.LinesOfComments + result.LinesOfComments
			self.global_result.volume = self.global_result.volume + result.volume
			self.global_result.effort = self.global_result.effort + result.effort
		#model = torch.load("./predef_v2/model_trainer/model.h")
		x = []
		x.append(self.global_result.NumberOfOperators)
		x.append(self.global_result.NumberOfOperands)
		x.append(self.global_result.TotalNumberOfOperators)
		x.append(self.global_result.TotalNumberOfOperands)
		x.append(self.global_result.HalsteadProgramLength)
		x.append(self.global_result.LinesOfCode)
		x.append(self.global_result.McCabeCyclomaticComplexity)
		x.append(self.global_result.LinesOfComments)
		x.append(self.global_result.volume)
		x.append(self.global_result.effort)
		print(x)
		self.global_result.prediction = 0
	
	def format(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)

	def globalToJson(self):
		return json.dumps(self.global_result, default=lambda o: o.__dict__, 
			sort_keys=True, indent=4)