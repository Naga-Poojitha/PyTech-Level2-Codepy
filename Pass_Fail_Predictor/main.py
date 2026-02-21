from model import PassFailModel


def main():
    model = PassFailModel("students.csv")

    try:
        model.load_data()
        accuracy = model.train_model()
        print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
    except Exception as e:
        print("Error loading dataset:", e)
        return

    while True:
        print("\n===== Pass/Fail Predictor =====")
        print("1. Predict Result")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                math = float(input("Enter Math score: "))
                reading = float(input("Enter Reading score: "))
                writing = float(input("Enter Writing score: "))

                prediction = model.predict(math, reading, writing)
                print("\nPrediction:", prediction)

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "2":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()