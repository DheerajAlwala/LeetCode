#Average Salary Excluding the Minimum and Maximum Salary
#Given an array of unique integers salary where salary[i] is the salary of the employee i.Return the average salary of employees excluding the minimum and maximum salary.
#Input: salary = [4000,3000,1000,2000]
#Output: 2500.00000
class Solution(object):
    def average(self, salary):
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary)/float(len(salary))
        
