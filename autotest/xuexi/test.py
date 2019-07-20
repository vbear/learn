# *
# **
# ***
# ****
# *****

# num=1
# while num<5:
#     print "*"
#     num=num+1
test = ''
for i in xrange(5):
    test = test + str("*")
print test

test = ''
for i in xrange(5):
    test = ''
    for j in xrange(i):
        test = test + str("*")
    print test
