
import streamlit as st
from bank import Bank


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)


# ---------------- TITLE ----------------

st.title("🏦 Bank Management System")
st.write("Welcome to the Bank Management System")


# ---------------- SIDEBAR ----------------

st.sidebar.title("Bank Menu")

choice = st.sidebar.selectbox(
    "Choose an option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Details",
        "Delete Account"
    ]
)


# ==================================================
# CREATE ACCOUNT
# ==================================================

if choice == "Create Account":

    st.header("📝 Create Account")

    name = st.text_input("Enter your name")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        step=1
    )

    email = st.text_input("Enter your email")

    pin = st.text_input(
        "Enter your 4 digit PIN",
        type="password",
        max_chars=4
    )

    if st.button("Create Account"):

        if not name or not email or not pin:
            st.error("Please fill all the fields.")

        elif not pin.isdigit() or len(pin) != 4:
            st.error("PIN must contain exactly 4 digits.")

        elif age < 18:
            st.error("You must be at least 18 years old.")

        else:

            info = {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "accountNo.": Bank._Bank__accountgenerate(),
                "balance": 0
            }

            Bank.data.append(info)
            Bank._Bank__update()

            st.success(
                "Account has been created successfully! 🎉"
            )

            st.write("### Account Details")

            st.write("**Name:**", info["name"])
            st.write("**Age:**", info["age"])
            st.write("**Email:**", info["email"])
            st.write("**PIN:**", info["pin"])
            st.write(
                "**Account Number:**",
                info["accountNo."]
            )
            st.write("**Balance:** ₹", info["balance"])

            st.warning(
                "⚠️ Please save your account number."
            )


# ==================================================
# DEPOSIT MONEY
# ==================================================

elif choice == "Deposit Money":

    st.header("💰 Deposit Money")

    accnumber = st.text_input(
        "Enter your Account Number"
    )

    pin = st.text_input(
        "Enter your PIN",
        type="password"
    )

    amount = st.number_input(
        "Enter amount to deposit",
        min_value=1,
        max_value=10000,
        step=100
    )

    if st.button("Deposit Money"):

        try:
            pin = int(pin)

            userdata = [
                i for i in Bank.data
                if i["accountNo."] == accnumber
                and i["pin"] == pin
            ]

            if not userdata:

                st.error("Sorry, no data found.")

            else:

                userdata[0]["balance"] += amount

                Bank._Bank__update()

                st.success(
                    f"₹{amount} deposited successfully! 💰"
                )

                st.info(
                    f"Current Balance: ₹{userdata[0]['balance']}"
                )

        except ValueError:

            st.error("PIN must contain numbers only.")


# ==================================================
# WITHDRAW MONEY
# ==================================================

elif choice == "Withdraw Money":

    st.header("💸 Withdraw Money")

    accnumber = st.text_input(
        "Enter your Account Number"
    )

    pin = st.text_input(
        "Enter your PIN",
        type="password"
    )

    amount = st.number_input(
        "Enter amount to withdraw",
        min_value=1,
        step=100
    )

    if st.button("Withdraw Money"):

        try:
            pin = int(pin)

            userdata = [
                i for i in Bank.data
                if i["accountNo."] == accnumber
                and i["pin"] == pin
            ]

            if not userdata:

                st.error("Sorry, no data found.")

            elif userdata[0]["balance"] < amount:

                st.error("Insufficient balance.")

            else:

                userdata[0]["balance"] -= amount

                Bank._Bank__update()

                st.success(
                    f"₹{amount} withdrawn successfully! 💸"
                )

                st.info(
                    f"Current Balance: ₹{userdata[0]['balance']}"
                )

        except ValueError:

            st.error("PIN must contain numbers only.")


# ==================================================
# ACCOUNT DETAILS
# ==================================================

elif choice == "Account Details":

    st.header("👤 Account Details")

    accnumber = st.text_input(
        "Enter your Account Number"
    )

    pin = st.text_input(
        "Enter your PIN",
        type="password"
    )

    if st.button("Show Details"):

        try:
            pin = int(pin)

            userdata = [
                i for i in Bank.data
                if i["accountNo."] == accnumber
                and i["pin"] == pin
            ]

            if not userdata:

                st.error("Sorry, no data found.")

            else:

                user = userdata[0]

                st.success("Account found! ✅")

                st.write("### Your Information")

                st.write("**Name:**", user["name"])
                st.write("**Age:**", user["age"])
                st.write("**Email:**", user["email"])
                st.write(
                    "**Account Number:**",
                    user["accountNo."]
                )
                st.write(
                    "**Balance:**",
                    f"₹{user['balance']}"
                )

        except ValueError:

            st.error("PIN must contain numbers only.")


# ==================================================
# UPDATE DETAILS
# ==================================================

elif choice == "Update Details":

    st.header("✏️ Update Details")

    accnumber = st.text_input(
        "Enter your Account Number"
    )

    pin = st.text_input(
        "Enter your Current PIN",
        type="password"
    )

    st.info(
        "You cannot change Age, Account Number "
        "or Balance."
    )

    new_name = st.text_input(
        "New Name (leave empty if no change)"
    )

    new_email = st.text_input(
        "New Email (leave empty if no change)"
    )

    new_pin = st.text_input(
        "New PIN (leave empty if no change)",
        type="password",
        max_chars=4
    )

    if st.button("Update Details"):

        try:

            pin = int(pin)

            userdata = [
                i for i in Bank.data
                if i["accountNo."] == accnumber
                and i["pin"] == pin
            ]

            if not userdata:

                st.error("No such user found.")

            else:

                user = userdata[0]

                if new_name:
                    user["name"] = new_name

                if new_email:
                    user["email"] = new_email

                if new_pin:

                    if not new_pin.isdigit() or len(new_pin) != 4:

                        st.error(
                            "New PIN must contain exactly 4 digits."
                        )

                    else:

                        user["pin"] = int(new_pin)

                        Bank._Bank__update()

                        st.success(
                            "Details updated successfully! ✅"
                        )

                else:

                    Bank._Bank__update()

                    st.success(
                        "Details updated successfully! ✅"
                    )

        except ValueError:

            st.error("Current PIN must contain numbers only.")


# ==================================================
# DELETE ACCOUNT
# ==================================================

elif choice == "Delete Account":

    st.header("🗑️ Delete Account")

    accnumber = st.text_input(
        "Enter your Account Number"
    )

    pin = st.text_input(
        "Enter your PIN",
        type="password"
    )

    st.warning(
        "⚠️ Deleting your account cannot be undone."
    )

    confirm = st.checkbox(
        "I understand that my account will be permanently deleted."
    )

    if st.button("Delete Account"):

        if not confirm:

            st.error(
                "Please confirm account deletion first."
            )

        else:

            try:

                pin = int(pin)

                userdata = [
                    i for i in Bank.data
                    if i["accountNo."] == accnumber
                    and i["pin"] == pin
                ]

                if not userdata:

                    st.error(
                        "Sorry, no such account exists."
                    )

                else:

                    Bank.data.remove(userdata[0])

                    Bank._Bank__update()

                    st.success(
                        "Account deleted successfully! 🗑️"
                    )

            except ValueError:

                st.error(
                    "PIN must contain numbers only."
                )