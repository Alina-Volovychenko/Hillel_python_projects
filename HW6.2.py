seconds = int(input("Введите количество секунд (0 - 8639999): "))

days, rem = divmod(seconds, 86400)
hours, rem = divmod(rem, 3600)
minutes, sec = divmod(rem, 60)

if 11 <= days % 100 <= 14:
    day_word = "дней"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дня"
else:
    day_word = "дней"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}")