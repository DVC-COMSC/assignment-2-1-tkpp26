def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males = int(input("Enter the number of males: "))
    num_females = int(input("Enter the number of females: "))
    total = num_females + num_males
    m_perc = num_males / total * 100
    f_perc = num_females / total * 100

    print(f"The total number of students    \t {total}")
    print(f"The number of males and females \t {num_males}    \t {num_females}")
    print(f"The total number of students    \t {m_perc:.2f} % \t {f_perc:.2f} %40")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
