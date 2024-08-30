# test_add_user.py

from services.user_service import add_user

# Добавление пользователя
new_user = add_user(
    nick="johndoe",
    name="John",
    surname="Doe",
    patronymic="Edward",
    role="admin",
    avatar="avatar.png"
)

print(f"User created with ID: {new_user.id}, Name: {new_user.name}")
