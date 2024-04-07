import csv
from statistics import mean
from collections import OrderedDict


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as input_file_name:
        reader = csv.reader(input_file_name)
        grades = OrderedDict()
        for row in reader:
            list_number = [float(i) for i in row[1:]]
            grades[row[0]] = mean(list_number)
        with open(output_file_name, mode='w', newline='') as output_file_name:
            writer = csv.writer(output_file_name)
            for key, value in grades.items():
                writer.writerow([key, value])


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as input_file_name:
        reader = csv.reader(input_file_name)
        grades = OrderedDict()
        for row in reader:
            list_number = [float(i) for i in row[1:]]
            grades[row[0]] = mean(list_number)
        ordered_grades = sorted(grades.items(), key=lambda kv: (kv[1], kv[0]))
        with open(output_file_name, mode='w', newline='') as output_file_name:
            writer = csv.writer(output_file_name)
            for key, value in ordered_grades:
                writer.writerow([key, value])


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as input_file_name:
        reader = csv.reader(input_file_name)
        grades = OrderedDict()
        for row in reader:
            list_number = [float(i) for i in row[1:]]
            grades[row[0]] = mean(list_number)
        ordered_grades = sorted(grades.items(), key=lambda kv: (kv[1], kv[0]))
        with open(output_file_name, mode='w', newline='') as output_file_name:
            writer = csv.writer(output_file_name)
            counter = 0
            three_best = {}
            temp_list = []
            for key, value in reversed(ordered_grades):
                three_best[key] = value
                temp_list.append(value)
                counter += 1
                if counter == 3:
                    break
            if temp_list[0] == temp_list[1] == temp_list[2]:
                three_best = OrderedDict(sorted(three_best.items()))
                for key, value in three_best.items():
                    writer.writerow([key, value])
            else:
                for key, value in three_best.items():
                    writer.writerow([key, value])


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as input_file_name:
        reader = csv.reader(input_file_name)
        grades = OrderedDict()
        for row in reader:
            list_number = [float(i) for i in row[1:]]
            grades[row[0]] = mean(list_number)
        ordered_grades = sorted(grades.items(), key=lambda kv: (kv[1], kv[0]))
        with open(output_file_name, mode='w', newline='') as output_file_name:
            writer = csv.writer(output_file_name)
            counter = 0
            for key, value in ordered_grades:
                writer.writerow([float(value)])
                counter += 1
                if counter == 3:
                    break


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as input_file_name:
        reader = csv.reader(input_file_name)
        grades = OrderedDict()
        for row in reader:
            list_number = [float(i) for i in row[1:]]
            grades[row[0]] = mean(list_number)
        with open(output_file_name, mode='w', newline='') as output_file_name:
            average_of_averages = list()
            counter = 0
            for key, value in (grades.items()):
                average_of_averages.append(float(value))
                counter += 1
            output_file_name.write(str(mean(average_of_averages)))

