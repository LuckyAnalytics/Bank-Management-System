
import json
import random
import string
from pathlib import Path


class Bank:
    database =  "/Users/luckysingh/Desktop/filehandling project/bank.json"
    data = []     #dummy data save in list
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An exception occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=5)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        account_id = alpha + num + spchar
        random.shuffle(account_id)

        return "".join(account_id)

    def createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0,
        }

        if (
            info["age"] < 18
            or info["age"] > 100
            or len(str(info["pin"])) != 4
        ):
            print("Sorry you cannot create your account")

        else:
            print("Account has been created successfully")
            print()

            for i in info:
                print(f"{i} : {info[i]}")

            print()
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositemoney(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if not userdata:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to deposit: "))

            if amount > 10000 or amount <= 0:
                print("Sorry, you can deposit between 1 and 10000")

            else:
                userdata[0]["balance"] += amount

                Bank.__update()

                print("Amount deposited successfully")

    def withdrwamoney(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if not userdata:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to withdraw: "))

            if amount <= 0:
                print("Amount must be greater than 0")

            elif userdata[0]["balance"] < amount:
                print("Sorry can't withdraw money")

            else:
                userdata[0]["balance"] -= amount

                Bank.__update()

                print("Amount withdrawn successfully")

    def showdetails(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))

        print()

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if not userdata:
            print("Sorry no data found")
            return

        print("Your information is:\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Enter your Account number: ")
        pin = input("Enter your Pin: ")

        if not accnumber or not pin:
            print("Account number and PIN cannot be empty")
            return

        pin = int(pin)

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if not userdata:
            print("No such user found")
            return

        print("You cannot change the age, account number, balance")
        print("Fill the details for change or leave it empty if no change")

        newdata = {
            "name": input(
                "Please tell your name or Press enter to skip: "
            ),
            "email": input(
                "Please enter your new email or press Enter to skip: "
            ),
            "pin": input(
                "Enter your new pin or Press enter to skip: "
            ),
        }

        # Keep old name if user presses Enter
        if newdata["name"] == "":
            newdata["name"] = userdata[0]["name"]

        # Keep old email if user presses Enter
        if newdata["email"] == "":
            newdata["email"] = userdata[0]["email"]

        # Keep old PIN if user presses Enter
        if newdata["pin"] == "":
            newdata["pin"] = userdata[0]["pin"]
        else:
            newdata["pin"] = int(newdata["pin"])

        newdata["age"] = userdata[0]["age"]
        newdata["accountNo."] = userdata[0]["accountNo."]
        newdata["balance"] = userdata[0]["balance"]

        for i in newdata:
            userdata[0][i] = newdata[i]

        Bank.__update()

        print("Details updated successfully")

    def deleteaccount(self):
        accnumber = input("Enter your Account number: ")
        pin = input("Enter your Pin: ")

        userdata = [
            i for i in Bank.data
            if i["accountNo."] == accnumber
            and str(i["pin"]) == pin
        ]

        if not userdata:
            print("Sorry, no such data exists")
            return

        check = input(
            "Press y to delete your account or n to skip: "
        )

        if check.lower() in ["n", "no"]:
            print("Nothing changed")

        elif check.lower() in ["y", "yes"]:
            Bank.data.remove(userdata[0])

            Bank.__update()

            print("Account deleted successfully")

        else:
            print("Invalid response")


#!streamlit run app.py.  always run in termial 
