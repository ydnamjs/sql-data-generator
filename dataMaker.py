from random import randrange

def main():
    f = open("data.txt", "w")

    #//, 'test_title', 'test_first', 'test_last', TO_DATE('2023-04-19 18:36:49', 'YYYY-MM-DD HH24:MI:SS'))

    title_bank = ["King", "Queen", "Manager", "CEO", "Founder", "Salesman", "Fashion-designer", "Teacher", "Pirate", "Cowboy"]
    first_bank = ["bert", "Fred", "Sean", "Piplup", "Ash", "Angelina", "Trinity", "Blair", "Chris", "Gabriella"]
    last_bank = ["smith", "steel", "Gonzales", "Brown", "Bart", "Silber", "Roosen", "Felker", "O'Sullivan", "Sherman"]

    # constants
    prefix = "INSERT INTO \"UD_437_11_8\".\"EMPLOYMENT_UNINDEXED\" (EMPLOYMENT_ID, JOB_TITLE, EMPLOYEE_FIRST, EMPLOYEE_LAST, HIRE_DATE) VALUES ('"
    vS = "', '"
    datePref = "', TO_DATE('"
    dateSuf = "', 'YYYY-MM-DD HH24:MI:SS'));\n"

    counter = 1;

    while(counter < 25000):

        # data field variables
        id = str(counter)
        title = title_bank[randrange(0, 9)]
        first = first_bank[randrange(0, 9)]
        last = last_bank[randrange(0, 9)]
        date = '2023-04-19 18:36:49'

        built_string = prefix + id + vS + title + vS + first + vS + last + datePref + date + dateSuf

        f.write(built_string)

        counter = counter + 1
    
    f.write("\nCOMMIT;")

    f.close()

if __name__ == "__main__":
    main()