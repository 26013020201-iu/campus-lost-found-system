import json
import os
from datetime import datetime

FILE_NAME = "campus_items.json"


def load_items():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_items(items):
    with open(FILE_NAME, "w") as file:
        json.dump(items, file, indent=4)


def report_item(items, item_type):
    print(f"\n--- Report {item_type} Item ---")

    name = input("Enter item name: ").strip()
    description = input("Enter description: ").strip()
    location = input("Enter location: ").strip()
    contact = input("Enter your contact details: ").strip()

    if not all([name, description, location, contact]):
        print("All fields are required.")
        return

    item = {
        "id": len(items) + 1,
        "name": name,
        "type": item_type,
        "description": description,
        "location": location,
        "contact": contact,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "status": "Active"
    }

    items.append(item)
    save_items(items)

    print("\nItem reported successfully!")


def view_items(items):
    print("\n--- All Reported Items ---")

    if not items:
        print("No items reported yet.")
        return

    for item in items:
        print("-" * 40)
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Type: {item['type']}")
        print(f"Description: {item['description']}")
        print(f"Location: {item['location']}")
        print(f"Date: {item['date']}")
        print(f"Status: {item['status']}")


def search_item(items):
    keyword = input("\nEnter item name to search: ").strip().lower()

    results = [
        item for item in items
        if keyword in item["name"].lower()
        or keyword in item["description"].lower()
    ]

    if not results:
        print("No matching items found.")
        return

    print("\n--- Search Results ---")
    for item in results:
        print(
            f"ID: {item['id']} | {item['name']} | "
            f"{item['type']} | {item['location']} | "
            f"{item['status']}"
        )


def mark_returned(items):
    try:
        item_id = int(input("\nEnter item ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for item in items:
        if item["id"] == item_id:
            item["status"] = "Returned"
            save_items(items)
            print("Item marked as returned successfully!")
            return

    print("Item ID not found.")


def main():
    items = load_items()

    while True:
        print("\n" + "=" * 45)
        print("       CAMPUS LOST & FOUND SYSTEM")
        print("=" * 45)
        print("1. Report Lost Item")
        print("2. Report Found Item")
        print("3. View All Items")
        print("4. Search for an Item")
        print("5. Mark Item as Returned")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            report_item(items, "Lost")
        elif choice == "2":
            report_item(items, "Found")
        elif choice == "3":
            view_items(items)
        elif choice == "4":
            search_item(items)
        elif choice == "5":
            mark_returned(items)
        elif choice == "6":
            print("Thank you for using Campus Lost & Found!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
