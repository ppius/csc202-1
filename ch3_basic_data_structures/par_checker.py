from linear_adts import Stack


def par_checker(symbol_str):
    """
    Check argument string for balanced paranthesis

      >>> par_checker('(())')
      True
      >>> par_checker('())')
      False
      >>> par_checker('((())')
      False
    """
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_str) and balanced:
        symbol = symbol_str[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    return balanced and s.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
