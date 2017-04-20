#
#
#
#
#

# get user email address

email = input("What is your email address?: ").strip()

# Slice out username

user = email[:email.index("@")] #Slice left side from @

# slice domain name

domain = email[email.index("@")+1:]  #Slice from after @

# format mesg

output = "Your name is {} and your domain name is {}".format(user, domain)

print(output)


####

# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
# and store it in the answer variable....

answer = word[word.index("establishment"):word.index("ari")]
print (answer)


