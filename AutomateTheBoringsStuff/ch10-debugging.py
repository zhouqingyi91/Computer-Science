import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
# filename='log.txt' can save log info to a file
# logging.disable(logging.DEBUG)
logging.debug('start of program')


def factorial(n):
    logging.debug('start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
        # assert i >= 3, 'i bigger than 2'
    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')
