# print("hey there!")

hello_string = "hey it's me!"
# print(hello_string)

def say_phrase(name):
    if len(name) >= 20:
        print(f"Greetings from a faraway land, fine sir/madam/knighted honorable {name}")
    elif len(name) > 10:
        print("Salutations, fine " + name)
    else:
        print("hello, " + name)

# say_phrase("Sire Michael Mazur VI, Esquire")
# nums = [4,8,15,16,23,42]


# print(nums[2])

sundae = {
    "flavor": "vanilla",
    "sauce": "raspberry syrup",
    "scoops": 10,
    "toppings": ["peanuts","chocolate shavings","whipped cream","cherry"]
}

# print(sundae.toppings)

# count = 0
# while(count < 10):
#     print(count)
#     count += 1

# JS syntax below
# for(var i = 0; i < 10; i++){}

nums = [4,8,15,16,23,42,108]
for num in range(1,-101,-1):
    print(num)