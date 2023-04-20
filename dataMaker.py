def main():
    f = open("data.txt", "w")

    #//, 'test_title', 'test_first', 'test_last', TO_DATE('2023-04-19 18:36:49', 'YYYY-MM-DD HH24:MI:SS'))

    first_bank = ["bert", "fred", "Raphael", "Piplup", "Ash", "Angelina", "Trinity", ]

    # constants
    prefix = "INSERT INTO \"UD_437_11_8\".\"EMPLOYMENT_UNINDEXED\" (EMPLOYMENT_ID, JOB_TITLE, EMPLOYEE_FIRST, EMPLOYEE_LAST, HIRE_DATE) VALUES ('"
    vS = "', '"
    datePref = "', TO_DATE('"
    dateSuf = "', 'YYYY-MM-DD HH24:MI:SS'));\n"

    counter = 1;

    while(counter < 10000):

        # data field variables
        id = str(counter)
        title = "Founder"
        first = "Burt"
        last = "Gibbons"
        date = '2023-04-19 18:36:49'

        built_string = prefix + id + vS + title + vS + first + vS + last + datePref + date + dateSuf

        f.write(built_string)

        counter = counter + 1
    
    f.write("\nCOMMIT;")

    f.close()

if __name__ == "__main__":
    main()