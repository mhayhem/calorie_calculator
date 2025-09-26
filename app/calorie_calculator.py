# @Author Danile Grande (Mhayhem)


def calorie_expenditure(gender: str, weigth: int, heigth: int, age: int) -> int:
    """calculated caloric expenditure

    Args:
        gender (str): user gender
        weigth (int): user weigth
        heigth (int): user heigth
        age (int): user age

    Returns:
        int: total calorie needed
    """
    match gender:
        case "male":
            result = int((weigth * 10) + (heigth * 6.25) - (age * 5) + 5)
        case "femele":
            result = int((weigth * 10) + (heigth * 6.25) - (age * 5) - 161)
    
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
    weigth = int(input("Peso: kg\n"))
    heigth = int(input("Altura: cm\n"))
    age = int(input("Edad: \n"))
    gender = input("Genero: [M]asculino, [F]emenino\n").lower()
    if gender == "m":
        gender = "male"
    else:
        gender = "femele"
        
    return gender, weigth, heigth, age

def get_level_activity() -> str:
    """collet activity info

    Returns:
        str: user activity
    """
    print("¿cual es su nivel de actividad?")
    activty = int(input("1. Ninguna.\n"
                        "2. Trabajo parcial.\n"
                        "3. Trabajo completo.\n"
                        "4. Trabajo y ejercicio.\n"))
    match activty:
        case 1:
            activty = "nothing"
        case 2:
            activty = "llow"
        case 3:
            activty = "medium"
        case 4:
            activty = "higth"
        case _:
            print("No es una opción valida.")
            get_level_activity()
    
    return activty

def get_rest_calorie() -> int:
    """collet user-selected deficit

    Returns:
        int: user deficit
    """
    print("Calórias para ajustar tu gasto calorico:")
    print("(Se recomienda un déficit de entre 350 a 500 calorias diarias)")
    rest_calorie = int(input("Déficit calórico:\n"))
    
    return rest_calorie

def display_info_and_calorie(gender: str, weigth: int, heigth: int, age: int, total_calorie: int) -> str:
    """display info and result

    Args:
        gender (str): user info
        weigth (int): user info
        heigth (int): user info
        age (int): user info
        total_calorie (int): user info

    Returns:
        str: user info and result deficit formula
    """
    return f"Género: {gender}\nPeso: {weigth}\nAltura: {heigth}\nEdad: {age}\nCalórias diarias: {total_calorie}"

def main() -> str:
    gender, weigth, heigth, age  = get_info()
    result = calorie_expenditure(gender, weigth, heigth, age)
    activity = get_level_activity()
    level = level_activity(activity)
    rest_calorie = get_rest_calorie()
    total_calorie = deficit_calories(rest_calorie, level, result)
    print(display_info_and_calorie(gender, weigth, heigth, age, total_calorie))

if __name__ == "__main__":
    main()