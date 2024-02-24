### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, value in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < value:
                return False
        return True
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        coins = {
            "large dollars($1)": 1,
            "half-dollars($0.5)": 0.5,
            "quarters($0.25)": 0.25,
            "nickels($0.05)": 0.05,
        }
        total = 0
        print("Please insert coins \n")
        for coin, value in coins.items():
            num = int(input(f"How many {coin} coins would you like to insert: "))
            total += num * value
        return total
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            return False
        else:
            return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, value in order_ingredients.items():
            self.machine_resources[ingredient] -= value
### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwich_machine = SandwichMachine(resources)

# Creating a while loop for the machine
while True:
    print("What would you like? (small/ medium/ large/ off/ report)")
    choice = input()

    # option to break the loop to turn off the machine
    if choice == "off":
        break

    # option to print a report of the current resourcees
    elif choice == "report":
        for resource, value in resources.items():
            print(f"{resource}: {value}")

    # focusing on the ingredients for the chosen size
    elif choice in recipes:
        ingredients = recipes[choice]["ingredients"]

        # validating if there are enough resources left for the chosen size
        if not sandwich_machine.check_resources(ingredients):
            print("Sorry there is not enough ingredients.\n")

        # continuing next with obtaining the total payment along with the cost
        else:
            total = sandwich_machine.process_coins()
            cost = recipes[choice]["cost"]

            # validating if payment is enough to cover the cost
            if not sandwich_machine.transaction_result(total, cost):
                print("Sorry, that is not enough for your sandwich. Money was refunded.\n")

            # lastly delivering sandwich and calculating/returning change
            else:
                sandwich_machine.make_sandwich(choice, ingredients)
                change = total - cost
                print(f"Here is $" + str(change) + " in change!\n")
                print("Here is your " + choice + " sandwich! Enjoy! \n")









