class day01:
    def __init__(self):
        with open("day01_input.txt", "r") as f:
            self.input = f.readlines()
        for index, line in enumerate(self.input):
            self.input[index] = line.strip()
    
    def run(self):
        self.part1()
        self.part2()

    def part1(self):
        sum = 0
        for line in self.input:
            first=self.get_first_digit(line)
            last = self.get_last_digit(line)
            sum += int(f'{first}{last}')
        print(f'day01:part01 = {sum}')

    def part2(self):
        sum = 0
        for line in self.input:
            altered_line = self.replace_first_word(line)
            altered_line = self.replace_last_word(altered_line)
            first = self.get_first_digit(altered_line)
            last = self.get_last_digit(altered_line)
            sum += int(f'{first}{last}')
            print(f'{line}\n\t{altered_line}\n\t{first}{last}')

        print(f'day01:part02 = {sum}')
    
    def get_first_digit(self, line):
        for char in line:
            if char.isnumeric():
                return char

    def get_last_digit(self, line):
        line = line[::-1]
        return self.get_first_digit(line)

    def replace_first_word(self, line):
        for i in range(0, len(line)):
            if line[i].isnumeric():
                break
            num = self.replace_num(line[i:])
            if num is not None:
                return f'{num}{line}'
        return line
            
    def replace_last_word(self, line):
        for i in range(0, len(line)):
            if line[i].isnumeric():
                break
            num = self.replace_num(line[len(line)-i:])
            if num is not None:
                return f'{line}{num}'
        return line

    def replace_num(self, line):
        if line.startswith("zero"):
            return 0
        elif line.startswith("one"):
            return 1
        elif line.startswith("two"):
            return 2
        elif line.startswith("three"):
            return 3
        elif line.startswith("four"):
            return 4
        elif line.startswith("five"):
            return 5
        elif line.startswith("six"):
            return 6
        elif line.startswith("seven"):
            return 7
        elif line.startswith("eight"):
            return 8
        elif line.startswith("nine"):
            return 9
        else:
            return None