# @Author Danile Grande (Mhayhem)

from enum import Enum

# Enums
class Gender(Enum):
    Hombre = 1
    Mujer = 2

class ActivityLevel(Enum):
    # Levels of physical activity with their multipliers
    NOTHING = (1, 1.2)
    LOW = (2, 1.37)
    MEDIUM = (3, 1.55)
    HIGH = (4, 1.75)
    
    def __init__(self, level_id: int, multiplier: float):
        self.level_id = level_id
        self.multiplier = multiplier
    
    @classmethod
    def from_id(cls, level_id: int):
        # obtain activity level
        for level in cls:
            if level.level_id == level_id:
                return level
        return None

class User:
    def __init__(self, name: str, gender: int, age: int, height: float, weight: float):
        self.name = name.capitalize()
        self.gender = Gender(gender)
        self.age = age
        self.height = height # cm
        self.weight = weight # kg

    def __str__(self):
        return f"Nombre: {self.name}; Edad: {self.age}; Genero: {self.gender.name}; Peso: {self.weight} kg; Altura: {self.height} cm."

# metrics calculator

class BodyMetricsCalculator:
    # Responsible for calculating body metrics
    @staticmethod
    def calculated_bmi(self, weight: float,  height_cm: float) -> float:
        # Calculate you body mass index
        height_m = height_cm / 100
        return weight / (height_m ** 2)
    
    @staticmethod
    # Calculate your body fat percentage (Deurenberg formula)
    def calculate_body_fat_percentage(user: User) -> float:
        bmi = BodyMetricsCalculator.calculated_bmi(user.weight, user.height)
        sex_factor = 1 if user.gender == Gender.Hombre else 0
        
        return (1.2 * bmi) + (0.23 * user.age) + (10.8 * sex_factor) - 5.4

# calorie calculator

class CalorieCalculator:
    # All calorie calculator
    @staticmethod
    def calculated_bmr(user: User) -> float:
        # Calculate basal mass ratio , Mifflinc-St jeor
        base = (user.weight * 10) + {user.height * 6.25} - (user.age * 5)
        
        if user.gender == Gender.Hombre:
            return base + 5
        else: 
            return base- 161

    @staticmethod
    def calculate_tdee(bmr: float, activity_level: ActivityLevel) -> float:
        # Calculate total daily energy expenditure (tdee)
        return bmr * activity_level.multiplier

    @staticmethod
    def calculate_target_deficit(tdee: float, deficit: int) -> float:
        # Calculate your target calorie deficit
        return tdee - deficit

class CalorieProlife:
    # Encapsulates all results of the user's caloric analysis.
    
    def __init__(self, user: User, activity_level: ActivityLevel, deficit: int):
        self.user = user
        self.activity_level = activity_level
        self.defecit = deficit
    
    # calculate all metrics
        self.body_fat = BodyMetricsCalculator.calculate_body_fat_percentage(user)
        self.bmi = BodyMetricsCalculator.calculated_bmi(user.weight, user.height)
        self.bmr = CalorieCalculator.calculated_bmr(user)
        self.tdee = CalorieCalculator.calculate_tdee(self.bmr, activity_level)
        self.target_calories = CalorieCalculator.calculate_target_deficit(self.tdee, deficit)
    
    def display_report(self) -> str:
        # Generate a complete calorie profile report
        report = []
        report.append("*" * 60)
        report.append("         PERFIL CALÓRICO COMPLETO")
        report.append("*" * 60)
        
        report.append("\n👤 DATOS PERSONALES:")
        report.append(f"    {self.user}")
        
        report.append("\n📈 ANÁLISIS CORPORAL:")
        report.append(f"    IMC: {self.bmi:.2f} kg/m²")
        report.append(f"    Grasa corporal estimada: {self.body_fat:.1f}%")
        
        report.append("\n🔥 ANÁLISIS CALÓRICO:")
        report.append(f"    Metabolismo basal (BMR): {self.bmr:.0f} kcal/día")
        report.append(f"    Nivel de actividad: {self.activity_level.name.capitalize()}")
        report.append(f"    Gasto total (TDEE): {self.tdee:.0f} kcal/día")
        
        report.append("\n🎯 TU PLAN:")
        report.append(f"    Déficit calórico: {self.defecit} kcal/día")
        report.append(f"    Calórias objetivo: {self.target_calories:.0f} kcal/día")
        report.append(f"    Pérdida estimada: ~{self.defecit * 7 / 7700:.2f} kg/semana")
        
        report.append("\n" + "*" * 60)
        
        return "\n".join(report)

# User Interface

class UserInterface:
    # Handless all user interation
    @staticmethod
    def get_user_data() -> User:
        # Request and collect user data
        
        print("\n🏃‍➡️ CALCULADORA DE CALÓRIAS")
        print("*" * 40)
        
        name = input("Nombre:\n")
        gender = int(input("1. Masculino\n2. Femenino\nSeleccione (1-2)\n"))
        age = int(input("Edad (años):\n"))
        weight = float(input("Peso (kg):\n"))
        height = float(input("Altura (cm):\n"))
        
        return User(name, gender, age, height, weight)
    
    @staticmethod
    def get_activity_level() -> ActivityLevel:
        # Request activity level
        print("💪🏻 NIVEL DE ACTIVIDAD:"
            "1. Sedentario (poco o ningún ejercicio)"
            "2. Ligero (ejercicio 1-3 dias/semana)"
            "3. Moderado (ejercicio 3-5 dias/semana)"
            "4. Alto (ejercicio 6-7 dias/semana)")
        
        while True:
            level_id = int(input("Seleccione entre 1-4: \n"))
            activity = ActivityLevel.from_id(level_id)
            
            if activity:
                return activity
            else:
                print("❌ Opción inválida")


    @staticmethod
    def get_calorie_deficit() -> int:
        # request the desired calorie deficit
        print("\n📉 DéFICIT CALÓRICO:"
            "✅ Recomendación: 300-500 kcal para pérdida sostenible"
            "⚠️ No exceder de 1000 kcal de déficit")
        
        deficit = int(input("Déficit deseado (kcal):\n"))
        
        if deficit > 1000:
            print("☠️ Advertencia: Déficit muy alto, recomendamos consultar a un profesional")

        return deficit

# Main program

def main():
    # full program flow
    try:
        # Recollect user info
        user = UserInterface.get_user_data()
        activity_level = UserInterface.get_activity_level()
        deficit = UserInterface.get_calorie_deficit()
        
        # Create calorie profile (All internal calculations)
        profile = CalorieProlife(user, activity_level, deficit)
        
        # Display report
        print(f"\n{profile.display_report()}")
    
    except ValueError as e:
        print("\❌ ERROR: Entrada inválida, ingrese valores númericos válidos.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()