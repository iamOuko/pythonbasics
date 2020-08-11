# friends = ["Kevin", "Karen", "Jim", "Oscar"]
# friends[2] = "Mike"

# print(friends[2])
# print(friends[1:3])


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Karen"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "kelly")
friends.pop()

lucky_numbers.sort()
lucky_numbers.reverse()

print(friends)
print(friends.index("Jim"))
print(friends.count("Karen"))

print(lucky_numbers)
