def recite(start_day, end_day):
    gifts = {
        1: "a Partridge in a Pear Tree",
        2: "two Turtle Doves",
        3: "three French Hens",
        4: "four Calling Birds",
        5: "five Gold Rings",
        6: "six Geese-a-Laying",
        7: "seven Swans-a-Swimming",
        8: "eight Maids-a-Milking",
        9: "nine Ladies Dancing",
        10: "ten Lords-a-Leaping",
        11: "eleven Pipers Piping",
        12: "twelve Drummers Drumming"
    }

    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    lyrics = []
    for i in range(start_day, end_day + 1):
        lyric = f"On the {days[i - 1]} day of Christmas my true love gave to me:"
        for j in range(i, 0, -1):
            if j != i:
                lyric += ","
            if j == 1 and i != 1:
                lyric += " and"
            lyric += f" {gifts[j]}"
        lyric += "."
        lyrics.append(lyric)

    return lyrics

def main():
    start_day = int(input("Enter the start day (1-12): "))
    end_day = int(input("Enter the end day (1-12): "))

    if start_day < 1 or start_day > 12 or end_day < 1 or end_day > 12 or start_day > end_day:
        print("Invalid input. Start day and end day must be between 1 and 12, and start day should be less than or equal to end day.")
        return

    lyrics = recite(start_day, end_day)
    for line in lyrics:
        print(line)

if __name__ == "__main__":
    main()
