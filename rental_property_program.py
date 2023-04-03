from time import sleep
import sys
import csv

class Rental():
    """
    Class to store information about a rental property for use in a rental property evaluation program
    """
    def __init__(self) -> None:
        self.income_dict = dict()
        self.expense_dict = dict()
        self.investment_dict = dict()

    def add_income_source(self,source:str,amount:float):
        """
        Method to add a source of income.
        """
        source = source.lower()
        if source in self.income_dict:
            print("Warning, source was already in income dict")
            print(f"Changed income amount of {source} from {self.income_dict[source]} to {amount}")
        self.income_dict[source] = float(amount)

    def add_expense(self,source:str,amount:float):
        """
        Method to add an expense.
        """
        source = source.lower()
        if source in self.expense_dict:
            print("Warning, source was already in expense dict")
            print(f"Changed expense amount of {source} from {self.expense_dict[source]} to {amount}")
        self.expense_dict[source] = float(amount)
    
    def add_investment(self,source:str,amount:float):
        """
        Method to add an investment.
        """
        source = source.lower()
        if source in self.income_dict:
            print("Warning, source was already in investment dict")
            print(f"Changed expense amount of {source} from {self.investment_dict[source]} to {amount}")
        self.investment_dict[source] = float(amount)

    def update_income_source(self,source:str,amount:float):
        """
        Method to update dollar amount of income source
        """
        self.income_dict[source.lower()] = float(amount)

    def update_expense(self,source:str,amount:float):
        """
        Method to update dollar amount of expense
        """
        self.expense_dict[source.lower()] = float(amount)

    def update_investment(self,source:str,amount:float):
        """
        Method to update dollar amount of investment
        """
        self.investment_dict[source.lower()] = float(amount)
    
    def remove_income_source(self,source:str):
        """
        Method to remove an income source
        """
        del self.income_dict[source.lower()]

    def remove_expense(self,source:str):
        """
        Method to remove an expense
        """
        del self.expense_dict[source.lower()]

    def remove_investment(self,source:str):
        """
        Method to remove an investment
        """
        del self.investment_dict[source.lower()]
        
    def get_monthly_income(self):
        """
        Method to get monthly income
        """
        if not self.income_dict:
            return 0.
        else:
            return sum(self.income_dict.values())
        
    def get_monthly_expenses(self):
        """
        Method to get monthly expenses
        """
        if not self.expense_dict:
            return 0.
        else:
            return sum(self.expense_dict.values())
        
    def get_yearly_income(self):
        """
        Method to get yearly income
        """
        return self.get_monthly_income() * 12
    
    def get_yearly_expenses(self):
        """
        Method to get yearly expenses
        """
        return self.get_monthly_expenses() * 12
    
    def get_total_investment(self):
        """
        Method to get total investments
        """
        if not self.investment_dict:
            return 0.0
        return sum(self.investment_dict.values())
        
    def show_income_sources(self):
        """
        Method to show all income sources
        """
        if not self.income_dict:
            print("There are currently no sources of income")
            return
        
        income_header = "Monthly Income" # len = 14
        
        format_money = lambda x: f"{x:,.2f}"
        # To be used in justifying when printing money
        max_income_len = len(format_money(max(self.income_dict.values())))
        # Recalculates to account for income header, which doesn't have '$ '
        max_income_len = max(max_income_len,len(income_header)-2)

        print()
        print(income_header.rjust(max_income_len+2),"/","Source Name")
        print()
        for source,amount in self.income_dict.items():
            print("$",format_money(amount).rjust(max_income_len),"/",source)
        
        print("\nTotal Monthly Income")
        print("$",format_money(self.get_monthly_income()))
        print("\nTotal Yearly Income")
        print("$",format_money(self.get_yearly_income()),"\n")

    def show_expenses(self):
        """
        Method to show all expenses
        """
        if not self.expense_dict:
            print("There are currently no expenses")
            return
        
        expense_header = "Monthly Expenses" # len = 16
        
        format_money = lambda x: f"{x:,.2f}"
        # To be used in justifying when printing money
        max_expense_len = len(format_money(max(self.expense_dict.values())))
        # Recalculates to account for income header, which doesn't have '$ '
        max_expense_len = max(max_expense_len,len(expense_header)-2)

        print()
        print(expense_header.rjust(max_expense_len+2),"/","Expense Name")
        print()
        for source,amount in self.expense_dict.items():
            print("$",format_money(amount).rjust(max_expense_len),"/",source)
        
        print("\nTotal Monthly Expense")
        print("$",format_money(self.get_monthly_expenses()))
        print("\nTotal Yearly Expense")
        print("$",format_money(self.get_yearly_expenses()),"\n")

    def show_investments(self):
        """
        Method to show all investments
        """
        if not self.investment_dict:
            print("There are currently no investments")
            return
        
        investment_header = "Investment Amount" #  len = 17x
        format_money = lambda x: f"{x:,.2f}"
        # To be used in justifying when printing money
        max_investment_len = len(format_money(max(self.investment_dict.values())))
        # Recalculates to account for income header, which doesn't have '$ '
        max_investment_len = max(max_investment_len,len(investment_header)-2)
        print()
        print(investment_header.rjust(max_investment_len+2),"/","Investment Name")
        print()
        for source,amount in self.investment_dict.items():
            print("$",format_money(amount).rjust(max_investment_len),"/",source)
        
        print("\nTotal Investment")
        print("$",format_money(self.get_total_investment()))

    def show_sources(self,source_type:str):
        """
        Method to show all incomes, expenses, or investments, based on input. Must be 'income', 'expense', or 'investment'
        """
        d = {
            "income":self.show_income_sources,
            "expense":self.show_expenses,
            "investment":self.show_investments,
        }
        d[source_type]()
        return

    def get_monthly_cashflow(self):
        """
        Method to get monthly cashflow
        """
        return self.get_monthly_income() - self.get_monthly_expenses()
    
    def get_yearly_cashflow(self):
        """
        Method to get yearly cashflow
        """
        return self.get_monthly_cashflow() * 12
    
    def get_yearly_return_on_investment(self):
        """
        Method to get yearly return on investment as a percentage. Result is a string.
        """
        ROI = self.get_yearly_cashflow() * 100 / self.get_total_investment()
        return f"{round(ROI,2):.2f}%"
    
    def export_summary(self,property_name:str):
        """
        Function to create CSV summarizing results of program. Must provide property name
        Property name must only contains letters, spaces, or numbers. Property name will be
        basis of file name.
        """
        file_name = "_".join(property_name.split())+"_ValueEstimate.csv"
        with open(file_name,"w") as file:
            writer = csv.writer(file)
            # Establish reusable lambda
            format_money = lambda x: f"{x:,.2f}"
            writer.writerow(["Rental Property Name",property_name])
            writer.writerow([''])

            # Income Section
            writer.writerow(["INCOME"]) 
            writer.writerow(["Monthly Income ($)","Income Name"])
            for name,amount in self.income_dict.items():
                writer.writerow([format_money(amount),name])
            writer.writerow([''])
            writer.writerow([format_money(self.get_monthly_income()),"Total Monthly Income"])
            writer.writerow([format_money(self.get_yearly_income()),"Total Yearly Income"])
            writer.writerow([''])
            writer.writerow([''])

            # Expenses Section
            writer.writerow(["EXPENSES"]) 
            writer.writerow(["Monthly Expenses ($)","Expense Name"])
            for name,amount in self.expense_dict.items():
                writer.writerow([format_money(amount),name])
            writer.writerow([''])
            writer.writerow([format_money(self.get_monthly_expenses()),"Total Monthly Expense"])
            writer.writerow([format_money(self.get_yearly_expenses()),"Total Yearly Expense"])
            writer.writerow([''])
            writer.writerow([''])

            # Cashflow Section
            writer.writerow(["CASHFLOW"])
            writer.writerow([format_money(self.get_monthly_cashflow()),"Monthly Cashflow"])
            writer.writerow([format_money(self.get_yearly_cashflow()),"Yearly Cashflow"])
            writer.writerow([''])
            writer.writerow([''])

            # Investments Section
            writer.writerow(["INVESTMENTS"])
            writer.writerow(["Investment Amount ($)","Investment Name"])
            for name,amount in self.investment_dict.items():
                writer.writerow([format_money(amount),name])
            writer.writerow([''])
            writer.writerow([format_money(self.get_total_investment()),"Total Investment"])
            writer.writerow([''])
            writer.writerow([''])

            # ROI Section
            writer.writerow(["CASH ON CASH ROI"])
            writer.writerow([self.get_yearly_return_on_investment(),"Cash on Cash ROI"])
    

