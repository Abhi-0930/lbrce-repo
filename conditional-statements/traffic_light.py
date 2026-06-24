# Printing the action based on traffic light color.

color = input()

match color.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")