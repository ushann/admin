

def print_subject_name_function():
  for x in sub_name:
    print('Subject Name :' + x)

sub_name = ["BME_221", "BME_223", "BME_225", "EEE_227", "MATH_263"]

def print_subject1_function():
  for i in sub1_details:
    for j in i:
      print(j)
    print("")

sub1_details = [["CT1", "08/07/2011", "syllabus", "upcoming"],
                ["CT2", "date", "syllabus", "13"],
                ["CT3", "date", "syllabus", "12"],
                ["CT4", "13/01/2022", "syllabus", "20"]]

def print_subject2_function():
  for i in sub2_details:
    for j in i:
      print(j)
    print("")

sub2_details = [["CT1", "01/11/2023", "syllabus", "upcoming"],
                ["CT2", "04/05/2021", "syllabus", "upcoming"],
                ["CT3", "02/03/2010", "syllabus", "10"],
                ["CT4", "date", "syllabus", "17"]]

def print_subject3_function():
  for i in sub3_details:
    for j in i:
      print(j)
    print("")

sub3_details = [["CT1", "13/12/2014", "syllabus", "upcoming"],
                ["CT2", "date", "syllabus", "12"],
                ["CT3", "date", "syllabus", "11"],
                ["CT4", "15/12/2024", "syllabus", "12"]]

def print_subject4_function():
  for i in sub4_details:
    for j in i:
      print(j)
    print("")

sub4_details = [["CT1", "01/01/1997", "syllabus", "11"],
                ["CT2", "date", "syllabus", "2"],
                ["CT3", "02/03/2019", "Testing", "upcoming"],
                ["CT4", "date", "syllabus", "10"]]

def print_subject5_function():
  for i in sub5_details:
    for j in i:
      print(j)
    print("")

sub5_details = [["CT1", "11/05/2016", "calculus", "upcoming"],
                ["CT2", "02/02/2050", "linear algebra", "18"],
                ["CT3", "date", "complex eqn", "12"],
                ["CT4", "date", "vector", "10"]]

def previousCTMarks_function():
  ct_marks = [[]]
  for i in range(len(sub1_details)):
    if (sub1_details[i][3] != "upcoming"):
      temporary_array = [sub_name[0]]
      temporary_array.append(sub1_details[i][0])
      temporary_array.append(sub1_details[i][1])
      temporary_array.append(sub1_details[i][2])
      temporary_array.append(sub1_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub2_details)):
    if (sub2_details[i][3] != "upcoming"):
      temporary_array = [sub_name[1]]
      temporary_array.append(sub2_details[i][0])
      temporary_array.append(sub2_details[i][1])
      temporary_array.append(sub2_details[i][2])
      temporary_array.append(sub2_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub3_details)):
     if (sub3_details[i][3] != "upcoming"):
      temporary_array = [sub_name[2]]
      temporary_array.append(sub3_details[i][0])
      temporary_array.append(sub3_details[i][1])
      temporary_array.append(sub3_details[i][2])
      temporary_array.append(sub3_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub4_details)):
    if (sub4_details[i][3] != "upcoming"):
      temporary_array = [sub_name[3]]
      temporary_array.append(sub4_details[i][0])
      temporary_array.append(sub4_details[i][1])
      temporary_array.append(sub4_details[i][2])
      temporary_array.append(sub4_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub5_details)):
    if (sub5_details[i][3] != "upcoming"):
      temporary_array = [sub_name[4]]
      temporary_array.append(sub5_details[i][0])
      temporary_array.append(sub5_details[i][1])
      temporary_array.append(sub5_details[i][2])
      temporary_array.append(sub5_details[i][3])
      ct_marks.append(temporary_array)
  ct_marks.pop(0)
  for x in ct_marks:
    print(x)

