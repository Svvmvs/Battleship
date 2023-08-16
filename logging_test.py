import logging

#filename is name of file
#filemode is like opening a file
    #using write will start clean each time, appending is probably more proper if you add date/timestamps etc, but idk
#datefmt is i think date formate, so the one i have here is hours:minutes:seconds
#level is what logging level, debug is 2nd lowest, i think it ignores everything below the level
logging.basicConfig(filename="logging_spot.txt", filemode='a', datefmt='%H:%M:%S', level=logging.DEBUG)

logging.info('Starting the math')

print(12*12)

logging.info('the math is done')

logging.info('this is stupid')

logging.info('done?\n')
