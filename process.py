# opens txt file
log_file = open("um-server-01.txt")

# function declaration


def sales_reports(log_file):
    # for loop returns item in file not index
    for line in log_file:
        # strip unnececary characters from data
        line = line.rstrip()
        # select first 3 char of each line
        day = line[0:3]
        # select day
        if day == "Mon":
            # display data on that day
            print(line)


sales_reports(log_file)
