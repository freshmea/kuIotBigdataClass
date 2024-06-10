import pandas as pd


def main():
    edges = pd.DataFrame({'source': [0, 1, 2],
                          'target': [2, 2, 3],
                          'weight': [3, 4, 5],
                          'color': ['red', 'blue', 'blue']})
    print(edges.dtypes)
    print(pd.get_dummies(edges, dtype=int))

    weight_dict = {3: 'M', 4: 'L', 5: 'XL'}
    edges["weight_sign"] = edges["weight"].map(weight_dict)
    print(edges["weight_sign"])
    weight_sign = pd.get_dummies(edges["weight_sign"], dtype=int)
    print(weight_sign)
    print(pd.concat([edges, weight_sign], axis=1))

if __name__ == '__main__':
    main()
