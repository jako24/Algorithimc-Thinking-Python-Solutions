import time

start_time = time.time()

#---------------------------CLASS SOLUTION------------------------------------#
class SnowflakesCounter:
    def __init__(self, snowflakes):
        self.snowflakes = snowflakes
        self.count_snowflakes = {}
        self.same_list = []

    def sorted_snowflakes(self):
        sorted_list = []
        for snowflake in self.snowflakes:
            sorted_snowflakes = sorted(snowflake)
            sorted_list.append(sorted_snowflakes)
        return sorted_list

    def count_equal_lists(self):
        sorted_snowflakes = self.sorted_snowflakes()
        for i in range(len(sorted_snowflakes)):
            for j in range(i + 1, len(sorted_snowflakes)):
                if sorted_snowflakes[i] == sorted_snowflakes[j]:
                    if str(sorted_snowflakes[i]) not in self.count_snowflakes:
                        self.count_snowflakes[str(sorted_snowflakes[i])] = 1
                        self.same_list.append(sorted_snowflakes[i])
                    else:
                        self.count_snowflakes[str(sorted_snowflakes[i])] += 1

    def print_results(self):
        self.count_equal_lists()
        print(f"Total number of equal lists: {sum(self.count_snowflakes.values())}")
        print(f"The following lists have a pair: ")
        for lst in self.same_list:
            print(lst)


snowflakes = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [3, 2, 1]]
counter = SnowflakesCounter(snowflakes)
counter.print_results()

end_time = time.time()
execution_time = end_time - start_time
print("Execution time: ", execution_time, "seconds")