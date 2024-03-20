#python script that determines if you entered and even or odd number

def main():
  def determine_num_of_nums():
    num_of_nums = int(input('Amount of numbers to determine: '))
    return num_of_nums

    
  def gather_nums():
      nums_list = []
      for x in range(determine_num_of_nums()):
        nums_list.append(int(input('Number to be determined: ')))
      return nums_list
    
  def calculat_and_print():
      for num in gather_nums():
        if num % 2 == 0:
          print('Even')
        else:
          print('Odd')
          
  calculat_and_print()

main()
