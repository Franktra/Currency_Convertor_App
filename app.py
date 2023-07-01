import streamlit as st
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if to_currency not in data["rates"]:
        return None

    exchange_rate = data["rates"][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    st.title("Currency Converter Application")
    st.write("Enter the amount, select the source currency, and select the target currency to convert.")

    amount = st.number_input("Amount", min_value=0.0)
    from_currency = st.selectbox("From Currency", ["USD", "EUR", "GBP", "JPY", "CAD"])
    to_currency = st.selectbox("To Currency", ["USD", "EUR", "GBP", "JPY", "CAD"])

    if st.button("Convert"):
        if amount > 0.0 and from_currency != to_currency:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            if converted_amount is not None:
                st.write(f"{amount} {from_currency} = {converted_amount} {to_currency}")
            else:
                st.write("Conversion rate not available.")

if __name__ == "__main__":
    main()
