import numpy as np
import pandas as pd


def main():
    viagra_spam = {
        "viagra": [1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1],
        "spam":   [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1]
    }
    df = pd.DataFrame(viagra_spam)

    # np_data = df.values
    np_data = df.to_numpy()
    print(type(df), type(np_data))

    
    # P(viagra)
    p_viagra = sum(np_data[:,0]) / len(np_data[:,0])
    print(f"p_viagra: {p_viagra}")
    
    # P(spam)
    p_spam = sum(np_data[:,1]) / len(np_data[:,1])
    print(f"p_spam: {p_spam}")
    
    # P(viagra intersection spam)
    p_viagra_inter_spam = sum(np_data[:,0] & np_data[:,1]) / len(np_data[:,0])
    print(f"p_viagra_inter_spam: {p_viagra_inter_spam}")
    
    # P ( (~viagra) intercection spam)
    p_not_viagra_inter_spam = sum((~np_data[:,0]) & np_data[:,1]) / len(np_data[:,0])
    print(f"p_not_viagra_inter_spam: {p_not_viagra_inter_spam}")
    
    # P(viagra|spam)
    p_via_cap_spam = sum(np_data[:,0] & np_data[:,1]) / sum(np_data[:,1])
    print(f"p_via_cap_spam: {p_via_cap_spam}")
    
    # P(spam| (~viagra))
    p_spam_cap_not_viagra = p_not_viagra_inter_spam / (1-p_viagra)
    print(f"p_spam_cap_not_viagra: {p_spam_cap_not_viagra}")
    
if __name__ == "__main__":
    main()
