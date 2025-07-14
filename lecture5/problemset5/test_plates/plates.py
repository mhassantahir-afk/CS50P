def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # three variables sq for sequence, x for alpha values and n is for numeric values
    sq = 0
    x = 0
    n = 0

    # if statement for checking required conditoons of starting, length of string

    if s.isalnum() and s[0:2].isalpha() and len(s)<=6 and len(s)>=2:

        # x=2 facilitates that s has valid first two entries

        x = 2
        for i in s:

            # using match case to evaluate given entries

            match sq:
                case 2:

                    # for third entry of string it can be number or alpha but should not be 0
                        if i.isdigit() and i != '0':
                            n+=1
                        elif i == '0':
                            break
                        else:
                            x+=1
                case 3:

                    # for forth entry cannot be alpha if third entry is number
                        if i.isalpha() and n>0:
                            break
                        elif i.isdigit():
                            n+=1
                        else:
                            x+=1
                case 4:
                        if i.isalpha() and n>1:
                            break
                        elif i.isdigit():
                            n+=1
                        else:
                            x+=1
                case 5:
                        if i.isalpha() and n>2:
                            break
                        elif i.isdigit():
                            n+=1
                        else:
                            x+=1
            sq+=1


    # if all conditons are true then sum of alpha and num will be equal to length of string
    if x + n == len(s):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
