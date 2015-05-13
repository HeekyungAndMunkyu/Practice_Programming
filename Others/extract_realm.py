import os

"""
    Please use this script when execute genymotion android device.
"""


home = os.curdir
print "Check whether exist ANDROID_HOME variable..."
if 'ANDROID_HOME' in os.environ:
    home = os.environ['ANDROID_HOME']
    print "Success."
else:
    print "Fail."
    print "Please input your android sdk directory."
    sdk_path = raw_input(">")
    home = sdk_path

path = home + "/platform-tools"

# if you want to use custom path, input your android sdk directory
# sdk_path = raw_input(">")
"""
print "Path: " + path
print "Is it alright???  (y/n)"
answer = raw_input(">")
if answer == "y":
    print "Okay. Let's access sdk directory."
else:
    print "Okay. Please re-input here."
    sdk_path = raw_input(">")
    home = sdk_path
    path = home + "/platform-tools"

"""
print "Change workinh directory..."
os.chdir(path)
print "Success."
print "directory: "
print os.system("ls")

print "What is a realm file name?"
realm_file_name = raw_input(">")
command = "./adb pull /data/data/com.mangoplate.alpha/files/" + realm_file_name + " " + home +"/Downloads"
os.system(command)
