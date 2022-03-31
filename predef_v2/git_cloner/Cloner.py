from git import Repo


class Cloner(object):
	def __init__(self,git_url,project_id,folder_name):
		super(Cloner, self).__init__()
		self.project_id = project_id
		self.folder_name = folder_name
		self.git_url = git_url
	
	def clone(self):
		Repo.clone_from(self.git_url,self.folder_name+"/"+ self.project_id)
