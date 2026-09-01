import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("students.csv")
print(data.head())


print(data.describe())


data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)
print(data[['Name', 'Average']])


plt.bar(data['Name'], data['Average'], color='skyblue')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()


plt.plot(data['Name'], data['Maths'], marker='o', label='Maths')
plt.plot(data['Name'], data['Science'], marker='o', label='Science')
plt.plot(data['Name'], data['English'], marker='o', label='English')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Subject-wise Performance")
plt.legend()
plt.show()


plt.hist(data['Maths'], bins=5, color='green', alpha=0.7)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Maths Marks")
plt.show()


plt.pie(data['Average'], labels=data['Name'], autopct='%1.1f%%', startangle=90)
plt.title("Share of Average Marks by Student")
plt.show()


data.to_csv("students_cleaned.csv", index=False)