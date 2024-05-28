import pandas as pd


def main():
    ex_obj = pd.Series([1, 2, 3, 4, 5])
    print(ex_obj)
    # no index
    ex_obj2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    print(ex_obj2)
    ex_obj2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
    print(ex_obj2)
    ex_obj2 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, index=['a', 'b', 'c', 'd', 'e'])
    print(ex_obj2)
    ex_obj2 = pd.Series([1, 2, 3, 4, 5], index=list('abcde'))
    print(ex_obj2)
    print(f"ex_obj2['a'] : {ex_obj2['a']}")
    print(f"ex_obj[1:4] : \n{ex_obj[1:4]}")

    ex_obj3 = pd.Series({'a':1, 'b':2, 'c':3, 'd':4}, name='example_data', index=list('abcdefghij'))
    print(f"ex_obj3 : \n{ex_obj3}")

if __name__ == "__main__":
    main()
