# Program to calculate Body Mass Index (BMI) and other calculations related to Body Mass Index

# Declaration of variables and constants
# Input
con = 1

while con == 1:
  print (" - "*46)
  reception = str("                      HEALTH RECEPTION")
  print (" ".join(reception))
  print (" - "*46)

  import time
  from time import sleep
  time.sleep (0.3)
  name = str(input("     ● Name: "))
  ic = input("     ● IC: ")
  gender = str(input("     ● Gender [M/F]: "))
  while gender != "M" and gender != "F" and gender != "m" and gender != "f":
    gender = str(input("     ● Gender [M/F]: "))
  
  print ("     Choose Range For Age: 1. 0-23 months")
  print ("                                            2. 2 years old and above")
  range_age = int(input("     ● Range For Age: "))
  while range_age != 1 and range_age != 2:
    range_age = int(input("     ● Range For Age: "))
  if range_age == 1:
    age1 = float(input("     ● Age [0-23 months]: "))
    while not (age1 >= 0) and not(age <= 23):
      age1 = float(input("     ● Age [0-23 months]: "))
  else:
    age2 = float(input("     ● Age [2 years old and above]: "))
    while not (age2 >= 2):
      age2 = float(input("     ● Age [2 years old and above]: "))

  blood_type = str(input("     ● Blood Type [A/B/AB/O]: "))
  while blood_type != "A" and blood_type != "B" and blood_type != "AB" and blood_type != "O" and blood_type != "a" and blood_type != "b" and blood_type != "ab" and blood_type != "o":
    blood_type = str(input("     ● Blood Type [A/B/AB/O]: "))

  print ("     Choose Unit For Weight: 1. kg")
  print ("                                             2. pounds")
  print ("                                             3. stones ")
  unit_weight = int(input("     ● Unit For Weight: "))
  while unit_weight != 1 and unit_weight != 2 and unit_weight != 3:
    unit_weight = int(input("     ● Unit For Weight: "))
  if unit_weight == 1:
    weight1 = float(input("     ● Weight [kg]: "))
    weight2 = float(weight1 * 2.20462)
    weight3 = float(weight1 * 0.157473)
  elif unit_weight == 2:
    weight2 = float(input("     ● Weight [pounds]: "))
    weight1 = float(weight2 / 2.20462)
    weight3 = float(weight2 * 0.0714286)
  else:
    weight3 = float(input("     ● Weight [stones]: "))
    weight1 = float(weight3 / 0.157473)
    weight2 = float(weight3 / 0.0714286)

  print ("     Choose Unit For Height: 1. m")
  print ("                                            2. cm")
  print ("                                            3. inches")
  print ("                                            4. feets")
  unit_height = int(input("     ● Unit For Height: "))
  while unit_height != 1 and unit_height != 2 and unit_height != 3 and unit_height != 4:
    unit_height = int(input("     ● Unit For Height: "))
  if unit_height == 1:
    height1 = float(input("     ● Height [m]: "))
    height2 = float(height1 * 100)
    height3 = float(height1 * 39.3701)
    height4 = float(height1 * 3.28084)
  elif unit_height == 2:
    height2 = float(input("     ● Height [cm]: "))
    height1 = float(height2 / 100)
    height3 = float(height2 * 0.393701)
    height4 = float(height2 * 0.0328084)
  elif unit_height == 3:
    height3 = float(input("     ● Height [inches]: "))
    height1 = float(height3 / 39.3701)
    height2 = float(height3 / 0.393701)
    height4 = float(height3 * 0.0833333)
  else:
    height4 = float(input("     ● Height [feets]: "))
    height1 = float(height4 / 3.28084)
    height2 = float(height4 / 0.0328084)
    height3 = float(height4 / 0.0833333)

  print ("     Choose Unit For Shoulder: 1. m")
  print ("                                                2. cm")
  print ("                                                3. inches")
  print ("                                                4. feets")
  unit_shoulder = int(input("     ● Unit For Shoulder: "))
  while unit_shoulder != 1 and unit_shoulder != 2 and unit_shoulder != 3 and unit_shoulder != 4:
    unit_shoulder = int(input("     ● Unit For Shoulder: "))
  if unit_shoulder == 1:
    shoulder1 = float(input("     ● Shoulder [m]: "))
    shoulder2 = float(shoulder1 * 100)
    shoulder3 = float(shoulder1 * 39.3701)
    shoulder4 = float(shoulder1 * 3.28084)
  elif unit_shoulder == 2:
    shoulder2 = float(input("     ● Shoulder [cm]: "))
    shoulder1 = float(shoulder2 / 100)
    shoulder3 = float(shoulder2 * 0.393701)
    shoulder4 = float(shoulder2 * 0.0328084)
  elif unit_shoulder == 3:
    shoulder3 = float(input("     ●Shoulder [inches]: "))
    shoulder1 = float(shoulder3 / 39.3701)
    shoulder2 = float(shoulder3 / 0.393701)
    shoulder4 = float(shoulder3 * 0.0833333)
  else:
    shoulder4 = float(input("     ● Shoulder [feets]: "))
    shoulder1 = float(shoulder4 / 3.28084)
    shoulder2 = float(shoulder4 / 0.0328084)
    shoulder3 = float(shoulder4 / 0.0833333)

  print ("     Choose Unit For Bust: 1. m")
  print ("                                        2. cm")
  print ("                                        3. inches")
  print ("                                        4. feets")
  unit_bust = int(input("     ● Unit For Bust: "))
  while unit_bust != 1 and unit_bust != 2 and unit_bust != 3 and unit_bust != 4:
    unit_bust = int(input("     ● Unit For Bust: "))
  if unit_bust == 1:
    bust1 = float(input("     ● Bust [m]: "))
    bust2 = float(bust1 * 100)
    bust3 = float(bust1 * 39.3701)
    bust4 = float(bust1 * 3.28084)
  elif unit_bust == 2:
    bust2 = float(input("     ● Bust [cm]: "))
    bust1 = float(bust2 / 100)
    bust3 = float(bust2 * 0.393701)
    bust4 = float(bust2 * 0.0328084)
  elif unit_bust == 3:
    bust3 = float(input("     ●Bust [inches]: "))
    bust1 = float(bust3 / 39.3701)
    bust2 = float(bust3 / 0.393701)
    bust4 = float(bust3 * 0.0833333)
  else:
    bust4 = float(input("     ● Bust [feets]: "))
    bust1 = float(bust4 / 3.28084)
    bust2 = float(bust4 / 0.0328084)
    bust3 = float(bust4 / 0.0833333)

  print ("     Choose Unit For Waist: 1. m")
  print ("                                          2. cm")
  print ("                                          3. inches")
  print ("                                          4. feets")
  unit_waist = int(input("     ● Unit For Waist: "))
  while unit_waist != 1 and unit_waist != 2 and unit_waist != 3 and unit_waist != 4:
    unit_waist = int(input("     ● Unit For Waist: "))
  if unit_waist == 1:
    waist1 = float(input("     ● Waist [m]: "))
    waist2 = float(waist1 * 100)
    waist3 = float(waist1 * 39.3701)
    waist4 = float(waist1 * 3.28084)
  elif unit_waist == 2:
    waist2 = float(input("     ● Waist [cm]: "))
    waist1 = float(waist2 / 100)
    waist3 = float(waist2 * 0.393701)
    waist4 = float(waist2 * 0.0328084)
  elif unit_waist == 3:
    waist3 = float(input("     ● Waist [inches]: "))
    waist1 = float(waist3 / 39.3701)
    waist2 = float(waist3 / 0.393701)
    waist4 = float(waist3 * 0.0833333)
  else:
    waist4 = float(input("     ● Waist [feets]: "))
    waist1 = float(waist4 / 3.28084)
    waist2 = float(waist4 / 0.0328084)
    waist3 = float(waist4 / 0.0833333)

  print ("     Choose Unit For High Hip: 1. m")
  print ("                                               2. cm")
  print ("                                               3. inches")
  print ("                                               4. feets")
  unit_high_hip = int(input("     ● Unit For High Hip: "))
  while unit_high_hip != 1 and unit_high_hip != 2 and unit_high_hip != 3 and unit_high_hip != 4:
    unit_high_hip = int(input("     ● Unit For High Hip: "))
  if unit_high_hip == 1:
    high_hip1 = float(input("     ● High Hip [m]: "))
    high_hip2 = float(high_hip1 * 100)
    high_hip3 = float(high_hip1 * 39.3701)
    high_hip4 = float(high_hip1 * 3.28084)
  elif unit_high_hip == 2:
    high_hip2 = float(input("     ● High Hip [cm]: "))
    high_hip1 = float(high_hip2 / 100)
    high_hip3 = float(high_hip2 * 0.393701)
    high_hip4 = float(high_hip2 * 0.0328084)
  elif unit_high_hip == 3:
    high_hip3 = float(input("     ● High Hip [inches]: "))
    high_hip1 = float(high_hip3 / 39.3701)
    high_hip2 = float(high_hip3 / 0.393701)
    high_hip4 = float(high_hip3 * 0.0833333)
  else:
    high_hip4 = float(input("     ● High Hip [feets]: "))
    high_hip1 = float(high_hip4 / 3.28084)
    high_hip2 = float(high_hip4 / 0.0328084)
    high_hip3 = float(high_hip4 / 0.0833333)

  print ("     Choose Unit For Hip: 1. m")
  print ("                                       2. cm")
  print ("                                       3. inches")
  print ("                                       4. feets")
  unit_hip = int(input("     ● Unit For Hip: "))
  while unit_hip != 1 and unit_hip != 2 and unit_hip != 3 and unit_hip != 4:
    unit_hip = int(input("     ● Unit For Hip: "))
  if unit_hip == 1:
    hip1 = float(input("     ● Hip [m]: "))
    hip2 = float(hip1 * 100)
    hip3 = float(hip1 * 39.3701)
    hip4 = float(hip1 * 3.28084)
  elif unit_hip == 2:
    hip2 = float(input("     ● Hip [cm]: "))
    hip1 = float(hip2 / 100)
    hip3 = float(hip2 * 0.393701)
    hip4 = float(hip2 * 0.0328084)
  elif unit_hip == 3:
    hip3 = float(input("     ● Hip [inches]: "))
    hip1 = float(hip3 / 39.3701)
    hip2 = float(hip3 / 0.393701)
    hip4 = float(hip3 * 0.0833333)
  else:
    hip4 = float(input("     ● Hip [feets]: "))
    hip1 = float(hip4 / 3.28084)
    hip2 = float(hip4 / 0.0328084)
    hip3 = float(hip4 / 0.0833333)

  daily_exercise_duration = float(input("     ● Daily Exercise Duration [minutes]: "))
  
  print ("     Choose Activity Level: 1. Sedentary (Less / No Exercise)")
  print ("                                         2. Low Active (Exercise 30 - 60 minutes daily)")
  print ("                                         3. Active (Exercise > 60 minutes daily)")
  print ("                                         4. Very Active (Exercise > 120 minutes daily)")
  activity_level = int(input("     ● Activity Level: "))
  while activity_level != 1 and activity_level != 2 and activity_level != 3 and activity_level != 4:
    activity_level = int(input("     ● Acrivity Level: "))

  print ("     Choose Region: 1. Asia")
  print ("                               2. Africa")
  print ("                               3. Europe")
  print ("                               4. America")
  print ("                               5. Australia")
  region = int(input("     ● Region: "))
  while region != 1 and region != 2 and region != 3 and region != 4 and region != 5:
    region = int(input("     ● Region: "))
  
  print (" - "*46)
  print ("     Choose To Continue: 1. Restart")
  print ("                                       2. Report")
  print ("                                       3. Exit")
  con = int(input("     ● Your Choice: "))
  while con != 1 and con != 2 and con != 3:
    con = int(input("     ● Your Choice: "))

