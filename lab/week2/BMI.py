def get_bmi(weight_kg:float, height_cm:float) -> float:
    bmi = weight_kg / (height_cm/100) ** 2
    return bmi

def test_get_bmi():
    height = 172
    weight = 60
    b = get_bmi(weight, height)
    print(f"키({height}cm), 몸무게({weight}kg) => BMI: {b}입니다")

if __name__ == "__main__":
    test_get_bmi()



   