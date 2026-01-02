# Exercises: Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. 
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
import statistics
class Stats:
    def __init__(self, count, soma, mini, maxi, rangee, mean, mediana, mode, std, var):
        self.count = count
        self.soma = soma
        self.mini = mini
        self.maxi = maxi
        self.rangee = rangee
        self.mean = mean
        self.medina = mediana
        self.mode = mode
        self.std = std
        self.var = var
    def Count(self):
        return len(self.count)
    def Soma(self):
        return sum(self.soma)
    def Mini(self):
        return min(self.mini)
    def Maxi(self):
        return max(self.maxi)
    def Rangee(self):
        return max(self.maxi) - min(self.mini)
    def Mean(self):
        return statistics.mean(self.mean)
    def Mediana(self):
        return statistics.median(self.medina)
    def Mode(self):
        return statistics.mode(self.mode)
    def Std(self):
        return statistics.stdev(self.std)
    def Var(self):
        return statistics.variance(self.var)


age = Stats(ages,ages,ages,ages,ages,ages,ages,ages,ages,ages)   
print('Count: ', age.Count())
print('Sum: ', age.Soma())
print('Min: ', age.Mini())
print('Max: ', age.Maxi())
print('Range: ', age.Rangee())
print('Mean: ', age.Mean())
print('Median: ', age.Mediana())
print('Mode:', age.Mode())
print('Standard Deviation', age.Std())
print('Variance: ', age.Var())

# Create a class called PersonAccount. 
# It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
    def add_income(self, amount, description):
        self.incomes.append({'amount':amount,'description':description})
    def add_expenses(self, amount, description):
        self.expenses.append({'amount':amount,'description':description})
    def total_income(self):
        soma = 0
        for n in self.incomes:
                for key, value in n.items():
                    if key == 'amount':
                        soma += value
        return soma
    def total_expense(self):
        soma = 0 
        for n in self.expenses:
            for key, value in n.items():
                if key == 'amount':
                    soma += value
        return soma
    def account_balance(self):
        return self.total_income() - self.total_expense()
    def account_info(self):
        return f'{self.firstname} {self.lastname} é o proprietário da conta com {self.account_balance()} mangos '
p = PersonAccount('wagner','moreira')
print(p.firstname)
print(p.lastname)
p.add_income(5000,'salário')
p.add_income(1000,'venda_telefone')
p.add_income(50000,'venda_carro')
print(p.incomes)
print(p.total_income())
p.add_expenses(100,'comida')
p.add_expenses(600,'namorada')
p.add_expenses(40000,'cirugia')
print(p.expenses)
print(p.total_expense())
print(p.account_balance())
print(p.account_info())