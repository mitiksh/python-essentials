if __name__ == "__main__":
    while True:
        altitude = int(input('enter the plane alitude >'))
        if altitude <= 1000:
            print('Safe to land.')
        elif altitude > 1000 and altitude <= 5000:
            print('Bring down to 1000')
        elif altitude > 5000 :
            print('Turn around and try later')


    