def rental_property_calculator():
    """
    Interactive rental property eveluator program
    """
    def p(text=""):
        """
        Make texted printed to console look like it is being typed
        The function below was created using knowledge gained from link below
        https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
        """
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.01)
        sleep(0.4)
        print()
        return

    def get_valid_money(prompt:str,error_message:str=None) -> float:
        """
        Function that continuously prompts a user to enter in a number until a non-negative number is given.
        """
        if not error_message:
            error_message = "Please enter a number 0 or greater"

        while True:
            p(prompt)
            response = input().strip()
            
            try:
                response = float(response)
            except:
                p(error_message)
                continue
            
            if response < 0:
                p(error_message)
                continue

            rounded = round(response,2)
            if response != rounded:
                p(f"We only track to the nearest cent. We rounded your input to be... {rounded:.2f}")

            return rounded
    
    def get_y_or_n(prompt:str,y_n_as_bool=True):
        """
        Prompts user to enter 'y' or 'n'. Will continue to ask until given. Returns ('y' or 'no")
        or (True or False) based on what y_n_as_bool as set to. Default returns bool.
        """
        while True:
            p(prompt)
            response = input().strip().lower()
            if response == "y" or response == "n":
                if y_n_as_bool:
                    return response == "y" 
                else:
                    return response
            p("That was not a valid input, try again")
    
    def welcome():
        """
        Function to welcome the user to the property estimation
        """
        p("Welcome to the rental property value calculator!")
        p()
        p("This program will help you estimate the value of your rental property.")
        p()
        p("We will start by first reviewing the monthly income from the rental property.")
        p()
        p("We will then review the monthly expenses from the property.")
        p()
        p("Monthly income and expenses will help us determine the property’s cash flow")
        p()
        p("From there we’ll collect info about the upfront investments, which will allow us to calculate the Cash on Cash return on investment (ROI)")
        p()
        p("Throughout this process, you will be prompted to enter dollar amounts")
        p("Please only enter numbers greater than or equal to zero")
        p("You can include decimal places, but they will be rounded to the nearest cent")
        p("Do not include commas when entering numbers")
        return
    
    def get_valid_source(source_type:str,action:str,prompt:str,error_message:str):
        """
        Helper function to get a valid source (income, expense, investment) from the 
        user. What is considered valid will be based on the type of source and the
        action the source will be used in. For instance, if this function is being called
        to get the name of an expense to remove, the user must provide an expense that
        already is being tracked.
        """
        valid_actions = {"add","update","remove"}
        if action not in valid_actions:
            p("Not a valid action")
            return False
        
        source_types = {
            "income":rental.income_dict,
            "expense":rental.expense_dict,
            "investment":rental.investment_dict,
            }
        if source_type not in source_types:
            p("Not a valid type")
            return False
        else:
            source_dict = source_types[source_type]

        while True:
            p(prompt)
            source = input().strip().lower()
            if not source:
                p("Response can not be empty. Please try again")
                continue

            if action == "add":
                if source in source_dict:
                    p(error_message)
                    continue
                else:
                    return source
            if action == "remove" or action == "update":
                if source not in source_dict:
                    p(error_message)
                    p(f"for reference, here are the list of items that can be {action}d")
                    p(", ".join(source_dict.keys()))
                    continue
                else:
                    return source

    def add_source(source_type:str):
        """
        Helper function to add a source based on source type (income, expense, investment)
        """
        source_types = {
            "income":"income source",
            "expense":"expense",
            "investment":"investment",
        }
        
        if source_type not in source_types:
            p("Type not found")
            return False
        
        source_text = source_types[source_type]

        prompt = f"What is the name of this new {source_text}?"
        error_message = f"Sorry, this {source_text} can't be added because it is already entered. Please try again"
        
        source = get_valid_source(source_type,"add",prompt,error_message)
        if source == False:
            return False
        
        money_prompt = {
            "income":f"How much money will you get from {source} per month?: ",
            "expense":f"How much money will {source} cost you per month?: ",
            "investment":f"How much money did {source} cost you?: " ,
        }
        money = get_valid_money(money_prompt[source_type])
        if source_type == "income":
            rental.add_income_source(source,money)
        elif source_type == "expense":
            rental.add_expense(source,money)
        elif source_type == "investment":
            rental.add_investment(source,money)

        sleep(delay_time)
        rental.show_sources(source_type)
        sleep(delay_time)
            
    def update_source(source_type:str):
        """
        Helper function to update a source based on source type (income, expense, investment)
        """
        source_types = {
            "income":"income source",
            "expense":"expense",
            "investment":"investment",
        }

        if source_type not in source_types:
            p("Type not found")
            return False
        
        source_dicts = {
            "income":rental.income_dict,
            "expense":rental.expense_dict,
            "investment":rental.investment_dict,
        }

        source_text = source_types[source_type]

        if not source_dicts[source_type]:
            p(f"You have not entered any {source_text}s, so there is nothing to update")
            return False

        prompt = f"What is the name of the {source_text} you'd like to update?: "
        error_message = f"Sorry, this {source_text} can't be updated because it hasn't yet been entered entered. Please try again"

        source = get_valid_source(source_type,"update",prompt,error_message)
        if source == False:
            return False
        money_prompt = {
            "income":f"How much money will you get from {source} per month?: ",
            "expense":f"How much money will {source} cost you per month?: ",
            "investment":f"How much money did {source} cost you?: " ,
        }
        money = get_valid_money(money_prompt[source_type])
        if source_type == "income":
            rental.update_income_source(source,money)
        elif source_type == "expense":
            rental.update_expense(source,money)
        elif source_type == "investment":
            rental.update_investment(source,money)
        
        sleep(delay_time)
        rental.show_sources(source_type)
        sleep(delay_time)

    def remove_source(source_type:str):
        """
        Helper function to remove a source based on source type (income, expense, investment)
        """
        source_types = {
            "income":"income source",
            "expense":"expense",
            "investment":"investment",
        }

        if source_type not in source_types:
            p("Type not found")
            return False
        
        source_dicts = {
            "income":rental.income_dict,
            "expense":rental.expense_dict,
            "investment":rental.investment_dict,
        }

        source_text = source_types[source_type]

        if not source_dicts[source_type]:
            p(f"You have not entered any {source_text}s, so there is nothing to remove")
            return False
        
        prompt = f"What is the name of the {source_text} you'd like to remove?: "
        error_message = f"Sorry, this {source_text} can't be remove because it hasn't yet been entered entered. Please try again"

        source = get_valid_source(source_type,"remove",prompt,error_message)
        if source == False:
            return False
        if source_type == "income":
            rental.remove_income_source(source)
        elif source_type == "expense":
            rental.remove_expense(source)
        elif source_type == "investment":
            rental.remove_investment(source)
        
        sleep(delay_time)
        rental.show_sources(source_type)
        sleep(delay_time)

    
    def print_modify_source_commands(source_type):
        """
        Helper function to print out the allowable commands when trying to modify a source
        """
        source_types = {
            "income":"income source",
            "expense":"expense",
            "investment":"investment",
        }
        source_text = source_types[source_type]
        p(f"Here are your commands to modify an {source_text}...")
        sleep(delay_time)

        print("'add'")
        print(f"Will prompt you to add a {source_text}\n")
        print("'update'")
        print(f"Will prompt you to update a {source_text}\n")
        print("'remove'")
        print(f"Will prompt you to remove a {source_text}\n")
        print("'cancel'")
        print(f"Stop modifying {source_text}\n")
        print("'commands'")
        print("Displays this list of commands\n")

    def modify_source(source_type):
        """
        Helper function that handles user commands when they are modifying a source. 
        Updates include adding, updating, or modifying.
        """
        print_modify_source_commands(source_type)
        
        while True:
            p("What would you like to do?: ")
            command = input().strip().lower()
            if command == "add":
                add_source(source_type)
            elif command == "update":
                update_source(source_type)
            elif command == "remove":
                remove_source(source_type)
            elif command == "cancel":
                return
            elif command == "commands":
                print_modify_source_commands(source_type)
            else:
                p("Sorry, that was not a valid command. Please try again. For a list of valid commands, enter 'commands'")

        
    def income():
        """"
        Function to drive the income portion of this program
        """
        p("Welcome to the income portion of this program")
        p("There are many different types of income. Let's walk through some of the basics, ")
        p("and then you'll have a chance to add your own")

        source_inputs = (
            ("rent","Rent: Rent is typically the main source of income. What is the total amount of money you make in rent each month from this property?: "),
            ("laundry","Laundry: Another common source of income is laundry. How much money do you take in from laundry each month?: "),
            ("storage","Storage: Some properties charge renters for extra storage. How much money do you take in from storage each month?: "),
        )
        
        for source_name,prompt in source_inputs:
            money = get_valid_money(prompt)
            rental.add_income_source(source_name,money)

        del source_inputs

        p("Here is a summary of your current income")
    
        sleep(delay_time)
        rental.show_income_sources()
        sleep(delay_time)

        p("The options I gave you are just some of the examples of different income sources")
        p("Now is your chance to customize")
    
        prompt = "Would you like to add, update, or remove any sources of income? Type 'y' for yes or 'n' for no: "
        modifying = get_y_or_n(prompt)
        
        if modifying:
            modify_source("income")

    def expenses():
        """
        Function to drive the expenses portion of this program.
        """
        p("Welcome to the expenses portion")
        p("There are many different types of expenses")
        p("We will run through the standard expenses, and then you will be given option to add your own")

        source_inputs = (
            ("taxes","Taxes: How much do you pay in taxes per month?: "),
            ("insurance","Insurance: How much do you pay in insurance per month?: "),
            ("utlities","Utilities: How much do you pay in utilities per month?: "),
            ("hoa fees","HOA fees: How much do you pay in Home Owner Association fees per month?: "),
            ("vacancy","Vacancy: It is good practice to put aside some money in case of vacancies. Experts recommend ~5% of cost of rent\n" + 
             "How much do you set aside for potential vacanies each month?: "),
            ("repairs","Repairs: It is a good practice to set aside some money each month for repairs. Expects recommend ~$100 per unit per month.\n" + 
             "How much do you set aside for repairs each month?: "),
            ("capex","Capital Expenditures (CapEx): Experts recommend putting aside ~$100 per month\n" + 
             "How much do you set aside for Capex each month?: "),
            ("property management","Property Management: How much do you pay for property management each month?: "),
            ("mortgage","Mortage: How much do you pay each month for your mortgage aside for property management each month?: "),
        )

        for source_name, prompt in source_inputs:
            money = get_valid_money(prompt)
            rental.add_expense(source_name,money)

        del source_inputs

        p("Here is a summary of your current expenses")
    
        sleep(delay_time)
        rental.show_expenses()
        sleep(delay_time)

        p("The options I gave you are just some of the examples of different types of expenses")
        p("Now is your chance to customize")

        prompt = "Would you like to add, update, or remove any expenses? Type 'y' for yes or 'n' for no: "
        modifying = get_y_or_n(prompt)
        if modifying:
            modify_source("expense")

        prompt = "Would you like to go back and add, update, or remove any sources of income? Type 'y' for yes or 'n' for no: "
        modifying = get_y_or_n(prompt)
        if modifying:
            modify_source("income")
    
    def cash_flow():
        """
        Function to calculate and display cashflow
        """
        p("Based on your provided income and expenses, we can estimate your cash flow")
        p("Monthly cash flow...")
        p("$ "+format_money(rental.get_monthly_cashflow()))
        p()
        p("Yearly cash flow...")
        p("$ "+format_money(rental.get_yearly_cashflow()))
    
    def investments():
        """
        Function to drive the the investments portion of this program
        """
        p("Welcome to the investments portion")
        p("There are many different types of investments")
        p("We will run through the standard investments, and then you will be given option to add your own")

        
        source_inputs = (
            ("down payment","Down Payment: What was the down payment?: "),
            ("closing cost","Closing Cost: What was the closing cost in purchasing this property?: "),
            ("rehab cost","rehab cost: How much did you spend on rehab for this property?: "),
        )
        
        for source_name, prompt in source_inputs:
            money = get_valid_money(prompt)
            rental.add_investment(source_name,money)

        p("Here is a summary of your current investments")
    
        sleep(delay_time)
        rental.show_investments()
        sleep(delay_time)
        
        p("The options I gave you are just some of the examples of different types of investment costs")

        prompt = "Would you like to add, update, or remove any investments? Type 'y' for yes or 'n' for no: "
        modifying = get_y_or_n(prompt)
        if modifying:
            modify_source("investment")
        
        p("Before we finalize the report, we want to make sure that you have a chance to update income or expenses if need.")
        
        prompt = "Would you like to go back and add, update, or remove any sources of income? Type 'y' for yes or 'n' for no: "
        modifying = get_y_or_n(prompt)
        if modifying:
            modify_source("income")
            p("Now that you have updated the property income, here is the updated cashflow")
            cash_flow()
        
        prompt = "Would you like to go back and add, update, or remove any expenses? Type 'y' for yes or 'n' for no: "
        modifying = get_y_or_n(prompt)
        if modifying:
            modify_source("expense")
            p("Now that you have updated the property expenses, here is the updated cashflow")
            cash_flow()


    def summary():
        """
        Function to summarize results
        """
        summary_sleep_duration = 3
        
        p("Here is the final report")
        sleep(1)
        
        print("\n\nINCOME")
        rental.show_income_sources()
        sleep(summary_sleep_duration)
        
        print("\n\nEXPENSES")
        rental.show_expenses()
        sleep(summary_sleep_duration)
        
        print("\n\nCASHFLOW\n")
        print("Monthly cash flow...")
        print("$ "+format_money(rental.get_monthly_cashflow()))
        print()
        print("Yearly cash flow...")
        print("$ "+format_money(rental.get_yearly_cashflow()))
        print()
        sleep(summary_sleep_duration)

        print("\n\nINVESTMENTS")
        rental.show_investments()
        print()
        sleep(summary_sleep_duration)

        p("With this this information, we can calculate your Cash on Cash return on investment (ROI)")
        p("Your cash on cash ROI is....")
        p(rental.get_yearly_return_on_investment())

        p()
        p("If you want, we can create a csv containing all of this information")
        prompt = "Would you like to create a CSV file containing all of this information? Type 'y' for yes or 'n' for no: "
        wants_summary = get_y_or_n(prompt)
        if wants_summary:
            p("Great!")
            p("We will ask that you provide a name for this rental property.")
            p("And that name will be used in the file name of the CSV")
            p("Be warned, this may overwrite any summaries previously created with the same property name.")
            p("Also, please only use letters, spaces, and numbers in property name")
            p("What would you like to name this property?: ")
            property_name = input().strip()
            rental.export_summary(property_name)
            p("Your summary file has been created")

        p("Thank you for using this program!!!")

    # Created the Rental Object
    rental = Rental()
    # Constant to manipulate delay time in displaying certain information
    delay_time = 1
    # Resuable lambda to quickly format a number
    format_money = lambda x: f"{x:,.2f}"    
    
    welcome()
    income()
    expenses()
    cash_flow()
    investments()
    summary()
    return rental

if __name__ == "__main__":
    rental_property_calculator()