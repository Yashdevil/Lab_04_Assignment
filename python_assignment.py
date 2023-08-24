class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        match = Match(location, team1, team2, timing)
        self.matches.append(match)

    def search_by_team(self, team_name):
        matches = [match for match in self.matches if team_name in (match.team1, match.team2)]
        return matches

    def search_by_location(self, location_name):
        matches = [match for match in self.matches if match.location == location_name]
        return matches

    def search_by_timing(self, timing_type):
        matches = [match for match in self.matches if timing_type in match.timing]
        return matches

def main():
    flight_table = FlightTable()

    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "South Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")

    while True:
        print("Search options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter team name: ")
            matches = flight_table.search_by_team(team_name)
        elif choice == 2:
            location_name = input("Enter location name: ")
            matches = flight_table.search_by_location(location_name)
        elif choice == 3:
            timing_type = input("Enter timing type: ")
            matches = flight_table.search_by_timing(timing_type)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
            continue

        print("Match Location\tTeam 01\tTeam 02\tTiming")
        for match in matches:
            print(f"{match.location}\t{match.team1}\t{match.team2}\t{match.timing}")

if __name__ == "__main__":
    main()

print(" ")