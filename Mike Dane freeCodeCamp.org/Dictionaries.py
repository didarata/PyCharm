monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    10: "Ten"
}

print(monthConversions["Mar"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Not a valid key"))
print(monthConversions[10])