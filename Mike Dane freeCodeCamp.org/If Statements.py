is_male = False
is_tall = True

if is_male and is_tall:               # "and" both have to be true, "or" both or one have to be true
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall.")

