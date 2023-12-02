
def read_input(): 
    passports = []
    with open("./day4/input.txt") as f: 
        lines = f.readlines()
        passport = {}
        
        for line in lines: 
            if (line == "\n"): 
                passports.append(passport.copy())
                passport = {}
            else: 
                attributes = [att.split(":") for att in line.strip().split(" ")]
                for att in attributes: 
                    passport[att[0]] = att[1]
    return passports
        
def check_keys(required, keys): 
    for r in required: 
        if (r not in keys): return False
    return True 

def puzzle1(input): 
    correct = 0 
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in input: 
        if(check_keys(required, passport)): correct += 1 
    return correct

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def puzzle2(input): 
    correct = 0 
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in input: 
       if(not check_keys(required, passport)): continue 

       for key in passport.keys(): 
            if (key == "byr"): 
                if (int(passport[key]) >= 1920 and int(passport[key]) <= 2002): correct += 1
            elif (key == "iyr"): 
                if (int(passport[key]) >= 2010 and int(passport[key]) <= 2020): correct += 1
            elif (key == "eyr"): 
                if (int(passport[key]) >= 2020 and int(passport[key]) <= 2030): correct += 1
            elif (key == "hgt"): 
                if (passport[key][-2:] == "cm"): 
                    if (int(passport[key][0:-2]) >= 150 and int(passport[key][0:-2]) <= 193): correct += 1
                elif (passport[key][-2:] == "in"): 
                    if (int(passport[key][0:-2]) >= 59 and int(passport[key][0:-2]) <= 76): correct += 1
            elif (key == "hcl"): 
                if (passport[key][0])

    
    return correct 

def main(): 
    input = read_input()

    print("result puzzle 1: ")
    result = puzzle1(input)
    print(result) 
    
    print("\nresult puzzle 2: ")
    result = puzzle2(input)
    print(result) 

if __name__ == "__main__": 
    main()