# Proses
  if gender == "M" or gender == "m":
    sex = str("Male")
  else:
    sex = str("Female")

  if range_age == 1:
    age = age1
    ran = str("month")
  else:
    age = age2
    ran = str("years old")

  if blood_type == "A" or blood_type == "a":
    blood = "A"
  elif blood_type == "B" or blood_type == "b":
    blood = "B"
  elif blood_type == "AB" or blood_type == "ab":
    blood = "AB"
  else:
    blood = "O"

  if activity_level == 1:
    activity = str("Sedentary (Less / No Exercise)")
    pa = 1
  elif activity_level == 2:
    activity = str("Low Active (Exercise 30 - 60 minutes daily)")
    pa = 1.4
  elif activity_level == 3:
    activity = str("Active (Exercise > 60 minutes daily)")
    pa = 1.6
  else:
    activity = str("Very Active (Exercise > 120 minutes daily)")
    pa = 1.9

  if region == 1:
    country = str("Asia")
  elif region == 2:
    country = str("Africa")
  elif region == 3:
    country = str("Europe")
  elif region == 4:
    country = str("America")
  else:
    country = str("Australia")

  # BMI
  if unit_weight == 1 and unit_height == 2:
    bmi = float((weight1 / height2 ** 2) * 10000)
  elif unit_weight == 2 and unit_height == 3:
    bmi = float((weight2 / height3 ** 2) * 703)
  else:
    bmi = float(weight1 / height1 ** 2)

  if range_age == 1:
    if age1 >= 0 and age1 < 1:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 11.3:
          bmi_classification = str("Underweight")
        elif bmi >= 11.3 and bmi < 14.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 14.8 and bmi < 15.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 11.5:
          bmi_classification = str("Underweight")
        elif bmi >= 11.5 and bmi < 14.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 14.7 and bmi < 15.5:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 1 and age1 < 2:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 12.6:
          bmi_classification = str("Underweight")
        elif bmi >= 12.6 and bmi < 16.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.4 and bmi < 17.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 12.4:
          bmi_classification = str("Underweight")
        elif bmi >= 12.4 and bmi < 16.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.1 and bmi < 17:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 2 and age1 < 3:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 13.8:
          bmi_classification = str("Underweight")
        elif bmi >= 13.8 and bmi < 17.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.8 and bmi < 18.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi <13.5:
          bmi_classification = str("Underweight")
        elif bmi >= 13.5 and bmi < 17.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.4 and bmi < 18.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 3 and age1 < 4:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.4:
          bmi_classification = str("Underweight")
        elif bmi >= 14.4 and bmi < 18.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.5 and bmi < 19.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi <14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 18:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18 and bmi < 19:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 4 and age1 < 5:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.7:
          bmi_classification = str("Underweight")
        elif bmi >= 14.7 and bmi < 18.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.7 and bmi < 19.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.3:
          bmi_classification = str("Underweight")
        elif bmi >= 14.3 and bmi < 18.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.3 and bmi < 19.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 5 and age1 < 6:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.8:
          bmi_classification = str("Underweight")
        elif bmi >= 14.8 and bmi < 18.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.9 and bmi < 19.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.5:
          bmi_classification = str("Underweight")
        elif bmi >= 14.5 and bmi < 18.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.5 and bmi < 19.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 6 and age1 < 7:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.9:
          bmi_classification = str("Underweight")
        elif bmi >= 14.9 and bmi < 18.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.9 and bmi < 19.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.6:
          bmi_classification = str("Underweight")
        elif bmi >= 14.6 and bmi < 18.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.6 and bmi < 19.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 7 and age1 < 8:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.9:
          bmi_classification = str("Underweight")
        elif bmi >= 14.9 and bmi < 18.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.9 and bmi < 19.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.3:
          bmi_classification = str("Underweight")
        elif bmi >= 14.3 and bmi < 18.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.6 and bmi < 19.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 8 and age < 9:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.9:
          bmi_classification = str("Underweight")
        elif bmi >= 14.9 and bmi < 18.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.8 and bmi < 19.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.3:
          bmi_classification = str("Underweight")
        elif bmi >= 14.3 and bmi < 18.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.5 and bmi < 19.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 9 and age1 < 10:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.8:
          bmi_classification = str("Underweight")
        elif bmi >= 14.8 and bmi < 18.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.7 and bmi < 19.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.2:
          bmi_classification = str("Underweight")
        elif bmi >= 14.2 and bmi < 18.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.4 and bmi < 19.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 10 and age1< 11:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.7:
          bmi_classification = str("Underweight")
        elif bmi >= 14.7 and bmi < 18.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.6 and bmi < 19.5:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14.1:
          bmi_classification = str("Underweight")
        elif bmi >= 14.1 and bmi < 18.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.2 and bmi < 19.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 11 and age1 < 12:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.6:
          bmi_classification = str("Underweight")
        elif bmi >= 14.6 and bmi < 18.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.4 and bmi < 19.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 18.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.1 and bmi < 19.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 12 and age1 < 13:
      if gender == "M" or gender == "m":
        ideal_weight = 7.8
        ideal_height = 0.68
        ideal_bmi = 16.87
        if bmi < 14.5:
          bmi_classification = str("Underweight")
        elif bmi >= 14.5 and bmi < 18.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.3 and bmi < 19.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 7.3
        ideal_height = 0.66
        ideal_bmi = 16.76
        if bmi < 13.9:
          bmi_classification = str("Underweight")
        elif bmi >= 13.9 and bmi < 17.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.9 and bmi < 19:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 13 and age1 < 14:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 14.4:
          bmi_classification = str("Underweight")
        elif bmi >= 14.4 and bmi < 18.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.1 and bmi < 19.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.8:
          bmi_classification = str("Underweight")
        elif bmi >= 13.8 and bmi < 17.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.8 and bmi < 18.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 14 and age1 < 15:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 14.3:
          bmi_classification = str("Underweight")
        elif bmi >= 14.3 and bmi < 18:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18 and bmi < 18.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 17.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.7 and bmi < 18.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 15 and age1 < 16:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 14.2:
          bmi_classification = str("Underweight")
        elif bmi >= 14.2 and bmi < 17.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.9 and bmi < 18.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 17.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.5 and bmi < 18.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 16 and age1 < 17:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 14.2:
          bmi_classification = str("Underweight")
        elif bmi >= 14.2 and bmi < 17.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.8 and bmi < 18.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.6:
          bmi_classification = str("Underweight")
        elif bmi >= 13.6 and bmi < 17.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.4 and bmi < 18.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 17 and age1 < 18:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 14.1:
          bmi_classification = str("Underweight")
        elif bmi >= 14.1 and bmi < 17.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.6 and bmi < 18.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.5:
          bmi_classification = str("Underweight")
        elif bmi >= 13.5 and bmi < 17.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.3 and bmi < 18.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 18 and age1 < 19:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 17.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.5 and bmi < 18.5:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.4:
          bmi_classification = str("Underweight")
        elif bmi >= 13.4 and bmi < 17.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.2 and bmi < 18.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 19 and age1 < 20:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 13.9:
          bmi_classification = str("Underweight")
        elif bmi >= 13.9 and bmi < 17.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.4 and bmi < 18.4:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.4:
          bmi_classification = str("Underweight")
        elif bmi >= 13.4 and bmi < 17.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.2 and bmi < 18.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 20 and age1 < 21:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 13.9:
          bmi_classification = str("Underweight")
        elif bmi >= 13.9 and bmi < 17.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.4 and bmi < 18.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.3:
          bmi_classification = str("Underweight")
        elif bmi >= 13.3 and bmi < 17.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.1 and bmi < 18.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 21 and age1 < 22:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 13.8:
          bmi_classification = str("Underweight")
        elif bmi >= 13.8 and bmi < 17.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.3 and bmi < 18.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.3:
          bmi_classification = str("Underweight")
        elif bmi >= 13.3 and bmi < 17:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17 and bmi < 18:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age1 >= 22 and age1 < 23:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 13.8:
          bmi_classification = str("Underweight")
        elif bmi >= 13.8 and bmi < 17.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.2 and bmi < 18.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.3:
          bmi_classification = str("Underweight")
        elif bmi >= 13.3 and bmi < 17:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17 and bmi < 17.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    else:
      if gender == "M" or gender == "m":
        ideal_weight = 12
        ideal_height = 0.84
        ideal_bmi = 17.01
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 17.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.1 and bmi < 18:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 11.2
        ideal_height = 0.83
        ideal_bmi = 16.26
        if bmi < 13.2:
          bmi_classification = str("Underweight")
        elif bmi >= 13.2 and bmi < 16.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.9 and bmi < 17.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
  else:
    if age2 >= 2 and age2 < 3:
      if gender == "M" or gender == "m":
        ideal_weight = 14.4
        ideal_height = 0.93
        ideal_bmi = 16.65
        if bmi < 14.5:
          bmi_classification = str("Underweight")
        elif bmi >= 14.5 and bmi < 18.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.1 and bmi < 19.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 13.7
        ideal_height = 0.92
        ideal_bmi = 16.19
        if bmi < 14.4:
          bmi_classification = str("Underweight")
        elif bmi >= 14.4 and bmi < 18:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18 and bmi < 19.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 3 and age2 < 4:
      if gender == "M" or gender == "m":
        ideal_weight = 16.5
        ideal_height = 1.01
        ideal_bmi = 16.17
        if bmi < 14.3:
          bmi_classification = str("Underweight")
        elif bmi >= 14.3 and bmi < 17.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.3 and bmi < 18.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 15.9
        ideal_height = 1
        ideal_bmi = 15.9
        if bmi < 14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 17.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 4 and age2 < 5:
      if gender == "M" or gender == "m":
        ideal_weight = 18.8
        ideal_height = 1.08
        ideal_bmi = 16.12
        if bmi < 14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 16.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.9 and bmi < 17.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 18.2
        ideal_height = 1.08
        ideal_bmi = 15.6
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 16.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.8 and bmi < 18:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 5 and age2 < 6:
      if gender == "M" or gender == "m":
        ideal_weight = 21
        ideal_height = 1.15
        ideal_bmi = 15.88
        if bmi < 13.8:
          bmi_classification = str("Underweight")
        elif bmi >= 13.8 and bmi < 16.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.8 and bmi < 17.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 20.6
        ideal_height = 1.14
        ideal_bmi = 15.85
        if bmi < 13.5:
          bmi_classification = str("Underweight")
        elif bmi >= 13.5 and bmi < 16.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 16.8 and bmi < 18.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 6 and age2 < 7:
      if gender == "M" or gender == "m":
        ideal_weight = 24
        ideal_height = 1.22
        ideal_bmi = 16.12
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 17:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17 and bmi < 18.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 23.3
        ideal_height = 1.22
        ideal_bmi = 15.65
        if bmi < 13.4:
          bmi_classification = str("Underweight")
        elif bmi >= 13.4 and bmi < 17.1:
          bmi_classification = str("Healthy Weigth")
        elif bmi >= 17.1 and bmi < 18.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 7 and age2 < 8:
      if gender == "M" or gender == "m":
        ideal_weight = 26.9
        ideal_height = 1.28
        ideal_bmi = 16.42
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 17.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.4 and bmi < 19.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 26.2
        ideal_height = 1.27
        ideal_bmi = 16.24
        if bmi < 13.4:
          bmi_classification = str("Underweight")
        elif bmi >= 13.4 and bmi < 17.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 17.6 and bmi < 19.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 8 and age2 < 9:
      if gender == "M" or gender == "m":
        ideal_weight = 30.4
        ideal_height =1.33 
        ideal_bmi = 17.19
        if bmi < 13.8:
          bmi_classification = str("Underweight")
        elif bmi >= 13.8 and bmi < 18:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18 and bmi < 20:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 29.5
        ideal_height = 1.32
        ideal_bmi = 16.93
        if bmi < 13.5:
          bmi_classification = str("Underweight")
        elif bmi >= 13.5 and bmi < 18.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.3 and bmi < 20.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 9 and age2 < 10:
      if gender == "M" or gender == "m":
        ideal_weight = 34.3
        ideal_height = 1.39
        ideal_bmi = 17.75
        if bmi < 14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 18.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 18.6 and bmi < 21:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 33.4
        ideal_height = 1.39
        ideal_bmi = 17.29
        if bmi < 13.7:
          bmi_classification = str("Underweight")
        elif bmi >= 13.7 and bmi < 19.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 19.2 and bmi < 21.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 10 and age2 < 11:
      if gender == "M" or gender == "m":
        ideal_weight = 37.9
        ideal_height = 1.44
        ideal_bmi = 18.28
        if bmi < 14.2:
          bmi_classification = str("Underweight")
        elif bmi >= 14.2 and bmi < 19.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 19.4 and bmi < 22.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 37.1
        ideal_height = 1.44
        ideal_bmi = 17.89
        if bmi < 14:
          bmi_classification = str("Underweight")
        elif bmi >= 14 and bmi < 20:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 20 and bmi < 23:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 11 and age2 < 12:
      if gender == "M" or gender == "m":
        ideal_weight = 42.7
        ideal_height = 1.5
        ideal_bmi = 18.98
        if bmi < 14.5:
          bmi_classification = str("Underweight")
        elif bmi >= 14.5 and bmi < 20.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 20.1 and bmi < 23.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 41.5
        ideal_height = 1.51
        ideal_bmi = 18.2
        if bmi < 14.4:
          bmi_classification = str("Underweight")
        elif bmi >= 14.4 and bmi < 20.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 20.9 and bmi < 24.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 12 and age2 < 13:
      if gender == "M" or gender == "m":
        ideal_weight = 47.6
        ideal_height = 1.56
        ideal_bmi = 19.56
        if bmi < 15:
          bmi_classification = str("Underweight")
        elif bmi >= 15 and bmi < 23:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 23 and bmi < 24.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 46.6
        ideal_height = 1.57
        ideal_bmi = 18.91
        if bmi < 14.9:
          bmi_classification = str("Underweight")
        elif bmi >= 14.9 and bmi < 21.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 21.7 and bmi < 25.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 13 and age2 < 14:
      if gender == "M" or gender == "m":
        ideal_weight = 53.9
        ideal_height = 1.64
        ideal_bmi = 20.04
        if bmi < 15.5:
          bmi_classification = str("Underweight")
        elif bmi >= 15.5 and bmi < 21.8:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 21.8 and bmi < 25.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 50.9
        ideal_height = 1.61
        ideal_bmi = 19.64
        if bmi < 15.3:
          bmi_classification = str("Underweight")
        elif bmi >= 15.3 and bmi < 22.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 22.5 and bmi < 26.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 14 and age2 < 15:
      if gender == "M" or gender == "m":
        ideal_weight = 60.1
        ideal_height = 1.71
        ideal_bmi = 20.55
        if bmi < 16:
          bmi_classification = str("Underweight")
        elif bmi >= 16 and bmi < 22.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 22.6 and bmi < 26:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 54.4
        ideal_height = 1.64
        ideal_bmi = 20.23
        if bmi < 15.8:
          bmi_classification = str("Underweight")
        elif bmi >= 15.8 and bmi < 21.3:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 21.3 and bmi < 27.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 15 and age2 < 16:
      if gender == "M" or gender == "m":
        ideal_weight = 65.3
        ideal_height = 1.75
        ideal_bmi = 21.32
        if bmi < 16.5:
          bmi_classification = str("Underweight")
        elif bmi >= 16.5 and bmi < 23.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 23.5 and bmi < 26.8:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 57.4
        ideal_height = 1.66
        ideal_bmi = 20.83
        if bmi < 16.3:
          bmi_classification = str("Underweight")
        elif bmi >= 16.3 and bmi < 24.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 24.1 and bmi < 28.1:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 16 and age2 < 17:
      if gender == "M" or gender == "m":
        ideal_weight = 70.7
        ideal_height = 1.79
        ideal_bmi = 22.07
        if bmi < 17.1:
          bmi_classification = str("Underweight")
        elif bmi >= 17.1 and bmi < 24.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 24.2 and bmi < 27.5:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 58.8
        ideal_height = 1.67
        ideal_bmi = 21.08
        if bmi < 16.8:
          bmi_classification = str("Underweight")
        elif bmi >= 16.8 and bmi < 24.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 24.7 and bmi < 28.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 17 and age2 < 18:
      if gender == "M" or gender == "m":
        ideal_weight = 73.2
        ideal_height = 1.8
        ideal_bmi = 22.59
        if bmi < 17.7:
          bmi_classification = str("Underweight")
        elif bmi >= 17.7 and bmi < 24.9:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 24.9 and bmi < 28.2:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 59.8
        ideal_height = 1.67
        ideal_bmi = 21.44
        if bmi < 17.2:
          bmi_classification = str("Underweight")
        elif bmi >= 17.2 and bmi < 25.2:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 25.2 and bmi < 29.6:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 18 and age2 < 19:
      if gender == "M" or gender == "m":
        ideal_weight = 75.8
        ideal_height = 1.81
        ideal_bmi = 23.14
        if bmi < 18.3:
          bmi_classification = str("Underweight")
        elif bmi >= 18.3 and bmi < 25.6:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 25.6 and bmi < 28.9:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 61.4
        ideal_height = 1.68
        ideal_bmi = 21.75
        if bmi < 17.5:
          bmi_classification = str("Underweight")
        elif bmi >= 17.5 and bmi < 25.7:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 25.7 and bmi < 30.3:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 19 and age2 < 20:
      if gender == "M" or gender == "m":
        ideal_weight = 75.8
        ideal_height = 1.81
        ideal_bmi = 23.14
        if bmi < 18.7:
          bmi_classification = str("Underweight")
        elif bmi >= 18.7 and bmi < 26.4:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 26.4 and bmi < 29.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 61.4
        ideal_height = 1.68
        ideal_bmi = 21.75
        if bmi < 17.7:
          bmi_classification = str("Underweight")
        elif bmi >= 17.7 and bmi < 26.1:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 26.1 and bmi < 31:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 20 and age2 < 21:
      if gender == "M" or gender == "m":
        ideal_weight = 79.2
        ideal_height = 1.81
        ideal_bmi = 24.18
        if bmi < 19.2:
          bmi_classification = str("Underweight")
        elif bmi >= 19.2 and bmi < 27:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 27 and bmi < 30.5:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        ideal_weight = 63
        ideal_height = 1.68
        ideal_bmi = 22.32
        if bmi < 17.8:
          bmi_classification = str("Underweight")
        elif bmi >= 17.8 and bmi < 26.5:
          bmi_classification = str("Healthy Weight")
        elif bmi >= 26.5 and bmi < 31.7:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
    elif age2 >= 21 and age2 < 65:
      if region == 1:
        if bmi < 18.5:
          bmi_classification = str("Underweight")
        elif bmi >= 18.5 and bmi < 23:
          bmi_classification = str("Normal")
        elif bmi >= 23 and bmi < 25:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      elif region == 2:
        if bmi < 18.5:
          bmi_classification = str("Underweight")
        elif bmi >= 18.5 and bmi < 23:
          bmi_classification = str("Normal Range")
        elif bmi >= 23 and bmi < 25:
          bmi_classification = str("Overweight")
        elif bmi >= 25 and bmi < 30:
          bmi_classification = str("Obese I")
        else:
          bmi_classification = str("Obese II")
      elif region == 3:
        if bmi < 18.5:
          bmi_classification = str("Underweight")
        elif bmi >= 18.5 and bmi < 25:
          bmi_classification = str("Normal Weight")
        elif bmi >= 25 and bmi < 30:
          bmi_classification = str("Pre-obesity")
        elif bmi >= 30 and bmi < 35:
          bmi_classification = str("Obesity Class I")
        elif bmi >= 35 and bmi < 40:
          bmi_classification = str("Obesity Class II")
        else:
          bmi_classification = str("Obesity Class III")
      elif region == 4:
        if bmi < 18.5:
          bmi_classification = str("Underweight")
        elif bmi >=18.5 and bmi < 25:
          bmi_classification = str("Healthy weight")
        elif bmi >= 25 and bmi < 30:
          bmi_classification = str("Overweight")
        else:
          bmi_classification = str("Obese")
      else:
        if bmi < 16:
          bmi_classification = str("Underweight (Severe Thinness)")
        elif bmi >= 16 and bmi < 17:
          bmi_classification = str("Underweight (Moderate Thinness)")
        elif bmi >= 17 and bmi < 18.5:
          bmi_classification = str("Underweight (Mild Thinness)")
        elif bmi >= 18.5 and bmi < 25:
          bmi_classification = str("Normal Range")
        elif bmi >= 25 and bmi < 30:
          bmi_classification = str("Overweight")
        elif bmi >= 30 and bmi < 35:
          bmi_classification = str("Obese Class I")
        elif bmi >= 35 and bmi < 40:
          bmi_classification = str("Obese Class II")
        else:
          bmi_classification = str("Obese Class III")
    else:
      if bmi < 24:
        bmi_classification = str("Underweight")
      elif bmi >= 24 and bmi < 30:
        bmi_classification = str("Healthy Weight")
      else:
        bmi_classification = str("Overweight")

  if range_age == 2:
    if age2 >= 21 and age2 < 25:
      if gender == "M" or gender == "m":
        ideal_weight = 79.2
        ideal_height = 1.81
        ideal_bmi = 24.18
      else:
        ideal_weight = 63
        ideal_height = 1.68
        ideal_bmi = 22.32
    elif age2 >= 25 and age2 < 30:
      if gender == "M" or gender == "m":
        ideal_weight = 82.5
        ideal_height = 1.81
        ideal_bmi = 25.18
      else:
        ideal_weight = 65.4
        ideal_height = 1.67
        ideal_bmi = 23.45
    elif age2 >= 30 and age2 < 35:
      if gender == "M" or gender == "m":
        ideal_weight = 84.4
        ideal_height = 1.8
        ideal_bmi = 26.05
      else:
        ideal_weight = 67
        ideal_height = 1.67
        ideal_bmi = 24.02
    elif age2 >= 35 and age2 < 40:
      if gender == "M" or gender == "m":
        ideal_weight = 85.9
        ideal_height = 1.8
        ideal_bmi = 26.51
      else:
        ideal_weight = 67.9
        ideal_height = 1.67
        ideal_bmi = 24.35
    elif age2 >= 40 and age2 < 45:
      if gender == "M" or gender == "m":
        ideal_weight = 87.3
        ideal_height = 1.8
        ideal_bmi = 26.94
      else:
        ideal_weight = 68.7
        ideal_height = 1.67
        ideal_bmi = 24.63
    elif age2 >= 45 and age2 < 50:
      if gender == "M" or gender == "m":
        ideal_weight = 87.6
        ideal_height = 1.8
        ideal_bmi = 27.04
      else:
        ideal_weight = 69.4
        ideal_height = 1.67
        ideal_bmi = 24.88
    elif age2 >= 50 and age2 < 55:
      if gender == "M" or gender == "m":
        ideal_weight = 87.8
        ideal_height = 1.79
        ideal_bmi = 27.4
      else:
        ideal_weight = 70.1
        ideal_height = 1.67
        ideal_bmi = 25.14
    elif age2 >= 55 and age2 < 60:
      if gender == "M" or gender == "m":
        ideal_weight = 87.7
        ideal_height = 1.79
        ideal_bmi = 27.37
      else:
        ideal_weight = 70.4
        ideal_height = 1.66
        ideal_bmi = 25.55
    elif age2 >= 60 and age2 < 65:
      if gender == "M" or gender == "m":
        ideal_weight = 87.3
        ideal_height = 1.78
        ideal_bmi = 27.55
      else:
        ideal_weight = 70.9
        ideal_height = 1.65
        ideal_bmi = 26.04
    elif age2 >= 65 and age2 < 70:
      if gender == "M" or gender == "m":
        ideal_weight = 86.5
        ideal_height = 1.76
        ideal_bmi = 27.92
      else:
        ideal_weight = 71.3
        ideal_height = 1.64
        ideal_bmi = 26.51
    elif age2 >= 70 and age2 < 75:
      if gender == "M" or gender == "m":
        ideal_weight = 84.8
        ideal_height = 1.76
        ideal_bmi = 27.38
      else:
        ideal_weight = 70.6
        ideal_height = 1.64
        ideal_bmi = 26.25
    else:
      if gender == "M" or gender == "m":
        ideal_weight = 81.2
        ideal_height = 1.74
        ideal_bmi = 26.82
      else:
        ideal_weight = 68.5
        ideal_height = 1.62
        ideal_bmi = 26.1

  #BFP
  if range_age == 1:
    if gender == "M" or gender == "m":
      bfp = (1.51 * bmi) - (0.7 * (age1 / 12)) - 2.2
    else:
      bfp = (1.51 * bmi) - (0.7 * (age1 / 12)) + 1.4
  elif range_age == 2:
    if age2 <= 15:
      if gender == "M" or gender == "m":
        bfp = (1.51 * bmi) - (0.7 * (age2)) - 2.2
      else:
        bfp = (1.51 * bmi) - (0.7 * (age2)) + 1.4
    else:
      if gender == "M" or gender == "m":
        bfp = (1.20 * bmi) + (0.23 * age2) - 16.2
      else:
        bfp = (1.20 * bmi) + (0.23 * age2) - 5.4

  if range_age == 1:
    if gender == "M" or gender == "m":
      if bfp < 8:
        bfp_classification = str("Underfat")
      elif bfp >= 8 and bfp < 14:
        bfp_classification = str("Healthy")
      elif bfp >= 14 and bfp < 21:
        bfp_classification = str("Overfat")
      else:
        bfp_classification = str("Obese")
    else:
      if bfp < 18:
        bfp_classification = str("Underfat")
      elif bfp >= 18 and bfp < 23:
        bfp_classification = str("Healthy")
      elif bfp >= 23 and bfp < 30:
        bfp_classification = str("Overfat")
      else:
        bfp_classification = str("Obese")
  else:
    if age2 < 5:
      if gender == "M" or gender == "m":
        if bfp < 8:
          bfp_classification = str("Underfat")
        elif bfp >= 8 and bfp < 14:
          bfp_classification = str("Healthy")
        elif bfp >= 14 and bfp < 21:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 18:
          bfp_classification = str("Underfat")
        elif bfp >= 18 and bfp < 23:
          bfp_classification = str("Healthy")
        elif bfp >= 23 and bfp < 30:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 5 and age2 < 6:
      if gender == "M" or gender == "m":
        if bfp < 13:
          bfp_classification = str("Underfat")
        elif bfp >= 13 and bfp < 20:
          bfp_classification = str("Healthy")
        elif bfp >= 20 and bfp < 24:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 15:
          bfp_classification = str("Underfat")
        elif bfp >= 15 and bfp < 23:
          bfp_classification = str("Healthy")
        elif bfp >= 23 and bfp < 27:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 6 and age2 < 7:
      if gender == "M" or gender == "m":
        if bfp < 13:
          bfp_classification = str("Underfat")
        elif bfp >= 13 and bfp < 21:
          bfp_classification = str("Healthy")
        elif bfp >= 21 and bfp < 25:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 15:
          bfp_classification = str("Underfat")
        elif bfp >= 15 and bfp < 24:
          bfp_classification = str("Healthy")
        elif bfp >= 24 and bfp < 28:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 7 and age2 < 8:
      if gender == "M" or gender == "m":
        if bfp < 14:
          bfp_classification = str("Underfat")
        elif bfp >= 14 and bfp < 21:
          bfp_classification = str("Healthy")
        elif bfp >= 21 and bfp < 26:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 16:
          bfp_classification = str("Underfat")
        elif bfp >= 16 and bfp < 26:
          bfp_classification = str("Healthy")
        elif bfp >= 26 and bfp < 30:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 8 and age2 < 9:
      if gender == "M" or gender == "m":
        if bfp < 14:
          bfp_classification = str("Underfat")
        elif bfp >= 14 and bfp < 22:
          bfp_classification = str("Healthy")
        elif bfp >= 22 and bfp < 27:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 16:
          bfp_classification = str("Underfat")
        elif bfp >= 16 and bfp < 27:
          bfp_classification = str("Healthy")
        elif bfp >= 27 and bfp < 31:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 9 and age2 < 10:
      if gender == "M" or gender == "m":
        if bfp < 14:
          bfp_classification = str("Underfat")
        elif bfp >= 14 and bfp < 23:
          bfp_classification = str("Healthy")
        elif bfp >= 23 and bfp < 28:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 28:
          bfp_classification = str("Healthy")
        elif bfp >= 28 and bfp < 32:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 10 and age2 < 11:
      if gender == "M" or gender == "m":
        if bfp < 14:
          bfp_classification = str("Underfat")
        elif bfp >= 14 and bfp < 24:
          bfp_classification = str("Healthy")
        elif bfp >= 24 and bfp < 29:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 29:
          bfp_classification = str("Healthy")
        elif bfp >= 29 and bfp < 33:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 11 and age2 < 12:
      if gender == "M" or gender == "m":
        if bfp < 14:
          bfp_classification = str("Underfat")
        elif bfp >= 14 and bfp < 24:
          bfp_classification = str("Healthy")
        elif bfp >= 24 and bfp < 29:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 30:
          bfp_classification = str("Healthy")
        elif bfp >= 30 and bfp < 34:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 12 and age2 < 13:
      if gender == "M" or gender == "m":
        if bfp < 13:
          bfp_classification = str("Underfat")
        elif bfp >= 13 and bfp < 24:
          bfp_classification = str("Healthy")
        elif bfp >= 24 and bfp < 29:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 30:
          bfp_classification = str("Healthy")
        elif bfp >= 30 and bfp < 34:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 13 and age2 < 14:
      if gender == "M" or gender == "m":
        if bfp < 13:
          bfp_classification = str("Underfat")
        elif bfp >= 13 and bfp < 23:
          bfp_classification = str("Healthy")
        elif bfp >= 23 and bfp < 28:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 30:
          bfp_classification = str("Healthy")
        elif bfp >= 30 and bfp < 34:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 14 and age2 < 15:
      if gender == "M" or gender == "m":
        if bfp < 12:
          bfp_classification = str("Underfat")
        elif bfp >= 12 and bfp < 22:
          bfp_classification = str("Healthy")
        elif bfp >= 22 and bfp < 27:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 31:
          bfp_classification = str("Healthy")
        elif bfp >= 31 and bfp < 35:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 15 and age2 < 16:
      if gender == "M" or gender == "m":
        if bfp < 11:
          bfp_classification = str("Underfat")
        elif bfp >= 11 and bfp < 22:
          bfp_classification = str("Healthy")
        elif bfp >= 22 and bfp < 26:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 31:
          bfp_classification = str("Healthy")
        elif bfp >= 31 and bfp < 35:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 16 and age2 < 17:
      if gender == "M" or gender == "m":
        if bfp < 11:
          bfp_classification = str("Underfat")
        elif bfp >= 11 and bfp < 21:
          bfp_classification = str("Healthy")
        elif bfp >= 21 and bfp < 25:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 31:
          bfp_classification = str("Healthy")
        elif bfp >= 31 and bfp < 35:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 17 and age2 < 18:
      if gender == "M" or gender == "m":
        if bfp < 11:
          bfp_classification = str("Underfat")
        elif bfp >= 11 and bfp < 21:
          bfp_classification = str("Healthy")
        elif bfp >= 21 and bfp < 25:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 17:
          bfp_classification = str("Underfat")
        elif bfp >= 17 and bfp < 31:
          bfp_classification = str("Healthy")
        elif bfp >= 31 and bfp < 36:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 18 and age2 < 19:
      if gender == "M" or gender == "m":
        if bfp < 11:
          bfp_classification = str("Underfat")
        elif bfp >= 11 and bfp < 21:
          bfp_classification = str("Healthy")
        elif bfp >= 21 and bfp < 25:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 18:
          bfp_classification = str("Underfat")
        elif bfp >= 18 and bfp < 32:
          bfp_classification = str("Healthy")
        elif bfp >= 32 and bfp < 36:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 19 and age2 < 21:
      if gender == "M" or gender == "m":
        if bfp < 4:
          bfp_classification = str("Underfat")
        elif bfp >= 4 and bfp < 12.6:
          bfp_classification = str("Healthy")
        elif bfp >= 12.6 and bfp < 19:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 15.8:
          bfp_classification = str("Underfat")
        elif bfp >= 15.8 and bfp < 21.6:
          bfp_classification = str("Healthy")
        elif bfp >= 21.6 and bfp < 30:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 21 and age2 < 26:
      if gender == "M" or gender == "m":
        if bfp < 5:
          bfp_classification = str("Underfat")
        elif bfp >= 5 and bfp < 13.7:
          bfp_classification = str("Healthy")
        elif bfp >= 13.7 and bfp < 21.3:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 18.5:
          bfp_classification = str("Underfat")
        elif bfp >= 18.5 and bfp < 23.9:
          bfp_classification = str("Healthy")
        elif bfp >= 23.9 and bfp < 29.7:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 26 and age2 < 31:
      if gender == "M" or gender == "m":
        if bfp < 8.5:
          bfp_classification = str("Underfat")
        elif bfp >= 8.5 and bfp < 16.5:
          bfp_classification = str("Healthy")
        elif bfp >= 16.5 and bfp < 22.4:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 19.1:
          bfp_classification = str("Underfat")
        elif bfp >= 19.1 and bfp < 24.6:
          bfp_classification = str("Healthy")
        elif bfp >= 214.6 and bfp < 31.6:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 31 and age2 < 36:
      if gender == "M" or gender == "m":
        if bfp < 9.5:
          bfp_classification = str("Underfat")
        elif bfp >= 9.5 and bfp < 17.6:
          bfp_classification = str("Healthy")
        elif bfp >= 17.6 and bfp < 23.5:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 19.7:
          bfp_classification = str("Underfat")
        elif bfp >= 19.7 and bfp < 25.2:
          bfp_classification = str("Healthy")
        elif bfp >= 25.2 and bfp < 32.2:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 36 and age2 < 41:
      if gender == "M" or gender == "m":
        if bfp < 10.6:
          bfp_classification = str("Underfat")
        elif bfp >= 10.6 and bfp < 18.7:
          bfp_classification = str("Healthy")
        elif bfp >= 18.7 and bfp < 24.5:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 22.3:
          bfp_classification = str("Underfat")
        elif bfp >= 22.3 and bfp < 27.4:
          bfp_classification = str("Healthy")
        elif bfp >= 27.4 and bfp < 32.8:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 41 and age2 < 46:
      if gender == "M" or gender == "m":
        if bfp < 13.9:
          bfp_classification = str("Underfat")
        elif bfp >= 13.9 and bfp < 21.4:
          bfp_classification = str("Healthy")
        elif bfp >= 21.4 and bfp < 26.7:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 22.9:
          bfp_classification = str("Underfat")
        elif bfp >= 22.9 and bfp < 28:
          bfp_classification = str("Healthy")
        elif bfp >= 28 and bfp < 34.5:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 46 and age2 < 51:
      if gender == "M" or gender == "m":
        if bfp < 14.9:
          bfp_classification = str("Underfat")
        elif bfp >= 14.9 and bfp < 22.5:
          bfp_classification = str("Healthy")
        elif bfp >= 22.5 and bfp < 27.8:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 23.5:
          bfp_classification = str("Underfat")
        elif bfp >= 23.5 and bfp < 28.7:
          bfp_classification = str("Healthy")
        elif bfp >= 28.7 and bfp < 35.1:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 51 and age2 < 56:
      if gender == "M" or gender == "m":
        if bfp < 16:
          bfp_classification = str("Underfat")
        elif bfp >= 16 and bfp < 23.5:
          bfp_classification = str("Healthy")
        elif bfp >= 23.5 and bfp < 28.8:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 24.1:
          bfp_classification = str("Underfat")
        elif bfp >= 24.1 and bfp < 29.3:
          bfp_classification = str("Healthy")
        elif bfp >= 29.3 and bfp < 35.7:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    elif age2 >= 56 and age2 < 60:
      if gender == "M" or gender == "m":
        if bfp < 17.1:
          bfp_classification = str("Underfat")
        elif bfp >= 17.1 and bfp < 24.6:
          bfp_classification = str("Healthy")
        elif bfp >= 24.6 and bfp < 30.9:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 24.7:
          bfp_classification = str("Underfat")
        elif bfp >= 24.7 and bfp < 29.9:
          bfp_classification = str("Healthy")
        elif bfp >= 29.9 and bfp < 37.3:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
    else:
      if gender == "M" or gender == "m":
        if bfp < 13:
          bfp_classification = str("Underfat")
        elif bfp >= 13 and bfp < 25:
          bfp_classification = str("Healthy")
        elif bfp >= 25 and bfp < 31:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")
      else:
        if bfp < 24:
          bfp_classification = str("Underfat")
        elif bfp >= 24 and bfp < 36:
          bfp_classification = str("Healthy")
        elif bfp >= 36 and bfp < 43:
          bfp_classification = str("Overfat")
        else:
          bfp_classification = str("Obese")

  if range_age == 1:
    if gender == "M" or gender == "m":
      ideal_bfp = str("Less Than 7%")
    else:
      ideal_bfp = str("Less Than 16%")
  else:
    if age2 < 20:
      if gender == "M" or gender == "m":
        ideal_bfp = str("Less Than 7%")
      else:
        ideal_bfp = str("Less Than 16%")
    elif age2 >= 20 and age2 < 30:
      if gender == "M" or gender == "m":
        ideal_bfp = str("7% - 17%")
      else:
        ideal_bfp = str("16% - 24%")
    elif age2 >= 30 and age2 < 40:
      if gender == "M" or gender == "m":
        ideal_bfp = str("12% - 21%")
      else:
        ideal_bfp = str("17% - 25%")
    elif age2 >= 40 and age2 < 50:
      if gender == "M" or gender == "m":
        ideal_bfp = str("14% - 23%")
      else:
        ideal_bfp = str("19% - 28%")
    elif age2 >= 50 and age2 < 60:
      if gender == "M" or gender == "m":
        ideal_bfp = str("16% - 24%")
      else:
        ideal_bfp = str("22% - 31%")
    elif age2 >= 60 and age2 < 70:
      if gender == "M" or gender == "m":
        ideal_bfp = str("17% - 25%")
      else:
        ideal_bfp = str("22% - 33%")
    else:
      if gender == "M" or gender == "m":
        ideal_bfp = str("More Than 25%")
      else:
        ideal_bfp = str("More Than 33%")

  #WHR
  whr = waist2 / hip2

  if gender == "M" or gender == "m":
    ideal_whr = 0.8
    if whr < 0.96:
      whr_classification = str("Low")
    elif whr >= 0.96 and whr < 1:
      whr_classification = str("Moderate")
    else:
      whr_classification = str("High")
  else:
    ideal_whr = 0.7
    if whr < 0.81:
      whr_classification = str("Low")
    elif whr >= 0.81 and whr < 0.84:
      whr_classification = str("Moderate")
    else:
      whr_classification = str("High")

  #WHtR
  whtr = waist2 / height2

  if range_age == 1:
    if whtr < 0.35:
      whtr_classification = str("Extremely Slim")
    elif whtr >= 0.35 and whtr < 0.46:
      whtr_classification = str("Slim")
    elif whtr >= 0.46 and whtr < 0.52:
      whtr_classification = str("Healthy")
    elif whtr >= 0.52 and whtr < 0.64:
      whtr_classification = str("Overweight")
    else:
      whtr_classification = str("Obese")
  else:
    if age2 < 16:
      if whtr < 0.35:
        whtr_classification = str("Extremely Slim")
      elif whtr >= 0.35 and whtr < 0.46:
        whtr_classification = str("Slim")
      elif whtr >= 0.46 and whtr < 0.52:
        whtr_classification = str("Healthy")
      elif whtr >= 0.52 and whtr < 0.64:
        whtr_classification = str("Overweight")
      else:
        whtr_classification = str("Obese")
    else:
      if gender == "M" or gender == "m":
        if whtr < 0.35:
          whtr_classification = str("Extremely Slim")
        elif whtr >= 0.35 and whtr < 0.43:
          whtr_classification = str("Slim")
        elif whtr >= 0.43 and whtr < 0.53:
          whtr_classification = str("Healthy")
        elif whtr >= 0.53 and whtr < 0.58:
          whtr_classification = str("Overweight")
        elif whtr >= 0.58 and whtr < 0.63:
          whtr_classification = str("Very Overweight")
        else:
          whtr_classification = str("Obese")
      else:
        if whtr < 0.35:
          whtr_classification = str("Extremely Slim")
        elif whtr >= 0.35 and whtr < 0.42:
          whtr_classification = str("Slim")
        elif whtr >= 0.42 and whtr < 0.49:
          whtr_classification = str("Healthy")
        elif whtr >= 0.49 and whtr < 0.54:
          whtr_classification = str("Overweight")
        elif whtr >= 0.54 and whtr < 0.58:
          whtr_classification = str("Very Overweight")
        else:
          whtr_classification = str("Obese")

  #EER
  if range_age == 1:
    if age1 < 4:
      eer = (89 * weight1 - 100) + 175
    elif age1 >= 4 and age1 < 6:
      eer = (89 * weight1 - 100) + 56
    elif age1 >= 7 and age1 < 12:
      eer = (89 * weight1 - 100) + 22
    else:
      eer = (89 * weight1 - 100) + 20
  else:
    if age2 < 3:
      eer = (89 * weight1 - 100) + 20
    elif age2 >= 3 and age2 < 9:
      if gender == "M" or gender == "m":
        eer = 88.5 - (61.9 * age2) + pa * ((26.7 * weight1) + (903 * height1)) + 20
      else:
        eer = 135.3 - (30.8 * age2) + pa * ((10 * weight1) + (934 * height1)) + 20
    elif age2 >= 9 and age2 < 19:
      if gender == "M" or gender == "m":
        eer = 88.5 - (61.9 * age2) + pa * ((26.7 * weight1) + (903 * height1)) + 25
      else:
        eer = 135.3 - (30.8 * age2) + pa * ((10 * weight1) + (934 * height1)) + 25
    elif age2 >= 19 :
      if gender == "M" or gender == "m":
        if bmi_classification == "Obese" or bmi_classification == "Obese I" or bmi_classification == "Obese II" or bmi_classification == "Obesity Class I" or bmi_classification == "Obesity Class II" or bmi_classification == "Obesity Class III" or bmi_classification == "Obese Class I" or bmi_classification == "Obese Class II" or bmi_classification == "Obese Class III":
          eer = 114 - (50.9 * age2) + pa * ((19.5 * weight1) + (1161.4 * height1))
        else:
          eer = 662 - (9.53 * age2) + pa * ((15.91 * weight1) + (539.6 * height1))
      else:
        if bmi_classification == "Obese" or bmi_classification == "Obese I" or bmi_classification == "Obese II" or bmi_classification == "Obesity Class I" or bmi_classification == "Obesity Class II" or bmi_classification == "Obesity Class III" or bmi_classification == "Obese Class I" or bmi_classification == "Obese Class II" or bmi_classification == "Obese Class III":
          eer = 389 - (41.2 * age2) + pa * ((15 * weight1) + (701.6 * height1))
        else:
          eer = 354 - (6.91 * age2) + pa * ((9.36 * weight1) + (726 * height1))

  #BMR
  if range_age == 1:
    if gender == "M" or gender == "m":
      bmr = (10 * weight1) + (6.25 * height2 ) - (5 * age1) + 5
    else:
      bmr = (10 * weight1) + (6.25 * height2 ) - (5 * age1) - 161
  else:
    if gender == "M" or gender == "m":
      bmr = (10 * weight1) + (6.25 * height2 ) - (5 * age2) + 5
    else:
      bmr = (10 * weight1) + (6.25 * height2 ) - (5 * age2) - 161

  #DCR
  dcr = bmr * pa

  #MN
  macronutrients_carb = dcr * 0.3 / 4
  macronutrients_protein = dcr * 0.4 / 4
  macronutrients_fat = dcr * 0.3 / 9

  #WATER
  water1 = (weight2 * 2 / 3) + (daily_exercise_duration / 30 * 12)
  water2 = water1 * 0.0295735
  water3 = water1 * 0.125
  
  #BS
  if gender == "M" or gender == "m":
    if shoulder3 < waist3 and shoulder3 < hip3:
      bs = str("Triangle")
    elif shoulder3 > waist3 and shoulder3 > hip3:
      bs = str("Inverterd Triangle")
    elif shoulder3 == waist3 and shoulder3 == hip3:
      bs = str("Rectangle")
    elif  waist3 > shoulder3 and waist3 > hip3:
      bs = str("Oval")
    elif shoulder3 > waist3 and waist3 == hip3:
      bs = str("Trapezoid")
    else:
      bs = str("None")
  else:
    if (bust3 - hip3) <= 1 and (hip3 - bust3) < 3.6 and (bust3 - waist3) >= 9 or (hip3 - waist3) >= 10:
      bs = str("Hourglass")
    elif (hip3 - bust3) >= 3.6 and (hip3 - bust3) < 10 and (hip3 - waist3) >= 9 and (high_hip3 / waist3) < 1.193:
      bs = str("Bottom Hourglass")
    elif (bust3 - hip3) > 1 and (bust3 - hip3) < 10 and (bust3 - waist3) >= 9:
      bs = str("Top Hourglass")
    elif (hip3 - bust3) > 2 and (hip3 - waist3) >= 7 and (high_hip3 - waist3) >= 1.193:
      bs = str("Spoon")
    elif (hip3 - bust3) >= 3.6 and (hip3 - waist3) < 9:
      bs = str("Triangle")
    elif (bust3 - hip3) >= 3.6 and (bust3 - waist3) < 9:
      bs = str("Inverted Triangle")
    elif (hip3 - bust3) < 3.6 and (bust3 - hip3) < 3.6 and (bust3 - waist3) < 9 and (hip3 - waist3) < 10:
      bs = str("Rectangle")
    else:
      bs = str("None")

