from driver import *

project  = Project("https://github.com/Sanjeev-Thiyagarajan/fastapi-course")
project.clone()
project.explore_project()
project.analyze()
project.compute_overall_results()
print(project.format())