import randompredictor
from csvreader import CsvReader
from league import League


csv = "prem16:17.csv"

original_prem = League("normal")
random_prem = League("random")


random_prem_reader = CsvReader(csv, random_prem)
original_prem_reader = CsvReader(csv, original_prem)




for result in random_prem_reader.results:
    random_prem.input_result(result)

# for result in original_prem_reader.results:
#     original_prem.input_result(result)



randompredictor.predicts_league(random_prem)

# counter = 0
#
# for result in random_prem.results:
#     for result in original_prem.results:
#         if result.get_result() == result.get_result():
#             counter += 1
#
# print(counter)


original_prem.display_league()

print("-------------------------------------------------------------")

random_prem.display_league()



