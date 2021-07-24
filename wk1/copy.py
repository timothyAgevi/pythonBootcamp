friend = [1,2,3,4]

newFriend = list(friend) # creates a copy
friend1 = newFriend # just stores a reference to newfriend
friend.pop()
newFriend.pop(-2)
print(friend)
print(newFriend)
print(friend1)