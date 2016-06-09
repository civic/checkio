def checkio(f,g):

    # Replace with your code
    def h(*args,**kwargs):
        f_ret = None
        g_ret = None
        f_has_error = None
        g_has_error = None
        try:
            f_ret = f(*args,**kwargs)
            if f_ret is None:
                f_has_error = True
        except:
            f_has_error = True
        try:
            g_ret = g(*args, **kwargs)
            if g_ret is None:
                g_has_error = True
        except:
            g_has_error = True

        if f_has_error and g_has_error:
            return (None, 'both_error')
        elif f_has_error:
            return (g_ret, 'f_error')
        elif g_has_error:
            return (f_ret, 'g_error')
        elif f_ret == g_ret:
            return (f_ret, 'same')
        else:
            return (f_ret, 'different')

    return h

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing

    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"

    # Remove odds from list
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"

    # Fizz Buzz
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"

    f = lambda x: abs(x)
    def g(x):
        if x>0:
            return x
        elif x<0:
            return -x
    assert checkio(f,g)(0) == (0, 'g_error')

    def f2(x):
        if x>0:
            return x
        elif x<0:
            return -x
    g2 = lambda x: abs(x)
    assert checkio(f2,g2)(0) == (0, 'f_error')
