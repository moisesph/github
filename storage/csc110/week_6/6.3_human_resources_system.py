#open file

with open("hr_system.txt") as hr_file:
    next(hr_file)

    #read though line by line
    for line in hr_file:

        #Get various parts of the record into variables
        parts = line.split(" ")

        name = parts[0]
        id = int(parts[1])
        job_tittle = parts[2]
        salary = int(parts[3])

        paycheck_amount = salary / 24



        if "engineer" in job_tittle.lower():
            paycheck_amount += 1000

        print(f"{name} (ID: {id}), {job_tittle} - ${paycheck_amount:.2f}")
