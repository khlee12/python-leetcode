'''
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses/
'''
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # save output at a set
        # loop each address
        # split using '@'
        # get every char
        # if char is . , do nothing(continue)
        # if char is +, break, 
        # else put into temporary variable which saving local value
        if emails is None:
            return
        output = set()
        for i in range(len(emails)):
            each_email = emails[i]
            local_name, postfix = (each_email.split('@'))[0], (each_email.split('@'))[1]
            actual_local_name = ''
            for i in range(len(local_name)):
                each_char = local_name[i]
                if each_char == '.':
                    continue
                elif each_char == '+':
                    break
                else:
                    actual_local_name += each_char
            output.add(actual_local_name+postfix)
        return len(output)
    