def futureCT_function():
  print("**** Upcoming CT Date *******")
  ct_marks = [[]]
  for i in range(len(sub1_details)):
    if (sub1_details[i][3] == "upcoming"):
      temporary_array = [sub_name[0]]
      temporary_array.append(sub1_details[i][0])
      dateformat = sub1_details[i][1]
      temporary_array.append("Day :" + dateformat[0:2])
      temporary_array.append("Month :" + dateformat[3:5])
      temporary_array.append("Year :" + dateformat[-4:])
      temporary_array.append(sub1_details[i][2])
      temporary_array.append(sub1_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub2_details)):
    if (sub2_details[i][3] == "upcoming"):
      temporary_array = [sub_name[1]]
      temporary_array.append(sub2_details[i][0])
      dateformat = sub2_details[i][1]
      temporary_array.append("Day :" + dateformat[0:2])
      temporary_array.append("Month :" + dateformat[3:5])
      temporary_array.append("Year :" + dateformat[-4:])
      temporary_array.append(sub2_details[i][2])
      temporary_array.append(sub2_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub3_details)):
    if (sub3_details[i][3] == "upcoming"):
      temporary_array = [sub_name[2]]
      temporary_array.append(sub3_details[i][0])
      dateformat = sub3_details[i][1]
      temporary_array.append("Day :" + dateformat[0:2])
      temporary_array.append("Month :" + dateformat[3:5])
      temporary_array.append("Year :" + dateformat[-4:])
      temporary_array.append(sub3_details[i][2])
      temporary_array.append(sub3_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub4_details)):
    if (sub4_details[i][3] == "upcoming"):
      temporary_array = [sub_name[3]]
      temporary_array.append(sub4_details[i][0])
      dateformat = sub4_details[i][1]
      temporary_array.append("Day :" + dateformat[0:2])
      temporary_array.append("Month :" + dateformat[3:5])
      temporary_array.append("Year :" + dateformat[-4:])
      temporary_array.append(sub4_details[i][2])
      temporary_array.append(sub4_details[i][3])
      ct_marks.append(temporary_array)
  for i in range(len(sub5_details)):
    if (sub5_details[i][3] == "upcoming"):
      temporary_array = [sub_name[4]]
      temporary_array.append(sub5_details[i][0])
      dateformat = sub5_details[i][1]
      temporary_array.append("Day :" + dateformat[0:2])
      temporary_array.append("Month :" + dateformat[3:5])
      temporary_array.append("Year :" + dateformat[-4:])
      temporary_array.append(sub5_details[i][2])
      temporary_array.append(sub5_details[i][3])
      ct_marks.append(temporary_array)
  ct_marks.pop(0)
  sorted_multi_list = sorted(ct_marks, key=lambda x: (x[4], x[3], x[2]))
  for x in sorted_multi_list:
    print(x)

def writefile_function():
  f = open("E:\\project", 'w')
  f.write(str(sub_name))
  f.write('\n')
  f.write('\n')
  f.write(str(sub_name[0]))
  f.write('\n')
  f.write(str(sub1_details))
  f.write('\n')
  f.write('\n')
  f.write(str(sub_name[1]))
  f.write('\n')
  f.write(str(sub2_details))
  f.write('\n')
  f.write('\n')
  f.write(str(sub_name[2]))
  f.write('\n')
  f.write(str(sub3_details))
  f.write('\n')
  f.write('\n')
  f.write(str(sub_name[3]))
  f.write('\n')
  f.write(str(sub4_details))
  f.write('\n')
  f.write('\n')
  f.write(str(sub_name[4]))
  f.write('\n')
  f.write(str(sub5_details))
  f.close();

def switch(lang):
  if lang == "1":
    print_subject_name_function()
    welcome_function()
  elif lang == "2":
    print("Subject Name : " + sub_name[0])
    print("")
    print_subject1_function()
    welcome_function()
  elif lang == "3":
    print("Subject Name : " + sub_name[1])
    print("")
    print_subject2_function()
    welcome_function()
  elif lang == "4":
    print("Subject Name : " + sub_name[2])
    print("")
    print_subject3_function()
    welcome_function()
  elif lang == "5":
    print("Subject Name : " + sub_name[3])
    print("")
    print_subject4_function()
    welcome_function()
  elif lang == "6":
    print("Subject Name : " + sub_name[4])
    print("")
    print_subject5_function()
    welcome_function()
  elif lang == "7":
    previousCTMarks_function()
    welcome_function()
  elif lang == "8":
    futureCT_function()
    welcome_function()
  elif lang == "9":
    writefile_function()
    welcome_function()
  elif lang =='0':
    return

def welcome_function():
  print("*******************************")
  print('Press 1 to show Subject Name')
  print('Press 2 to show Subject 1 Details')
  print('Press 3 to show Subject 2 Details')
  print('Press 4 to show Subject 3 Details')
  print('Press 5 to show Subject 4 Details')
  print('Press 6 to show Subject 5 Details')
  print('Press 7 to show all previous ct marks')
  print('Press 8 to show all Future CT Date')
  print('Press 9 to write to a file')
  print('Press 0 to exit')
  print("*******************************")
  print("")
  print(switch((input('Please Press a Key : '))))

welcome_function()