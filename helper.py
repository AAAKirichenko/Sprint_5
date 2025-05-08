from faker import Faker

faker = Faker()

def generate_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password  # Возвращаем кортеж (email, password)

def generate_registration_data_for_error_password():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=4, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password  # Возвращаем кортеж (email, password)