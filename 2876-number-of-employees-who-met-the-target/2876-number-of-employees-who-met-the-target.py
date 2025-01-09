class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        result = 0

        for emp in hours:
            if emp >= target:
                result += 1
                
        return result