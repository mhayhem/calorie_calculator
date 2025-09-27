# @Author Danile Grande (Mhayhem)


def calorie_expenditure(gender: str, weight: int, height: int, age: int) -> int:
    """calculated caloric expenditure

    Args:
        gender (str): user gender
        weight (int): user weight
        height (int): user height
        age (int): user age

    Returns:
        int: total calorie needed
    """
    match gender:
        case "male":
            result = int((weight * 10) + (height * 6.25) - (age * 5) + 5)
        case "female":
            result = int((weight * 10) + (height * 6.25) - (age * 5) - 161)
    
    return result

def level_activity(activity: str) -> int:
    """get level activity user

    Args:
        activity (str): activity user

    Returns:
        int: activity user
    """
    incrase_activity = {
        "nothing": 1.2,
        "low": 1.37,
        "medium": 1.55,
        "higth": 1.75
    }
    
    if activity in incrase_activity:
        level = incrase_activity[activity]
        
        return level

def deficit_calories(rest_calorie: int, level: float, result: int) -> int:
    """calorie deficit formula

    Args:
        rest_calorie (int): user-selected deficit
        level (float): user activity
        result (int): user calorie needed

    Returns:
        int: calories you should per day
    """
    total_calorie = int((result * level) - rest_calorie)
    
    return total_calorie

def get_info():
    """collect user information to calculate their calorie deficit

    Returns:
        variables with information
    """
    print("Datos necesarios: peso, altura, edad y genero")
    weight = int(input("Peso: kg\n"))
    height = int(input("Altura: cm\n"))
    age = int(input("Edad: \n"))
    gender = input("Genero: [M]asculino, [F]emenino\n").lower()
    if gender == "m":
        gender = "male"
    else:
        gender = "female"
        
    return gender, weight, height, age

def body_fat_percentage(weight: int, height: int, age: int, gender: str) -> float:
    """calculated user %BF with Deurenberg formula
    

    Args:
        weight (int): user info
        height (int): user info
        age (int): user info
        gender (str): user info

    Returns:
        float: user %BF
    """
    match gender:
        case "male":
            sex = 1
        case "female":
            sex = 0
    height /= 100
    imc = weight / height**2
    body_fat = (1.2 * imc) + (0.23 * age) - (10.8 * sex) - 5.4
    
    return body_fat

def get_level_activity() -> str:
    """collect activity info

    Returns:
        str: user activity
    """
    print("¿cual es su nivel de actividad?")
    activty = int(input("1. Ninguna.\n"
                        "2.  Poca.\n"
                        "3.  Media.\n"
                        "4.  Alta.\n"))
    match activty:
        case 1:
            activty = "nothing"
        case 2:
            activty = "low"
        case 3:
            activty = "medium"
        case 4:
            activty = "higth"
        case _:
            print("No es una opción valida.")
            get_level_activity()
    
    return activty

def get_rest_calorie() -> int:
    """collect user-selected deficit

    Returns:
        int: user deficit
    """
    print("Calórias para ajustar tu gasto calorico:")
    print("(Se recomienda un déficit de entre 350 a 500 calorias diarias)")
    rest_calorie = int(input("Déficit calórico:\n"))
    
    return rest_calorie

def display_info_and_calorie(gender: str, weight: int, height: int, age: int, total_calorie: int, imc: float) -> str:
    """display info and result

    Args:
        gender (str): user info
        weight (int): user info
        height (int): user info
        age (int): user info
        total_calorie (int): user info
        imc (float): user info

    Returns:
        str: user info and result deficit formula
    """
    return f"Género: {gender}\nIMC: {imc:.2f} %\nPeso: {weight} kg\nAltura: {height} cm\nEdad: {age} años\nCalórias diarias: {total_calorie} kcal"

def main() -> str:
    gender, weight, height, age  = get_info()
    result = calorie_expenditure(gender, weight, height, age)
    activity = get_level_activity()
    level = level_activity(activity)
    rest_calorie = get_rest_calorie()
    total_calorie = deficit_calories(rest_calorie, level, result)
    body_fat = body_fat_percentage(weight, height, age, gender)
    print(display_info_and_calorie(gender, weight, height, age, total_calorie, body_fat))

if __name__ == "__main__":
    main()

