import pandas as pd

# לקחתי את הקובץ מידע הקיים ועשיתי עליו פעולות כמו : הוספת עמודה, חישוב ממוצעים, המרת שדה זמן וכו .. ולבסוף שמירת המידע לאותו הקובץ

df = pd.read_csv("air_quality.csv")  # לקרוא מקובץ
df["date"] = pd.to_datetime(df["date"])  # המרת הזמנים
df["day_of_the_week"] = df["date"].dt.day_name()
avg_p25_column = df["pm25"].mean()
avg_day_of_the_week = df.groupby("day_of_the_week")["pm25"].mean()
print(df)
print(avg_day_of_the_week)
df.to_csv("air_quality.csv", index=False)