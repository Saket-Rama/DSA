class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2=s.lower()
        s3=[]
        for i in s2:
            s3.append(s2.split(i))
        s4=set(s3)
        print(s4)
        # if s3.isalnum()==False:
        # if s3[::-1]==s:
        #     return True
        # else:
        #     return False
if "__name__"=="__main__":
    n=input()
