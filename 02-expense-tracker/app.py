def main():
    print("Expense Tracker")
    print("Type your expense amount and press Enter.")
    print("type 'exit' to see your final total.\n")
    
    total = 0.0  
    
    while True:
        user_input = input("Enter expense amount: ").strip()
        
        if user_input.lower() == 'exit':
            break
            
        try:
            expense = float(user_input)
            
            if expense < 0:
                print("Expenses can't be negative. Please enter a valid number.")
                continue
                
            total += expense
            print(f"Current Total: ${total:.2f}\n")
            
        except ValueError:
            print("Invalid input. Please enter a number or type 'exit'.\n")
            
    print(f"Final Total Spent: ${total:.2f}")
    print("Thank you for using the tracker!")

if __name__ == "__main__":
    main()