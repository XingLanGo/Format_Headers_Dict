import re
print ("The input headers must be copied on Google/Edge format headers.")
in_addr = input ("headers file address(if is null,normally set as 'in_headers'):")
if in_addr == '':
    in_addr = "in_headers.txt"
out_addr = input ("output file address(if is null,normally set as 'out_headers'):")
if out_addr == '':
    out_addr = "out_headers.txt"

in_file = open (in_addr,"r")
out_file = open (out_addr,"w")
temp = re.sub("^","{'",in_file.read())
temp = re.sub("$","'}",temp)
temp = re.sub('\n',"',\n'",temp)
temp = re.sub(': |:',"':'",temp)
out_file.write(temp)
print("%s has successfully output,please copy the headers into you project."%out_addr)