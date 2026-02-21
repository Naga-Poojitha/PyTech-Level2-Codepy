from model import HousePriceModel


def main():
    model = HousePriceModel("kc_house_data.csv")

    try:
        model.load_data()
        r2 = model.train_model()
        print(f"\nModel R2 Score: {r2:.4f}")
    except Exception as e:
        print("Error loading dataset:", e)
        return

    while True:
        print("\n===== House Price Prediction =====")
        print("1. Predict House Price")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                sqft = float(input("Enter Sqft Living: "))
                bedrooms = float(input("Enter Bedrooms: "))
                bathrooms = float(input("Enter Bathrooms: "))

                price = model.predict(sqft, bedrooms, bathrooms)

                    # Convert USD to INR
                usd_to_inr = 83
                price_in_inr = price * usd_to_inr

                # Convert to Lakhs
                price_in_lakhs = price_in_inr / 100000

                print(f"\nPredicted Price (USD): ${price:,.2f}")

                if price_in_lakhs >= 100:
                    price_in_crores = price_in_lakhs / 100
                    print(f"Predicted Price (INR): ₹{price_in_crores:,.2f} Crores")
                else:
                    print(f"Predicted Price (INR): ₹{price_in_lakhs:,.2f} Lakhs")

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "2":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()