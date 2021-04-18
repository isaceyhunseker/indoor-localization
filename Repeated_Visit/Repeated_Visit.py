import pandas
control = 0
of_unique_user = 0
number_of_user = 0
one_time = 0
two_times = 0
three_times = 0
four_times = 0
five_or_more_times = 0

Imported_DataFrame = pandas.read_csv("repeated_visit.csv", sep=',', encoding='utf-16', low_memory=False, index_col='hopi_id')
print(Imported_DataFrame)
user_no = int(Imported_DataFrame.shape[0]) - 1
avm_no = int(Imported_DataFrame.shape[1]) - 1
avm_list = list(Imported_DataFrame.columns)
repeated_visit_col = ['month', 'mall', 'of_uniqueUser', '5orMoreTimes', '4times', '3times', '2times', '1time']
Analysis_CSV = pandas.DataFrame(columns=repeated_visit_col, index=avm_list)
Analysis_CSV = Analysis_CSV.fillna(0)


def repeated_visit_analysis(hopi_id):
    global Analysis_CSV, five_or_more_times, four_times, three_times, two_times, one_time, of_unique_user
    for index, avm_name in enumerate(avm_list):
        Analysis_CSV.loc[avm_name]['month'] = 11
        Analysis_CSV.loc[avm_name]['mall'] = index
        if Imported_DataFrame.loc[hopi_id][avm_name] > 4:
            Analysis_CSV.loc[avm_name]['5orMoreTimes'] += 1
        elif Imported_DataFrame.loc[hopi_id][avm_name] == 4:
            Analysis_CSV.loc[avm_name]['4times'] += 1
        elif Imported_DataFrame.loc[hopi_id][avm_name] == 3:
            Analysis_CSV.loc[avm_name]['3times'] += 1
        elif Imported_DataFrame.loc[hopi_id][avm_name] == 2:
            Analysis_CSV.loc[avm_name]['2times'] += 1
        elif Imported_DataFrame.loc[hopi_id][avm_name] == 1:
            Analysis_CSV.loc[avm_name]['1time'] += 1
        Analysis_CSV.loc[avm_name]['of_uniqueUser'] = Analysis_CSV.loc[avm_name]['1time']+ Analysis_CSV.loc[avm_name]['2times']+ Analysis_CSV.loc[avm_name]['3times']+Analysis_CSV.loc[avm_name]['4times']+Analysis_CSV.loc[avm_name]['5orMoreTimes']
    of_unique_user = 0

Imported_DataFrame.index.map(repeated_visit_analysis)

print(Analysis_CSV)
Analysis_CSV.to_csv('Repeated_Visit_Analysis.csv', sep=',', encoding='utf-16')
