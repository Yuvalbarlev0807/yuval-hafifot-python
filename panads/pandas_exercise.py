import pandas as pd
from io import StringIO

csv_data = """
city,date,pm25,pm10,temperature
Tel Aviv,2025-11-27,22,40,28
Jerusalem,2025-11-27,18,35,24
Haifa,2025-11-27,30,50,26
Tel Aviv,2025-11-28,26,45,29
Jerusalem,2025-11-28,28,48,23
Haifa,2025-11-28,35,60,25
"""

csv_lack_data = """
city,date,pm25,pm10,temperature
Tel Aviv,2025-11-27,22,40,28
Jerusalem,2025-11-27,,35,24
Haifa,2025-11-27,30,,26
Tel Aviv,2025-11-28,26,45,
"""

# StringIO הופך את המחרוזת ל-"קובץ" שפנדס יודעת לקרוא
data_file = StringIO(csv_data)
data_missing_values_file = StringIO(csv_lack_data)
# כאן את אמורה להשתמש ב-pandas כדי לקרוא את הנתונים
df = pd.read_csv(data_file)
df3 = pd.read_csv(data_missing_values_file)

all_tables = df  # הדפסת כל הטבלה
top_3_tables = df.head(3)  # הדפסת 3 השורות הראשונות בטבלה
all_columns = df.columns  # הדספת שמות העמודות
columns_type = df.dtypes  # הדפסת סוג הנתונים בכל עמודה
avg_p25_column = df["pm25"].mean()  # ממוצע של הערכים בעמודה ספציפית
data_where_bigger_then25 = df[df["pm25"] > 25]  # בחירת הערכים שהערך PM25 גדול מ 25
df["bad_air"] = df["pm25"] > 25  # הוספת עמודה שמציגה האם האוויר טוב או לא ע"פ תנאי
avg_p25_by_city = df.groupby("city")["pm25"].mean()  # הצגת ממוצע הערך עבור כל עיר
avg_p10_by_city = df.groupby("city")["pm10"].mean()
both_avg = df.groupby("city")[["pm25", "pm10"]].mean()
df["date"] = pd.to_datetime(df["date"])  # המרת הזמנים
# print(df["date"])

df.to_csv("air_quality.csv", index=False)  # לשמור לקובץ
df2 = pd.read_csv("air_quality.csv")  # לקרוא מקובץ
# print(df2)

missing = df3.isna().sum() # כמה ערכים חסרים בכל עמודה
delete = df3.dropna() # מחיקת שורות שחסר בהן מידע - מחזיר רק את מה שלא חסר בו
print(delete)
