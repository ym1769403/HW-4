#Yasir Mushtaque
#1769403
def get_age():
    age = int(input())
    if age < 18 or age >75:
            raise ValueError("Invalid age.")
    return age

def fat_burning_heart_rate(age):
    heart_rate =(220- age)*.70
    return heart_rate

if __name__ == "__main__":
    try:
        age = get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,fat_burning_heart_rate(age)))
    except ValueError as error:
        print(error)
        print('Could not calculate heart rate info.\n')
