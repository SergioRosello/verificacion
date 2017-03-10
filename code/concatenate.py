# -*- coding: utf-8 -*-
import errno


def concatenate(*args):
    chain = ''
    output = None
    if len(args) < 2:
        output =  errno.EPERM
    if len(args) > 10:
        output = errno.E2BIG
    for string in args:
        if not isinstance(string, str):
            output = errno.EINVAL
        elif len(string) > 10:
            output = errno.EINVAL

    if output == None:
        for string in args:
            chain = chain + string
        output = chain.replace(" ", "")


    return output


    for string in args:
        string = string + string[i]
        i


if __name__ == "__main__":
    concatenate('hola', 'hola')