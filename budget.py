
class Category:
    def __init__(self, category) -> None:
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        """A method that accepts an amount and description. 

        Returns an empty if no description is given.

        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Checks for withdrawal and funds in the ledger.

        Returns True if withdrawal took place, False otherwise.

        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        """A method that returns the current balance of the budget category 
        based on the deposits and withdrawals that have occurred.

        """
        current_balance = 0

        for item in self.ledger:
            current_balance += item["amount"]

        return current_balance

    def transfer(self, amount, category_2):
        """Checks for funds and prints transfer text.

        Returns True if the transfer took place, False otherwise.

        """
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category_2.category)
            category_2.deposit(amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        """Checks the amount of the budget category's balance."""
        return True if amount <= self.get_balance() else False

    def __str__(self) -> str:
        """Returns details of budget category."""
        title_line = f"{self.category.center(30, '*')}\n"

        output = ""

        total = 0

        for item in self.ledger:
            output += f"{item['description'].ljust(23)[:23]} {item['amount']:.2f}\n"
            total += item["amount"]

        return f"{title_line}{output}Total: {total}"


def create_spend_chart(categories) -> str:
    """Displays the percentage spent in each category."""
    chart_title = "Percentage spent by category\n"

    category_names, total_expenses, expense_percentages = [], [], []

    # Calculates the expenses of each category and totaling them up.
    for category in categories:
        expenses = 0
        for item in category.ledger:
            if item["amount"] < 0:
                expenses += item["amount"]
        total_expenses.append(round(expenses, 2))
        category_names.append(category.category)

    # Calculates the spending percentage of each category and round it down to the nearest 10.
    for amount in total_expenses:
        expense_percentages.append(round(amount/sum(total_expenses), 2)*100)

    # Displays the chart title and a vertical axis of 0 - 100.
    vertical_axis = range(100, -1, -10)

    for figure in vertical_axis:
        chart_title += "\n".join([str(figure).rjust(3) + "| "])
        for percent in expense_percentages:
            if percent >= figure:
                chart_title += "o  "
            else:
                chart_title += "   "

        chart_title += "\n"

    # Displays a horizontal line bar below that goes two spaces pas the final bar.
    chart_title += (" ".rjust(4)) + "---" * len(category_names) + "-"
    chart_title += "\n     "

    # Displays the name of each category vertically below the bar.
    max_name_length = max(len(name) for name in category_names)

    for name_length in range(max_name_length):
        chart_title += ''.join([char[name_length] + "  " if len(char)
                               > name_length else "   " for char in category_names])
        if name_length < max_name_length - 1:
            chart_title += "\n     "

    return chart_title
