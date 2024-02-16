"""
CSC 4110
HOMEWORK4:QUESTION 1
START DATE: 02/ 10 / 2024
BEGIN ROHITH SURESH (02/10/24)
"""


# Import necessary libraries
import random
import string

class DataWarehousing:
    def __init__(self):
        self.data_store = {}

    # Step One: Data Collector
    def data_collector(self, num_records):
        """
        Simulates user records and generates sample data.
        
        Args:
        - num_records: Number of user records to generate
        
        Returns:
        - None, but populates self.data_store with generated data
        """
        for _ in range(num_records):
            username = ''.join(random.choices(string.ascii_lowercase, k=8))
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            birthdate = f"{random.randint(1950, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            address = f"{random.randint(100, 999)} {random.choice(['Street', 'Avenue', 'Boulevard'])}"
            ssn = ''.join(random.choices(string.digits, k=9))
            product_purchased = f"ID-{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}"
            salesperson = random.choice(['John', 'Jane', 'Smith'])

            # Storing data in key-value pairs with unique user ID as key
            user_id = f"UID-{random.randint(1000, 9999)}"
            self.data_store[user_id] = {
                'username': username,
                'password': password,
                'birthdate': birthdate,
                'address': address,
                'ssn': ssn,
                'product_purchased': product_purchased,
                'salesperson': salesperson
            }

    # Step Three: Search Engine
    def search_data_store(self, user_id):
        """
        Searches the data store based on provided user ID.
        
        Args:
        - user_id: User ID to search
        
        Returns:
        - User record matching the user ID or None if not found
        """
        return self.data_store.get(user_id)

# Usage example
if __name__ == "__main__":
    dw = DataWarehousing()
    dw.data_collector(100)  # Generate 100 user records
    
    # Display a limited number of user IDs
    print("List of User IDs:")
    user_ids = list(dw.data_store.keys())[:10]  # Change 10 to the desired limit
    for user_id in user_ids:
        print(user_id)
    
    while True:
        user_input = input("Enter the user ID to search (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        user_data = dw.search_data_store(user_input)
        if user_data:
            print("User Details:")
            print(user_data)
        else:
            print("User ID not found.")


"""
FINAL DATE: 15/ 02/ 2024
END ROHITH SURESH
"""