# Output
if con == 2:
  print (" - "*46)
  report = str("                      HEALTH REPORT")
  print (" ".join(report))
  import datetime
  x = datetime.datetime.now()
  print (str("\n                                         ~"), (x.strftime("%c ~")))
  print (" - "*46)

  import time
  from time import sleep
  time.sleep (0.3)
  print ("     ● Name:", name)
  
  import time
  from time import sleep
  time.sleep (0.3)
  print ("     ● IC:", ic)
  
  import time
  from time import sleep
  time.sleep (0.3)
  print ("     ● Gender:", sex)
  
  import time
  from time import sleep
  time.sleep (0.3)
  print ("     ● Age:", round(age,2), ran)
  
  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Blood Type:", blood)
  
  if blood == "A":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Higher Risk Of Disease: ")
    print ("        ▪ Microbial Infection")
    print ("        ▪ Fertility")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Eat: ")
    print ("        ▪ Soy protein (Tofu)")
    print ("        ▪ Grains (Spelt, hulled barley, and sprouted bread)")
    print ("        ▪ Walnuts, pumpkin seeds, and peanuts")
    print ("        ▪ Olive oil")
    print ("        ▪ Fruits (Blueberries and elderberries)")
    print ("        ▪ Certain kinds of beans and legumes")
    print ("        ▪ Vegetables (Kale, Swiss chard, and spinach)")
    print ("        ▪ Garlic and onions")
    print ("        ▪ Cold-water fish (Sardines and salmon)")
    print ("        ▪ Limited amounts of chicken and turkey")
    print ("        ▪ Green tea")
    print ("        ▪ Ginger")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Avoid: ")
    print ("        ▪ Beef")
    print ("        ▪ Pork")
    print ("        ▪ Lamb")
    print ("        ▪ Cow’s milk")
    print ("        ▪ Potatoes, yams, and sweet potatoes")
    print ("        ▪ Vegetables (Cabbage, eggplant, tomatoes, peppers, and mushrooms)")
    print ("        ▪ Lima beans")
    print ("        ▪ Fruits (Melons, oranges, strawberries, and mangos)")
    print ("        ▪ Duck")
    print ("        ▪ Venison")
    print ("        ▪ Fish (Bluefish, barracuda, haddock, herring, and catfish)")
    print ("        ▪ Grains and grain products (Wheat bran, multigrain bread, and durum wheat)")
    print ("        ▪ Refined sugar")
    print ("        ▪ Refined carbohydrates (White flour and white bread)")
    print ("        ▪ Oils other than olive oil")
    print ("        ▪ Artificial ingredients")
    print ("        ▪ Most condiments")
  elif blood == "B":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Higher Risk Of Disease: ")
    print ("        ▪ Pancreatic Cancer")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Eat: ")
    print ("        ▪ Lamb")
    print ("        ▪ Goat")
    print ("        ▪ Rabbit")
    print ("        ▪ Mutton")
    print ("        ▪ Vension")
    print ("        ▪ Green vegetables")
    print ("        ▪ Eggs")
    print ("        ▪ Low-fat dairy")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Avoid: ")
    print ("        ▪ Wheat")
    print ("        ▪ Buckwheat")
    print ("        ▪ Corn")
    print ("        ▪ Lentils")
    print ("        ▪ Peanuts")
    print ("        ▪ Sesame seeds")
    print ("        ▪ Tomatoes")
    print ("        ▪ Chicken")
  elif blood == "AB":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Higher Risk Of Disease: ")
    print ("        ▪ Pancreatic cancer")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Eat: ")
    print ("        ▪ Tofu")
    print ("        ▪ Seafood")
    print ("        ▪ Dairy")
    print ("        ▪ Green vegetables")
    print ("        ▪ Fish (Mahi-mahi, red snapper, salmon, sardines and tuna)")
    print ("        ▪ Dairy (Yogurt and kefir)")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Avoid: ")
    print ("        ▪ Caffeine")
    print ("        ▪ Alcohol")
    print ("        ▪ Smoked or cured meats")
  else:
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Higher Risk Of Disease: ")
    print ("        ▪ Stomach Uclers")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Lower Risk Of Disease: ")
    print ("        ▪ Heart Disease")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Eat: ")
    print ("        ▪ Meat")
    print ("        ▪ Fish")
    print ("        ▪ Vegetables")
    print ("        ▪ Fruits")
    print ("        ▪ Olive oil")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Food To Avoid: ")
    print ("        ▪ Wheat")
    print ("        ▪ Corn")
    print ("        ▪ Legumes")
    print ("        ▪ Kidney beans")
    print ("        ▪ Dairy")
    print ("        ▪ Caffeine")
    print ("        ▪ Alcohol")
    
  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Weight [kg]:", round(weight1,2), "kg")
  print ("     ● Weight [pounds]:", round(weight2,2), "pounds")
  print ("     ● Weight [stones]:", round(weight3,2), "stones")
  print ("     ● Ideal Weight:", ideal_weight)

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Height [m]:", round(height1,2), "m")
  print ("     ● Height [cm]:", round(height2,2), "cm")
  print ("     ● Height [inches]:", round(height3,2), "inches")
  print ("     ● Height [feets]:", round(height4,2), "feets")
  print ("     ● Ideal Height:", ideal_height)

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Shoulder [m]:", round(shoulder1,2), "m")
  print ("     ● Shoulder [cm]:", round(shoulder2,2), "cm")
  print ("     ● Shoulder [inches]:", round(shoulder3,2), "inches")
  print ("     ● Shoulder [feets]:", round(shoulder4,2), "feets")

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Bust [m]:" , round(bust1,2), "m")
  print ("     ● Bust [cm]:", round(bust2,2), "cm")
  print ("     ● Bust [inches]:", round(bust3,2), "inches")
  print ("     ● Bust [feets]:" , round(bust4,2), "feets")

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Waist [m]:", round(waist1,2), "m")
  print ("     ● Waist [cm]:", round(waist2,2), "cm")
  print ("     ● Waist [inches]:", round(waist3,2), "inches")
  print ("     ● Waist [feets]:", round(waist4,2), "feets")

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● High Hip [m]:", round(high_hip1,2), "m")
  print ("     ● High Hip [cm]:", round(high_hip2,2), "cm")
  print ("     ● High Hip [inches]:", round(high_hip3,2), "inches")
  print ("     ● High Hip [feets]:", round(high_hip4,2), "feets")

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Daily Exercise Duration:", round(daily_exercise_duration,2), "minutes")
  print ("\n     ● Activity Level:", activity)
  print ("\n     ● Region:", country)

  import time
  from time import sleep
  time.sleep (0.3)
  print ("\n     ● Body Mass Index (BMI):", round(bmi,2))
  print ("     ● Body Mass Index (BMI) Classification:", bmi_classification)
  print ("     ● Ideal Body Mass Index (BMI):", ideal_bmi)
  if bmi_classification == "Underweight" or bmi_classification == "Underweight (Severe Thinness)" or bmi_classification == "Underweight (Moderate Thinness)" or bmi_classification == "Underweight (Mild Thinness)":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Effects Of Being", bmi_classification, ": ")
    print ("        ▪ Malnutrition")
    print ("        ▪ Decreased immune function")
    print ("        ▪ Osteoporosis")
    print ("        ▪ Increase of surgical complications")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Treatments Of", bmi_classification, ": ")
    print ("        ▪ Drink 6-8 glasses of distilled water a day.")
    print ("        ▪ Eat frequent but small meals.")
    print ("        ▪ Eat lots of raw fruits and vegetables (Green leafy vegetables).")
    print ("        ▪ Do not drink coffee, alcohol and soda pop.")
    print ("        ▪ Do not eat processed foods and white sugar.")
    print ("        ▪ Avoid eating red meat and animal fats.")
    print ("        ▪ Reduce intake of dairy products.")
    print ("        ▪ Do not smoke and avoid second hand smoke.")
  elif bmi_classification == "Healthy Weight" or bmi_classification == "Normal" or bmi_classification == "Normal Range"  or bmi_classification == "Normal Weight":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Benefits Of Being", bmi_classification, ": ")
    print ("        ▪ Associated with living longest.")
    print ("        ▪ Lowest incidence of serious illness.")
    print ("        ▪ More physically attractive.")
  elif bmi_classification == "Overweight" or bmi_classification == "Pre-obesity":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Diseases Causes By", bmi_classification, ": ")
    print ("        ▪ Blood Pressure")
    print ("        ▪ Diabetes")
    print ("        ▪ Heart Disease")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Treatments Of", bmi_classification, ": ")
    print ("        ▪ Eliminate red meat.")
    print ("        ▪ Cut out fried food.")
    print ("        ▪ Start with a soup or a salad.")
    print ("        ▪ Stop Cola consumption.")
    print ("        ▪ Drink water.")
  elif bmi_classification == "Obese" or bmi_classification == "Obese I" or bmi_classification == "Obese II" or bmi_classification == "Obesity Class I" or bmi_classification == "Obesity Class II" or bmi_classification == "Obesity Class III" or bmi_classification == "Obese Class I" or bmi_classification == "Obese Class II" or bmi_classification == "Obese Class III":
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Diseases Causes By", bmi_classification, ": ")
    print ("        ▪ Heart Disease")
    print ("        ▪ Diabetes")
    print ("        ▪ High Blood Pressure")
    print ("        ▪ Gall Bladder Disease")
    print ("        ▪ Cancer")
    print ("        ▪ Infertility")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Effects Of Being", bmi_classification, ": ")
    print ("        ▪ Less sleep")
    print ("        ▪ Reduce life expectancy")
    import time
    from time import sleep
    time.sleep (0.3)
    print ("     □ Treatments Of ", bmi_classification, ": ")
    print ("        ▪ Slow and steady weight loss of not more than 1-2 pounds per week.")
    print ("        ▪ Do at least 30 minutes of physical activity a day on most days of the week.")
    print ("        ▪ Eat pasta, rice, wholemeal bread and other whole-grain food.")
    print ("        ▪ Reduce fat-intake")
    print ("        ▪ Eat lots of fruits and vegetables.")

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Body Fat Percentage (BFP):", round(bfp,2))
  print ("     ● Body Fat Percentage (BFP) Classification:", bfp_classification)
  print ("     ● Ideal Body Fat Percentage (BFP):", ideal_bfp)

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Waist-hip Ratio (WHR):", round(whr,2))
  print ("     ● Risk Of Having Heart Disease:", whr_classification)
  print ("     ● Ideal Waist-hip Ratio (WHR):", ideal_whr)

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Waist-to-height Ratio (WHtR):", round(whtr,2))
  print ("     ● Waist-to-height Ratio (WHtR) Classification:", whtr_classification)

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Estimated Energy Requirement (EER):", round(eer,2), "kcal/day")

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Basal Metabolic Rate (BMR):", round(bmr,2), "calories/day")
  print ("     ● Daily Calorie Requirement (DCR):", round(dcr,2), "calories/day")

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Daily Macronutrients Intake Requirement: ")
  print ("        ▪ Carbohydrate:", round(macronutrients_carb,2), "g")
  print ("        ▪ Protein:", round(macronutrients_protein,2), "g")
  print ("        ▪ Fat:", round(macronutrients_fat,2), "g")

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Daily Water Intake Requirement:")
  print ("        ▪", round(water1,2), "ounces")
  print ("        ▪", round(water2,2), "litres")
  print ("        ▪", round(water3,2), "cups")

  import time
  from time import sleep
  time.sleep (0.2)
  print ("\n     ● Body Shape (BS):", bs)
  if gender == "M" or gender == "m":
    if bs == "Triangle":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Osteoporosis")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Higher-protein Food")
      print ("        ▪ Lean meats")
      print ("        ▪ Leafy greens")
      print ("        ▪ Healthy fats")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Any food that has more than 3g of added sugar")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Running")
      print ("        ▪ Power walking")
      print ("        ▪ Strength training")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Tailored patterned blazers")
      print ("        ▪ Vertical stripes")
      print ("        ▪ Jackets with structured shoulders")
      print ("        ▪ Single-breasted suits")
      print ("        ▪ Brighter color panels")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Fitted polo shirts and roll necks")
      print ("        ▪ Brighter colors and busy prints")
      print ("        ▪ Bold belts")
      print ("        ▪ Skinny fits and extreme tapers")
    elif bs == "Inverted Triangle":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Gall Bladder Disease")
      print ("        ▪ Blood Pressure")
      print ("        ▪ Stroke")
      print ("        ▪ Coronary Heart Disease")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ High-end protein")
      print ("        ▪ Fresh fruits and vegetables")
      print ("        ▪ Dairy products")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Under cooked meats")
      print ("        ▪ Starch")
      print ("        ▪ Full fat")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Squatting")
      print ("        ▪ Lunging")
      print ("        ▪ Deadlifts")
      print ("        ▪ Twisting type exercises")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Horizontal stripes")
      print ("        ▪ Slim-fit shirts")
      print ("        ▪ Slim cotton polo shirt")
      print ("        ▪ Regular V-neck T-shirts")
      print ("        ▪ Straight-leg trousers and jeans")
      print ("        ▪ Trousers with larger seat drop")
      print ("        ▪ Jackets")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Structured tailoring")
      print ("        ▪ Prints, patterns and scoop necklines")
      print ("        ▪ Plunging V-neck t-shirts")
    elif bs == "Rectangle":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Obesity")
      print ("        ▪ Malfunction of kidneys, liver and heart")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Protein rich diet")
      print ("        ▪ Poached eggs, chicken breasts and Greek Yogurt")
      print ("        ▪ Rolled Oats, walnuts and green salad")
      print ("        ▪ Almond, peanuts and Ground Flax Seed powder")
      print ("        ▪ Chicken, turkey, beef and tuna")
      print ("        ▪ Tempeh, beans, low-fat cheese and Quinoa")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ White rice")
      print ("        ▪ Fast foods")
      print ("        ▪ Tinned foods")
      print ("        ▪ Fries")
      print ("        ▪ Beverages")
      print ("        ▪ Alcohol")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Upper/Lower abdominal crunches")
      print ("        ▪ Push-ups")
      print ("        ▪ Sit-ups")
      print ("        ▪ Cardio exercises")
      print ("        ▪ Squat")
      print ("        ▪ Leg press")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Horizontal stripes")
      print ("        ▪ Structured tailoring")
      print ("        ▪ Layered looks")
      print ("        ▪ Scarves")
      print ("        ▪ Prints, color pops, and detailing")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Double-breasted jackets")
    elif  bs == "Oval":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Cardiovascular disease")
      print ("        ▪ Type-2 diabetes")
      print ("        ▪ Blood pressure")
      print ("        ▪ Breast cancer")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Nuts, salmon and mackerel")
      print ("        ▪ High quantity of carbohydrates")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Sweets")
      print ("        ▪ Ice creams")
      print ("        ▪ Fruit juices")
      print ("        ▪ White flour baked products (Cakes, crackers, pasta, sweet carbonated drinks, syrups and honey)")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Plank")
      print ("        ▪ Swimming")
      print ("        ▪ Jogging")
      print ("        ▪ Cycling")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Trousers")
      print ("        ▪ Suspenders")
      print ("        ▪ Pleats")
      print ("        ▪ Shirts")
      print ("        ▪ Jackets")
      print ("        ▪ Neckties")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Tight fits in the torso")
      print ("        ▪ Patterns and visual clutter")
    elif bs == "Trapezoid":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Protein rich diet")
      print ("        ▪ Poached eggs, chicken breasts, and Greek Yogurt")
      print ("        ▪ Rolled Oats, walnuts and green salad")
      print ("        ▪ Almond, peanuts and Ground Flax Seed powder")
      print ("        ▪ Chicken, turkey, beef and tuna")
      print ("        ▪ Tempeh, beans, low-fat cheese and Quinoa")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ White rice")
      print ("        ▪ Fast foods")
      print ("        ▪ Tinned foods")
      print ("        ▪ Fries")
      print ("        ▪ Beverages")
      print ("        ▪ Alcohol")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Plank")
      print ("        ▪ Swimming")
      print ("        ▪ Jogging")
      print ("        ▪ Cycling")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Trousers")
      print ("        ▪ Shirts")
      print ("        ▪ Jackets")
      print ("        ▪ Neckties")
    else:
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     ● Your body shape is unable to classify within the five male body shapes.")
  else:
    if bs == "Hourglass":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Heart disease")
      print ("        ▪ Type-2 diabetes")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Vegetables")
      print ("        ▪ Fruits")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Food high in glycemic index")
      print ("        ▪ Food containing high saturated fat")
      print ("        ▪ Too much whole milk dairy")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Prone Plank")
      print ("        ▪ Shoulder cycles")
      print ("        ▪ Single leg stretch")
      print ("        ▪ Squats")
      print ("        ▪ Walking lunges")
      print ("        ▪ One leg deadlifts")
      print ("        ▪ Leg press")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Broad belts")
      print ("        ▪ Flowy dresses")
      print ("        ▪ Well-fitting tops")
      print ("        ▪ Fitting jackets")
      print ("        ▪ Tops or dresses with pleated waist")
      print ("        ▪ Pencil skirts")
      print ("        ▪ Jeggings")
      print ("        ▪ Boots")
      print ("        ▪ Strappy sandals")
      print ("        ▪ High heels")
      print ("        ▪ Peep toes")
      print ("        ▪ Necklaces")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Shapeless and loose tops and dresses")
      print ("        ▪ Gaudy embellishments")
    elif bs == "Bottom Hourglass":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Cardiovascular diseases")
      print ("        ▪ Type-2 diabetes")
      print ("        ▪ Elevated blood pressure")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Monounsaturated and omega-3 fats")
      print ("        ▪ Food rich in protein and fibre")
      print ("        ▪ Food low in carbohydrates")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Snacks")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Swimming")
      print ("        ▪ Cycling")
      print ("        ▪ Jogging")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Square neck, V-neck, and U-neck tops or shirts")
      print ("        ▪ Wrap around tops, skirts, and jackets")
      print ("        ▪ Vertical stripes")
      print ("        ▪ Peplum tops")
      print ("        ▪ Tunic tops")
      print ("        ▪ Belted dresses and tops")
      print ("        ▪ Wide collared jackets")
      print ("        ▪ Fish-cut or flared skirts")
      print ("        ▪ Cargo pants with pockets near your hip")
      print ("        ▪ Empire waisted dresses or tops")
      print ("        ▪ High heels")
      print ("        ▪ Long and slender earrings and necklaces")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Tapered jeans or trousers")
      print ("        ▪ Loose fitting tops")
      print ("        ▪ Wide stripes")
      print ("        ▪ Ruffles")
      print ("        ▪ Pleated skirts")
      print ("        ▪ Baggy jackets")
      print ("        ▪ Tight t-shirts")
      print ("        ▪ High necks")
      print ("        ▪ Turtle necks")
      print ("        ▪ Cardigans")
      print ("        ▪ Chunky earrings and necklaces")
      print ("        ▪ Round toed shoes")
      print ("        ▪ Heavy boots")
      print ("        ▪ Flats")
    elif bs == "Top Hourglass":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Osteoporosis")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Quinoa")
      print ("        ▪ Barley")
      print ("        ▪ Brown rice")
      print ("        ▪ Lentils")
      print ("        ▪ Beans")
      print ("        ▪ Sweet potatoes")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Coconut oil")
      print ("        ▪ Cheese")
      print ("        ▪ Butter")
      print ("        ▪ Canola oil")
      print ("        ▪ Vegetable oils")
      print ("        ▪ Seed oils")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Swimming")
      print ("        ▪ Cycling")
      print ("        ▪ Jogging")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Clothes and tops that have V-necks that are narrow")
      print ("        ▪ Dark colored tops")
      print ("        ▪ A couple of jackets")
      print ("        ▪ Well-tailored shirts")
      print ("        ▪ Skirts")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Baggy jeans")
      print ("        ▪ Jackets")
      print ("        ▪ Loose fitting clothes")
      print ("        ▪ Boxy shirts")
      print ("        ▪ Stiff clothes")
      print ("        ▪ Square necks")
      print ("        ▪ Boat necks")
      print ("        ▪ Frills")
      print ("        ▪ Ruffles near your bust line")
      print ("        ▪ Wide striped skirts or trouser")
    elif bs == "Spoon":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Osteoporosis")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Higher-protein Food")
      print ("        ▪ Lean meats")
      print ("        ▪ Leafy greens")
      print ("        ▪ Healthy fats")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Any food that has more than 3g of added sugar")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Running")
      print ("        ▪ Power walking")
      print ("        ▪ Strength training")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Lighter color in the upper body region but darker in the middle and lower body region")
      print ("        ▪ Strapless")
      print ("        ▪ Boat necks")
      print ("        ▪ Wide necks")
      print ("        ▪ Short skirts")
      print ("        ▪ A-line skirts")
      print ("        ▪ Boot cut jeans or trousers")
      print ("        ▪ Mid-rise jeans")
      print ("        ▪ Padded bras")
      print ("        ▪ Chunky earrings and necklaces")
      print ("        ▪ Well-defined shouldered jackets, dresses, and tops")
      print ("        ▪ Well fitted dresses around the waist")
      print ("        ▪ Bags that come till your hip bone")
      print ("        ▪ Peep-toes")
      print ("        ▪ Flats")
      print ("        ▪ Ballerina shoes with pointed toes")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Tapered ankle trouser or jeans")
      print ("        ▪ Tops with a tie just below your bust line")
      print ("        ▪ Shapeless shirts")
      print ("        ▪ Short sleeves with round neck tops")
      print ("        ▪ Dresses that are overly ruffled or pleated below your bust")
      print ("        ▪ Wide stripes near your mid-body region")
      print ("        ▪ Narrow shouldered tops")
      print ("        ▪ Shorts or skirts that end just below your hips")
      print ("        ▪ Rounded toes shoes")
      print ("        ▪ strappy sandals")
    elif bs == "Triangle":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Osteoporosis")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Higher-protein Food")
      print ("        ▪ Lean meats")
      print ("        ▪ Leafy greens")
      print ("        ▪ Healthy fats")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Any food that has more than 3g of added sugar")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Running")
      print ("        ▪ Power walking")
      print ("        ▪ Strength training")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Bright and beautiful scoop-neck and boat-neck tops")
      print ("        ▪ Gorgeous bracelets and accessories")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Balloon dresses")
      print ("        ▪ Cigarette pants")
      print ("        ▪ Tight skirts")
    elif bs == "Inverted Triangle":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Osteoporosis")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ Quinoa")
      print ("        ▪ Barley")
      print ("        ▪ Brown rice")
      print ("        ▪ Lentils")
      print ("        ▪ Beans")
      print ("        ▪ Sweet potatoes")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Coconut oil")
      print ("        ▪ Cheese")
      print ("        ▪ Butter")
      print ("        ▪ Canola oil")
      print ("        ▪ Vegetable oils")
      print ("        ▪ Seed oils")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ Swimming")
      print ("        ▪ Cycling")
      print ("        ▪ Jogging")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Ruffles around the neck")
      print ("        ▪ Peplum tops")
      print ("        ▪ Jeans with back pockets")
      print ("        ▪ Low waist jeans")
      print ("        ▪ Checks and stripes in slanting angle")
      print ("        ▪ Front pockets in skirts")
      print ("        ▪ Satin dresses")
      print ("        ▪ V-necks")
      print ("        ▪ A-line dresses and skirts")
      print ("        ▪ Fish cuts")
      print ("        ▪ Shorts")
      print ("        ▪ Chunky shoes and earrings")
      print ("        ▪ Slender necklace")
      print ("        ▪ Long dresses")
      print ("        ▪ High-waist pants")
      print ("        ▪ Bell bottoms")
      print ("        ▪ Sequined skirts")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Baggy jeans")
      print ("        ▪ Jackets")
      print ("        ▪ Loose fitting clothes")
      print ("        ▪ Boxy shirts")
      print ("        ▪ Stiff clothes")
      print ("        ▪ Square necks")
      print ("        ▪ Boat necks")
      print ("        ▪ Frills")
      print ("        ▪ Ruffles near your bust line")
      print ("        ▪ Wide striped skirts or trouser")
    elif bs == "Rectangle":
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Higher Risk Of Disease: ")
      print ("        ▪ Osteoporosis")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Eat: ")
      print ("        ▪ All unprocessed food")
      print ("        ▪ Whole food")
      print ("        ▪ High in fiber")
      print ("        ▪ Fruits and vegetables")
      print ("        ▪ Lean protein")
      print ("        ▪ Low in saturated fats and sugars")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Food To Avoid: ")
      print ("        ▪ Protein powders")
      print ("        ▪ Shakes")
      print ("        ▪ Large slabs of meat")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ Recommended Exercise: ")
      print ("        ▪ 30 minutes of moderate intensity exercise 3-5 times per week")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What To Wear: ")
      print ("        ▪ Tube tops or dresses")
      print ("        ▪ A nice and snazzy belt")
      print ("        ▪ Bright colors")
      print ("        ▪ Different textures, and cuts")
      import time
      from time import sleep
      time.sleep (0.3)
      print ("     □ What Not To Wear: ")
      print ("        ▪ Clothes that highlight your waist")
      print ("        ▪ Rigid and shapeless clothes")
    else:
      print ("     ● Your body shape is unable to classify within the seven female body shapes.")

    import time
    from time import sleep
    time.sleep (0.3)
    print (" - "*46)
    ending = str("             THE GREATEST WEALTH IS HEALTH")
    print (" ".join(ending))
    tq = str("\n               >>>>>>>>THANK YOU>>>>>>>>")
    print (" ".join(tq))
    print (" - "*46)

if con == 3:
  import time
  from time import sleep
  time.sleep (0.3)
  print (" - "*46)
  ending = str("             THE GREATEST WEALTH IS HEALTH")
  print (" ".join(ending))
  tq = str("\n               >>>>>>>>THANK YOU>>>>>>>>")
  print (" ".join(tq))
  print (" - "*46)
