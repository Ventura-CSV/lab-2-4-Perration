def main():
    ##################################################
    # Comlete your code here
    ##################################################
    original_str = "Python Programming"
    sub1 = original_str[: -12]
    sub2 = (original_str.split()[1])
    merged_str = sub2 + sub1 
    
    print(sub2) 
    print(sub1) 
    print(merged_str)
      
    pass


if __name__ == '__main__':
    main()
