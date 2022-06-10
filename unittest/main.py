# assert

if __name__ == '__main__':
    try:
        #assert 5 == 10, 'Sorry but not sorry 5 is not equal to 10.'
        if not 5 == 10:
            raise AssertionError("Sorry but not sorry gg five isn't equal to ten")

        print('>>> The program continues with his excution.')

    except AssertionError as error:
        print(error)


