menu = """
Uni Residences Rental System
What would you like to do?
[1] Register a new Tenant
[2] Remove an existing Tenant
[3] Show all Tenants
[4] Display Total Monthly Rent
[5] Display Total Yearly Rent
[6] Display Total Monthly Maintenance and Utility Cost
[7] Display Total Yearly Maintenance and Utility Cost
[8] Exit the Program
"""
tenant_name = []

# Register a new Tenant
def register_tenant():
        while True:
            name = input("Enter the name of the new tenant (Type 'cancel' to abort): ").title()
            if len(name) == 0:
                print("Sorry, please try again and enter an appropriate name.\n")
            elif name in tenant_name:
                print("Sorry, it seems like the tenant is already added. Please try again.\n")
            elif name == "Cancel":
                print("Returning to menu...\n")
                break
            else:
                tenant_name.append(name)
                print("The new tenant has been registered!")
                print("New list:\n" + ", ".join(tenant_name))
                break
                        
# Remove an existing Tenant
def remove_tenant():
    while True:
        name = input("Enter the name of the tenant you want to remove (Type 'cancel' to abort): ").title()
        if len(name) == 0:
            print("Sorry, please try again and enter an appropriate name.\n")
        elif name == "Cancel":
            print("Returning to menu...\n")
            break
        elif name in tenant_name:
            tenant_name.remove(name)
            print(f"'{name}' successfully removed from the list!")
            if len(tenant_name) == 0:
                print("Updated list: The list is currently empty.")
                break
            else:
                print("Updated list:\n " + ", ".join(tenant_name))
                break
        else:
            print(f"Sorry, '{name}' is not in the list.")

# Show all tenants
def show_tenant():
    if len(tenant_name) == 0:
        print("There are no tenants in the list yet.")
    else:
        print("List of all tenants:")
        for no, name in enumerate(sorted(tenant_name)):
            print(f"{no + 1}. {name}")

# Display Total Monthly Rent
def total_monthlyRent():
    num = int(len(tenant_name))
    if num > 4:
        totalNo = num - 4
        sum = (2*450) + (2*500) + (totalNo*550)
    elif num == 1:
        sum = 450
    elif num == 2:
        sum = (2*450)
    elif num == 3:
        sum = (2*450) + 500
    elif num == 4:
        sum = (2*450) + (2*500)
    else:
        sum = "Sorry, no rent records available."
    return sum

# Display Total Yearly Rent
def total_yearlyRent():
    if len(tenant_name) != 0:
        yearlyRent = total_monthlyRent() * 12
    else:
        yearlyRent = "Sorry, no rent records available."
    return yearlyRent

# Display Total Monthly Maintenance and Utility Cost
def monthly_maintenance():
    if len(tenant_name) != 0:
        mmaint = total_monthlyRent() * 0.15
    else:
        mmaint = "Sorry, no rent records available."
    return mmaint

# Display Total Yearly Maintenance and Utility Cost
def yearly_maintenance():
    if len(tenant_name) != 0:
        ymaint = total_yearlyRent() * 0.15
    else:
        ymaint = "Sorry, no rent records available."
    return ymaint


while True:
    print(f"\n {menu}")
    select = input("Please enter your choice: ")

    if select == "1":
        register_tenant()
    elif select == "2":
        remove_tenant()
    elif select == "3":
        show_tenant()
    elif select == "4":
        if len(tenant_name) != 0:
            print(f"Total monthly rent is: RM{total_monthlyRent()}")
        else:
            print(total_monthlyRent())
    elif select == "5":
        if len(tenant_name) != 0:
            print(f"Total yearly rent is: RM{total_yearlyRent()}")
        else:
            print(total_yearlyRent())
    elif select == "6":
        if len(tenant_name) != 0:
            print(f"Total monthly maintenance and utility cost is: RM{monthly_maintenance()}")
        else:
            print(monthly_maintenance())
    elif select == "7":
        if len(tenant_name) != 0:
            print(f"Total yearly maintenance and utility cost is: RM{yearly_maintenance()}")
        else:
            print(yearly_maintenance())
    elif select == "8":
        print("Thank you for using our service! Exiting...")
        break
    else:
        print("Error! Please try again.")
