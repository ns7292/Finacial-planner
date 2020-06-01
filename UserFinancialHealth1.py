#FinancialPlannerCalculator
import csv

class User:

    list=[['Age','Salary','Expense','OneTimeExpense','Savings','Networth']]
    networth_at_key_stages={}

    def __init__(self, current_age,retirement_age, current_salary,salary_increment_percent,current_expense,
                 expenece_increment_percent,current_networth,ROI,age_and_one_time_expence,life_expectancy=80):
        self.age=current_age
        self.retire_age=retirement_age
        self.salary=int(current_salary)
        self.salary_increment=salary_increment_percent
        self.expense=int(current_expense)
        self.expense_increment=expenece_increment_percent
        self.savings = self.salary - self.expense
        self.OTE=age_and_one_time_expence
        self.LE=life_expectancy
        self.networth = current_networth + self.savings
        self.ROI=ROI
        User.list.append([self.age,self.salary,self.expense,0,self.savings,self.networth])

    def end_worth(self):
        for _ in range(self.LE-self.age):
            self.age+=1
            if self.age<=self.retire_age:
                self.salary=int(self.salary*(1+self.salary_increment/100))
            else:
                self.salary=0
            self.expense=int(self.expense*(1+self.expense_increment/100))
            if self.age in self.OTE.keys():
                extra_expense=self.OTE[self.age]
            else:
                extra_expense=0
            self.savings = self.salary - self.expense - extra_expense
            if self.networth>0:
                self.networth=int(self.networth*(1+self.ROI/100))+self.savings
            else:
                self.networth=self.networth+self.savings
            dynamic_list=[self.age,self.salary,self.expense,extra_expense,self.savings,self.networth]

            User.list.append(dynamic_list) #Saves summery of each year in a list
            if self.age in self.OTE.keys():
                User.networth_at_key_stages[self.age]=self.networth
            elif self.age==self.retire_age:
                User.networth_at_key_stages[self.age]=self.networth
            elif self.age==self.LE:
                User.networth_at_key_stages[self.age] = self.networth
        return self.networth

    def csv_writer(self): # Writes summery of User's finance year by year
        with open('UserFinancialHealth1.csv','w',newline='') as file:
            writer=csv.writer(file)
            for i in User.list:
                writer.writerow(i)

    def msg(self):
        if self.end_worth()>=0:
            print('Your financial health is good. Your EndWorth is: ',self.end_worth())
        else:
            print('You financial health is at risk. Your EndWorth is: ',self.end_worth())

#User Inputs
CurrentAge_input=35
CurrentSalary_input=1000000
SalaryIncrement_input=2.5
CurrentExpense_input=500000
ExpenseIncrement_input=5
CurrentNetwoth_input=2000000
OneTimeExpenceWithAge_input={42:5000000,43:5000000,50:10000000}
LifeExpectancy_input=80

RetirementAge_input=50     #Variable Inputs
ExpenseChangepPerecent_input=-30
ROI_input=8
CurrentExpense=CurrentExpense_input*(1+ExpenseChangepPerecent_input/100)

#User Attributes
user=User(CurrentAge_input,RetirementAge_input,CurrentSalary_input,SalaryIncrement_input,CurrentExpense,
          ExpenseIncrement_input,CurrentNetwoth_input,ROI_input,OneTimeExpenceWithAge_input,LifeExpectancy_input)

user.msg()
user.csv_writer()

print(User.networth_at_key_stages)
if user.end_worth()<0:
    #Optimized Retire Age
    retire_age=RetirementAge_input
    user_RA=user
    while user_RA.end_worth()<0 and retire_age<80:
        retire_age+=1
        user_RA = User(CurrentAge_input, retire_age, CurrentSalary_input, SalaryIncrement_input, CurrentExpense,
                    ExpenseIncrement_input, CurrentNetwoth_input, ROI_input, OneTimeExpenceWithAge_input,LifeExpectancy_input)
    if user_RA.end_worth()<0:
        print('Extending retirement age only can not secure positive endworth. Try cutting expenses or incresing ROI')
    else:
        print('\nYou should either take retirement at',retire_age,'and keep everything else unchanged')

    #Optimized Expense Cut
    expense_cut=0
    user_EC=user
    while user_EC.end_worth()<0 and expense_cut<=80*CurrentExpense/100:
        OptimumExpense = CurrentExpense-expense_cut
        expense_cut+=100
        user_EC = User(CurrentAge_input, RetirementAge_input, CurrentSalary_input, SalaryIncrement_input, OptimumExpense,
                    ExpenseIncrement_input, CurrentNetwoth_input, ROI_input, OneTimeExpenceWithAge_input,LifeExpectancy_input)
    if user_EC.end_worth()<0:
        print('Cutting expenses only even by 80 percent cant secure positive endworth. Try to increase retirement age and ROI')
    else:
        print('OR You should cut your expenses by',int(CurrentExpense-OptimumExpense),'Rs and keep everything else unchanged OR')

    #Optimized ROI
    ROI=ROI_input
    user_ROI=user
    while user_ROI.end_worth()<0 and ROI<=25:
        ROI+=0.05
        user_ROI = User(CurrentAge_input, RetirementAge_input, CurrentSalary_input, SalaryIncrement_input, CurrentExpense,
                    ExpenseIncrement_input, CurrentNetwoth_input, ROI, OneTimeExpenceWithAge_input,LifeExpectancy_input)
    if user_EC.end_worth() < 0:
        print('Increasing ROI to even 25 percent can not secure positive endworth.')
    else:
        print('OR You should increase your ROI to', round(ROI,3),'percent and keep everything else unchanged')
