import coin

def main():
    my_coin = coin.Coin()

    print('This side up is ', my_coin.get_sideup())

    #toss the coin
    print('I am tossing the coin tens times...')
    for count in range(10):
        my_coin.toss()
        print('This side up is ', my_coin.get_sideup())


main()