def lst1():
    with open('1.txt', 'r') as f:
        data=f.readlines()
        for line in data:
            odom01=line.split(',')
    return odom01
def main():
    print(lst1())

if __name__ == '__main__':
    main()
