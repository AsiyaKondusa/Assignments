class DateCalculator:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def calculate_weekday(self):
        q = self.day
        m = self.month
        Y = self.year

        if m == 1 or m == 2:
            m += 12
            Y -= 1

        K = Y % 100
        J = Y // 100

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

        return days[h]

if __name__ == "__main__":
    year = int(input("Enter year (e.g., 1589): "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))

    date = DateCalculator(year, month, day)
    print(f"The day of the week was: {date.calculate_weekday()}")