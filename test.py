from paperbase import auth
from paperbase import config
from paperbase import pdb

#config.createNewProject("test_project")

config.connect("94e13ca4-e50c-4bbd-944b-67d020218e64")
auth.signInUser("aritra@gmail.com", "123456")

#pdb.newPaperBase("user_data")
data = pdb.retrieveData("user_data", "Name")
print(data)


