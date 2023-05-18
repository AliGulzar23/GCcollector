import requests
link = "https://www.gradcracker.com/hub/44/stantec/graduate-job/50963/graduate-civil-engineer-2023"
link2 = "https://www.gradcracker.com/hub/1092/lumentum/work-placement-internship/49396/optical-systems-engineer-intern"
parsed = link.split('/')
count = 0
companyIndex = 5
jobTypeIndex =6
JobTitleIndex = 8
for x in parsed:
    print(count , ':' ,x)
    count += 1
