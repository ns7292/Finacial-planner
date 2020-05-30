#FinancialPlannerCalculator
import csv

class User:

    list=[['Age','Salary','Expense','OneTimeExpense','Savings','Networth']]

    def __init__(self, current_age,retirement_age, current_salary,salary_increment_percent,
                 current_expense,expense_cut_percent,expenece_increment_percent,
                 current_networth,ROI,one_time_expence_and_age=[(0,0),(0,0)],life_expectancy=80):
        self.age=current_age
        self.retire_age=retirement_age
        self.salary=int(current_salary)
        self.salary_increment=salary_increment_percent
        self.expense_cut_percent=expense_cut_percent
        self.expense=int(current_expense*(1+self.expense_cut_percent/100))
        self.expense_increment=expenece_increment_percent
        self.savings = self.salary - self.expense
        self.OTE=one_time_expence_and_age
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
            if self.age==self.OTE[0][1]:
                extra_expense=self.OTE[0][0]
            elif self.age==self.OTE[1][1]:
                extra_expense=self.OTE[1][0]
            else:
                extra_expense=0
            self.savings = self.salary - self.expense - extra_expense
            self.networth=int(self.networth*(1+self.ROI/100))+self.savings
            dynamic_list=[self.age,self.salary,self.expense,extra_expense,self.savings,self.networth]
            User.list.append(dynamic_list) #Saves summery of each year in a list
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

#User variables
CurrentAge_input=35
CurrentSalary_input=2400000
SalaryIncrement_input=2.5
CurrentExpense_input=1000000
ExpenseIncrement_input=5
CurrentNetwoth_input=1900000
OneTimeExpenceWithAge_input=[(5000000,42),(5000000,43)]
LifeExpectancy_input=80

RetirementAge_input=50       #Variable Inputs
ExpenseChange_input=-12.09
ROI_input=8

#User Initialization
user=User(CurrentAge_input,RetirementAge_input,CurrentSalary_input,SalaryIncrement_input,CurrentExpense_input,
          ExpenseChange_input,ExpenseIncrement_input,CurrentNetwoth_input,ROI_input,OneTimeExpenceWithAge_input,LifeExpectancy_input)

user.msg()  #User networth as per inputs
user.csv_writer()  

if user.end_worth()<0:   # Iterations to calcualete optimized retire age, or expense cut or ROI
    #Optimized Retire Age
    retire_age=RetirementAge_input
    user_RA=user
    while user_RA.end_worth()<0:
        retire_age+=1
        user_RA = User(CurrentAge_input, retire_age, CurrentSalary_input, SalaryIncrement_input, CurrentExpense_input,
                ExpenseChange_input, ExpenseIncrement_input, CurrentNetwoth_input, ROI_input, OneTimeExpenceWithAge_input,LifeExpectancy_input)
    print('\nYou should either take retirement at',retire_age,'and keep everything else unchanged OR')

    #Optimized Expense Cut
    expense_cut=ExpenseChange_input
    user_EC=user
    while user_EC.end_worth()<0:
        expense_cut+=-0.05
        user_EC = User(CurrentAge_input, RetirementAge_input, CurrentSalary_input, SalaryIncrement_input, CurrentExpense_input,
                    expense_cut, ExpenseIncrement_input, CurrentNetwoth_input, ROI_input, OneTimeExpenceWithAge_input,
                    LifeExpectancy_input)
    print('You should cut your expenses by',round(-expense_cut,3),'percent and keep everything else unchanged OR')

    #Optimized ROI
    ROI=ROI_input
    user_ROI=user
    while user_ROI.end_worth()<0:
        ROI+=0.05
        user_ROI = User(CurrentAge_input, RetirementAge_input, CurrentSalary_input, SalaryIncrement_input, CurrentExpense_input,
                    ExpenseChange_input, ExpenseIncrement_input, CurrentNetwoth_input, ROI, OneTimeExpenceWithAge_input,
                    LifeExpectancy_input)
    print('You should increase your ROI to', round(ROI,3),'percent and keep everything else unchanged')

# If user have large endworth, he can also opt to retire early or increase his expense but right now i have made it optional
'''else:    
    #Optimized Retire Age
    retire_age=RetirementAge_input
    user_RA=user
    while user_RA.end_worth()>0:
        retire_age-=1
        user_RA = User(CurrentAge_input, retire_age, CurrentSalary_input, SalaryIncrement_input, CurrentExpense_input,
                ExpenseCut_input, ExpenseIncrement_input, CurrentNetwoth_input, ROI_input, OneTimeExpenceWithAge_input,LifeExpectancy_input)
    print('\nYou can take retirement early at',retire_age+1,'OR and keep everything else unchanged')

    #Optimized Expense Cut
    expense_cut=ExpenseCut_input
    user_EC=user
    while user_EC.end_worth()>0:
        expense_cut+=0.1
        user_EC = User(CurrentAge_input, RetirementAge_input, CurrentSalary_input, SalaryIncrement_input, CurrentExpense_input,
                    expense_cut, ExpenseIncrement_input, CurrentNetwoth_input, ROI_input, OneTimeExpenceWithAge_input,
                    LifeExpectancy_input)
    print('You can increase your expenses by',round(expense_cut,3),'percent and keep everything else unchanged OR')

    #Optimized ROI
    ROI=ROI_input
    user_ROI=user
    while user_ROI.end_worth()>0:
        ROI-=0.1
        user_ROI = User(CurrentAge_input, RetirementAge_input, CurrentSalary_input, SalaryIncrement_input, CurrentExpense_input,
                    ExpenseCut_input, ExpenseIncrement_input, CurrentNetwoth_input, ROI, OneTimeExpenceWithAge_input,
                    LifeExpectancy_input)
    print('You can decrease your ROI to', round(ROI+0.1,3),'percent and keep everything else unchanged')
'''
