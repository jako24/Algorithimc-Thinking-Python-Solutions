def solve(input_text):
    # Process all five neighborhood descriptions
    output = []

    def process_neighborhood(neighborhood):
        streets = neighborhood.split('|')
        candies = 0
        for street in streets:
            houses = list(map(int, street.split()))
            candies += sum(houses)  # Calculate the total candies collected from each street
        min_streets = len(streets)
        return min_streets, candies

    input_lines = input_text.strip().split('\n')
    for neighborhood_description in input_lines:
        min_streets, candies_collected = process_neighborhood(neighborhood_description)
        output.append(f"{min_streets} {candies_collected}")
    
    return output  # Return the results as a list of strings

def main():
    input_data = """5|12 8|7 10|9 6
                    15 6|10 4|11 8 3
                    9 7 12|5|11 8
                    8 6 11|4 10|7
                    11 7 8 9|6|12"""

    results = solve(input_data)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()