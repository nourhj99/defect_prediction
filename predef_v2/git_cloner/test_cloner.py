from Cloner import *


git_test_url = "https://github.com/octocat/Hello-World"
project_id = "rwerwrew"
folder_name = "../projects"
cloner = Cloner(git_test_url,project_id,folder_name)
cloner.clone()