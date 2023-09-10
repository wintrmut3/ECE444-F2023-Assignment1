class utils:
  def reversed(self, n:int) -> int:
    # for the negative case, I will add back the sign at the end
    # idea for casting back and forth from string with reverse slice is from https://www.upgrad.com/blog/how-to-reverse-a-number-in-python/; I only used the sentence "At first, the integer can be converted into a string. The string can then be reversed and then converted back into an integer."
    
    if not isinstance(n, int): # ref https://note.nkmk.me/en/python-check-int-float/
      return -1

    is_neg = n < 0
    rev_str = str(abs(n))[::-1]
    return int(('-' if is_neg else '') + rev_str) 
    

  def formatter(self, n:int) -> int:
    if not isinstance(n, int): # ref https://note.nkmk.me/en/python-check-int-float/
      return -1, -1
    return bin(n), oct(n)

