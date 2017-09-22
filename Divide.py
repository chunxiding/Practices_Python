import sys
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        """
        exceed timelimit
        result = 0
        sign = 1
        dd = abs(dividend)
        ds = abs(divisor)
        
        if dividend > 0 and divisor < 0:
            sign = -1
        if dividend < 0 and divisor > 0:
            sign = -1
        
        while(dd >= dds):
            dd -= dds
            result += 2
            if result > sys.maxsize:
                return sys.maxsize
        
        if dd > ds:
            result += 1
        if result > sys.maxsize:
                return sys.maxsize
        
        return sign*result
        
        need to find a DP solution
        bitwise operator: 
        << shift binary expression left by one digit
        ***same as times 2
        >> shift binary expression right by one digit
        ***same as divided by 2
        """
        
        dd = abs(dividend)
        ds = abs(divisor)
        result = 0
        tempr = 1
        temps = ds
        
        while dd>=ds:
            if dd >= temps:
                dd -= temps
                result += tempr
                temps <<= 1
                tempr <<= 1
            else:
                temps >>= 1
                tempr >>= 1
                
        if dividend > 0 and divisor < 0:
            result = -result
        if dividend < 0 and divisor > 0:
            result = -result
            
        return  min(max(-2147483648,result),2147483647)
