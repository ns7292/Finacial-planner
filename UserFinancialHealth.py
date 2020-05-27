#FinancialPlannerCalculator
import csv

class User:

    list=[['Age','Salary','Expense','OneTimeExpense','Savings','Networth']]

    def __init__(self, current_age, current_salary, current_expense,r, current_networth, one_time_expence_and_age=[(0,0),(0,0)],life_expectancy=80):
        self.age=current_age
        self.salary=int(current_salary)
        self.expense=int(current_expense*(1+r/100))
        self.savings = self.salary - self.expense
        self.OTE=one_time_expence_and_age
        self.LE=life_expectancy
        self.networth = current_networth + self.savings
        User.list.append([self.age,self.salary,self.expense,0,self.savings,self.networth])

    def end_worth(self,RetirementAge=50, SalaryIncrement=2.5, ExpenseIncrement=5, ROI=8): #Default values
        for _ in range(self.LE-self.age):
            self.age+=1
            if self.age<=RetirementAge:
                self.salary=int(self.salary*(1+SalaryIncrement/100))
            else:
                self.salary=0
            self.expense=int(self.expense*(1+ExpenseIncrement/100))
            if self.age==self.OTE[0][1]:
                extra_expense=self.OTE[0][0]
            elif self.age==self.OTE[1][1]:
                extra_expense=self.OTE[1][0]
            else:
                extra_expense=0
            self.savings = self.salary - self.expense - extra_expense
            self.networth=int(self.networth*(1+ROI/100))+self.savings
            dynamic_list=[self.age,self.salary,self.expense,extra_expense,self.savings,self.networth]
            User.list.append(dynamic_list) #Saves summery of each year in a list
        return round(self.networth)

    def csv_writer(self): # Writes summery of User's finance year by year
        with open('UserFinancialHealth.csv','w',newline='') as file:
            writer=csv.writer(file)
            for i in User.list:
                writer.writerow(i)
            print('Your summery is in UserFinancialHealth.csv file')

    def msg(self):
        if self.end_worth()>=0:
            print('Your financial health is good. Your EndWorth is: ',self.end_worth())
        else:
            print('You financial health is at risk. Your EndWorth is: ',self.end_worth())


RetirementAge_input=50 # We can varry these three inputs as we wish to
ExpenceChangePercent_input=0
ROI_input=8.1

user1=User(35,2400000,1000000,ExpenceChangePercent_input,1900000,[(5000000,42),(5000000,43)],80)

user1.end_worth(RetirementAge_input,2.5,5,ROI_input)

# RetirementAge_input=50 # We can varry these three inputs as we wish to
# ExpenceChangePercent_input=0
# ROI_input=8
# user2=User(30,2400000,1000000,ExpenceChangePercent_input,1900000,[(6000000,42),(6000000,43)])
# user2.end_worth(RetirementAge_input,2.5,5,ROI_input)

user1.msg()
user1.csv_writer()
# user2.msg()
# user2.csv_writer()
