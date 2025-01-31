print("Welcome to the Email Generator!")
name = input("Enter your name: ")
company = input("Enter your company: ")
domain = input("Enter your domain: ")

email = f"{name.lower()}@{company.lower()}.{domain.lower()}"

print(f"Your email is: {email}")