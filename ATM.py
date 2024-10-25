def atm_simulation():
    balance = int(input("Enter your Balance: "))
    
    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            print(f"Your balance is: ${balance:.2f}")
        
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"Deposited: ${amount:.2f}")
                
        
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > 0 and amount <= balance:
                balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            elif amount > balance:
                print("Insufficient funds.")
        
        elif choice == '4':
            print("Exiting the ATM. Thank you!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")

atm_simulation()
