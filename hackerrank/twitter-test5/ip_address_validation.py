"""
Given a list of IP addresses, check whether each is a valid IPv4/IPv6 address.

Return a list of outputs like 'Ipv4' is address is Ipv4, 'Ipv6' if address is IPv6,
'Neither' if it is none.

Each oputput in returned list corresponds to corresponding input in given address list.

Assume no trailing or leading spaces in given input.

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Hackerrank.com","Twitter.com"]
__status__  = "Prototype"


def  checkIP(ip):
    result = []
    for addr in ip:
        if is_ipv4_addr(addr):
            result.append("IPv4")
            continue;
        elif is_ipv6_address(addr):
            result.append("IPv6")
        else:
            result.append("Neither")
         
    return result

def is_ipv4_addr(addr):
  
    parts = addr.split('.')
    accepted_chars = {'0','1','2','3','4','5','6','7','8','9'}
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        
        if len(part) > 3:
            return False
        
        for char in part:
            if char not in accepted_chars:
                return False      
        
        if  int(part) < 0 or int(part) > 255:
            return False
        
    return True

def is_ipv6_address(addr):
    
    parts = addr.split(':')
    
    accepted_chars = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
    
    if len(parts) != 8:
        return False
    
    for part in parts:
        if len(part) > 4:
            return False
       
        for char in part:
            if char not in accepted_chars:
                return False
    
    return True



if __name__ == '__main__':
    addresses = ['This is nothing','10.1.1.2']
    print(checkIP(addresses))
