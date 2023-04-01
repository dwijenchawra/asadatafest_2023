import concurrent.futures

N = 999999
left_commas = 3
right_commas = 1

DELIMITER = '`'

def process_line(line, i):
    #loop over the line

    lcounter = 0

    for i in range(len(line)):
        if line[i] == ',':
            lcounter += 1
        if lcounter == left_commas:
            lcounter = i
            break
    
    rcounter = 0
    for i in range(len(line)-1, -1, -1):
        if line[i] == ',':
            rcounter += 1
        if rcounter == right_commas:
            rcounter = i
            break
    
    left = line[:lcounter]
    right = line[rcounter+1:]
    middle = line[lcounter+1:rcounter]

    lsplit = left.split(',')
    # lsplit[0] = str(i)


    line = DELIMITER.join(lsplit) + DELIMITER + middle + DELIMITER + right

    line = DELIMITER.join(lsplit) + DELIMITER + middle + DELIMITER + right
    
    # if there are two delimiters in a row, return an empty string
    if DELIMITER + DELIMITER in line:
        return ""
    if DELIMITER not in line:
       return ""
    else:
      return line
    

i = 0
with open('../data/questionposts.csv', 'r') as infile, open('../data/cleanedquestions.txt', 'w') as outfile:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for line in infile:
            if i == 0:
                outfile.write(DELIMITER.join(line.split(",")))
                i += 1
                continue
            if i >= N:
                break
            i += 1
            futures.append(executor.submit(process_line, line, i))
        for future in concurrent.futures.as_completed(futures):
            outfile.write(future.result())
