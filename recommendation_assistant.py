import requests


class VirtualAssistant:
    def __init__(self):
        self.real_time_data = {}

    def add_category_data(self, category, data):
        self.real_time_data[category] = data

    def get_recommendations(self):
        if self.real_time_data:
            print("\nRecommendations based on real-time data:")
            for category, recommendations in self.real_time_data.items():
                print(f"\n{category} recommendations:")
                for item, details in recommendations.items():
                    print(f"- {item}: {details}")
        else:
            print("No recommendations available.")

    def fetch_data_from_api(self, url):
        try:
            response = requests.get(url)
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching data from the API: {e}")
            return None


def display_menu():
    print("\nMenu Options:")
    print("1. Add Recommendation Category")
    print("2. Get Recommendations")
    print("3. Fetch Data from API")
    print("4. Exit")


def get_user_input(prompt):
    return input(prompt).strip()


def main():
    assistant = VirtualAssistant()

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == "1":
            category = get_user_input("Enter the recommendation category: ")
            data = {}

            while True:
                item = get_user_input("Enter an item (or leave blank to finish): ")
                if not item:
                    break

                details = get_user_input("Enter details for the item: ")
                data[item] = details

            assistant.add_category_data(category, data)
            print(f"Category '{category}' added successfully.")

        elif choice == "2":
            assistant.get_recommendations()

        elif choice == "3":
            url = get_user_input("Enter the API URL: ")
            data = assistant.fetch_data_from_api(url)
            if data:
                print("Data fetched from API:")
                print(data)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
