# Parens Valid
# Create a function that, given an input string (str), returns a boolean whether parentheses in the string are valid. Valid sets of parentheses always open before they close.

# For example, for "Y(3(p)p(3)r)s", return true.
# Given "N(0(p)3", return false: not every parenthesis is closed.
# Given "N(0)t )0(k", return false, because the second ")" is premature: there is nothing open for it to close.

def parens(string):
    newlist = []
    for i in range(0, len(string)-1):
        if i == ( || { ||[:
            newlist.append(i)
            if 






# Braces Valid
# Given a sequence of parentheses, braces and brackets, determine whether it is valid.
# Example: "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!" => true.
# "D(i{a}l[ t]o)n{e" => false.
# "A(1)s[O (n]0{t) 0}k" => false