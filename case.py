#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv('StudentsPerformance .csv')
# print(df.head())

print('Девочки набирают большее количество баллов в гуманитарных тестах, а мальчики в математических тестах')
print('')

female_math = df[df['gender'] == 'female']['math score'].mean()
female_read = df[df['gender'] == 'female']['reading score'].mean()
female_write = df[df['gender'] == 'female']['writing score'].mean()
male_math = df[df['gender'] == 'male']['math score'].mean()
male_read = df[df['gender'] == 'male']['reading score'].mean()
male_write = df[df['gender'] == 'male']['writing score'].mean()

print('Результаты девочек:', 'Математика:', round(female_math, 2), 'Чтение:', round(female_read, 2), 'Письмо:', round(female_write, 2))
print('Результаты мальчиков:', 'Математика:', round(male_math, 2), 'Чтение:', round(male_read, 2), 'Письмо:', round(male_write, 2))
print('')

print('Гипотеза подтверждена. Девочки набрали болеше баллов в гуманитарных тестах чем мальчики.')
print('')

print('Если образование с окончанием колледжа, то результаты будут высокими')
print('')

bachelors_degree_m = df[df['parental level of education'] == "bachelor's degree"]['math score'].mean()
bachelors_degree_r = df[df['parental level of education'] == "bachelor's degree"]['reading score'].mean()
bachelors_degree_w = df[df['parental level of education'] == "bachelor's degree"]['writing score'].mean()
bachelors = bachelors_degree_m + bachelors_degree_r + bachelors_degree_w
print('Образование - Бакалавариат:', round(bachelors, 2))

masters_degree_m = df[df['parental level of education'] == "master's degree"]['math score'].mean()
masters_degree_r = df[df['parental level of education'] == "master's degree"]['reading score'].mean()
masters_degree_w = df[df['parental level of education'] == "master's degree"]['writing score'].mean()
masters = masters_degree_m + masters_degree_r + masters_degree_w
print('Образование - Магистр:', round(masters, 2))

associates_degree_m = df[df['parental level of education'] == "associate's degree"]['math score'].mean()
associates_degree_r = df[df['parental level of education'] == "associate's degree"]['reading score'].mean()
associates_degree_w = df[df['parental level of education'] == "associate's degree"]['writing score'].mean()
associates = associates_degree_m + associates_degree_r + associates_degree_w
print('Образование - Степень младшего специалиста:', round(associates, 2))

college_m = df[df['parental level of education'] == "some college"]['math score'].mean()
college_r = df[df['parental level of education'] == "some college"]['reading score'].mean()
college_w = df[df['parental level of education'] == "some college"]['writing score'].mean()
college = college_m + college_r + college_w
print('Образование - Колледж:', round(college, 2))

high_school_m = df[df['parental level of education'] == "high school"]['math score'].mean()
high_school_r = df[df['parental level of education'] == "high school"]['reading score'].mean()
high_school_w = df[df['parental level of education'] == "high school"]['writing score'].mean()
high = high_school_m + high_school_r + high_school_w
print('Образование - Высшая школа:', round(high, 2))
print('')

print('Гипотеза опровержена. Больше всего баллов набирают со степенью магистра, а наименишие баллы у высшей школы.')

g = pd.Series(data = [female_math, female_read, female_write, male_math, male_read, male_write],
index = ['Математика девочки', "Чтение девочки", "Письмо девочки", "Математика мальчики", "Чтение мальчики", "Писльмо мальчики"])
g.plot(kind = 'barh', figsize = (15, 7), grid = True)
plt.show()

s = pd.Series(data = [bachelors, masters, associates, college, high],
index = ["Бакалавр", "Магистр", 'Специалист', "Колледж", "Старшая школа"])
s.plot(kind = 'barh', figsize = (10, 5), grid = True)
plt.show()

lunch = df['lunch'].value_counts()
lunch.plot(kind = 'pie')
plt.show()

preparetion = df['test preparation course'].value_counts()
preparetion.plot(kind = 'pie')
plt.show()

education = df['parental level of education'].value_counts()
education.plot(kind = 'pie')
plt.show()



