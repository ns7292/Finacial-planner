# Financial_Planner
present_age, annual_salary, annual_expence,retirement_age,net_worth = map(int, input('Enter age, Salary, Expence, RetirementAge,Networth as space seperated:').split())
salary_increment_rate, expence_increment_rate, return_rate_on_investment = map(float,input('Enter rates here:').split())
one_time_expense , age_at_one_time_expense=map(int,input('Enter one time expense and age at that time here:').split())
def end_worth(p_a,r_a,a_s,a_e,sal_inc,exp_inc,inv_ret,networth):
    p_a=present_age
    r_a=retirement_age
    a_s=annual_salary
    a_e=annual_expence
    sal_inc = salary_increment_rate/ 100
    exp_inc = expence_increment_rate / 100
    inv_ret =  return_rate_on_investment / 100
    networth = net_worth
    for i in range(80 - p_a):
        if i < (r_a - p_a):
            a_s = round(a_s * (1 + sal_inc))
        else:
            a_s = 0
        a_e = round(a_e * (1 + exp_inc))
        if (i == age_at_one_time_expense-p_a):
            onetime_expence = one_time_expense
        else:
            onetime_expence = 0
        annual_savings = a_s - a_e - onetime_expence

        networth = round(networth * (1 + inv_ret)) + annual_savings
    if networth>0:
        print('Great, User have good financial planning and sufficient funds for his comfortable life')
    else:
        def end_worth_on_increasing_retirement(r_a):
            p_a=present_age
            a_s=annual_salary
            a_e=annual_expence
            sal_inc = salary_increment_rate/ 100
            exp_inc = expence_increment_rate / 100
            inv_ret =  return_rate_on_investment / 100
            networth = net_worth
            for i in range(80 - p_a):
                if i < (r_a - p_a):
                    a_s = round(a_s * (1 + sal_inc))
                else:
                    a_s = 0
                a_e = round(a_e * (1 + exp_inc))
                if (i == age_at_one_time_expense - p_a):
                    onetime_expence = one_time_expense
                else:
                    onetime_expence = 0
                annual_savings = a_s - a_e - onetime_expence

                networth = round(networth * (1 + inv_ret)) + annual_savings
            if networth>0:
                if r_a<=80:
                    print('User should  retire at',r_a)
                else:
                    print('User cant sustain by increasing hi retirement age')
            else:
                # print(networth)
                return end_worth_on_increasing_retirement(r_a+1)

        def end_worth_reduce_expense(exp_inc):
            p_a = present_age
            r_a=retirement_age
            a_s = annual_salary
            a_e = annual_expence
            sal_inc = salary_increment_rate / 100
            inv_ret = return_rate_on_investment / 100
            networth = net_worth
            for i in range(80 - p_a):
                if i < (r_a - p_a):
                    a_s = round(a_s * (1 + sal_inc))
                else:
                    a_s = 0
                a_e = round(a_e * (1 + exp_inc))
                if (i == age_at_one_time_expense - p_a):
                    onetime_expence = one_time_expense
                else:
                    onetime_expence = 0
                annual_savings = a_s - a_e - onetime_expence

                networth = round(networth * (1 + inv_ret)) + annual_savings
            if networth > 0:
                print('Or user should reduce his expenses to', round(exp_inc*100,3),'percent')
            else:
                # print(networth)
                return end_worth_reduce_expense(exp_inc - 0.005)

        def end_worth_inc_ROI(inv_ret):
            p_a = present_age
            r_a=retirement_age
            a_s = annual_salary
            a_e = annual_expence
            sal_inc = salary_increment_rate / 100
            exp_inc = expence_increment_rate / 100
            networth = net_worth
            for i in range(80 - p_a):
                if i < (r_a - p_a):
                    a_s = round(a_s * (1 + sal_inc))
                else:
                    a_s = 0
                a_e = round(a_e * (1 + exp_inc))
                if (i == age_at_one_time_expense - p_a):
                    onetime_expence = one_time_expense
                else:
                    onetime_expence = 0
                annual_savings = a_s - a_e - onetime_expence

                networth = round(networth * (1 + inv_ret)) + annual_savings
            if networth > 0:
                print('Or user should try to increase his ROI to',round(inv_ret*100,3),'percent')
            else:
                # print(networth, round(inv_ret,3))
                return end_worth_inc_ROI(inv_ret + 0.005)
        end_worth_on_increasing_retirement(retirement_age)
        end_worth_reduce_expense(expence_increment_rate/100)
        end_worth_inc_ROI(return_rate_on_investment/100)

end_worth(present_age,retirement_age,annual_salary,annual_expence,salary_increment_rate,expence_increment_rate,return_rate_on_investment,net_worth)
