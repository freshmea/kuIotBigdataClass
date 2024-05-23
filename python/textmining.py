from collections import OrderedDict, defaultdict


def main():
    text = """text mining consists in using Machine Learning for text analysis. Discover all you need to know: definition, functioning, techniques, advantages, use cases... Modern companies have a lot of data on their customers or their business sector. New digital technologies such as social networks, e-commerce, or mobile applications for smartphones give access to a vast amount of information.
By analyzing this data, it is possible to discover untapped opportunities or alarming problems that need to be addressed urgently. However, some types of data are more difficult to exploit than others.

Data from social networks or other websites are mainly texts: comments on posts, product reviews, and complaints on community forums…"""

    word_count = defaultdict(lambda: 0)
    for word in text.split():
        word_count[word] += 1
    print(word_count)
    for i, v in OrderedDict(sorted(word_count.items(), key=lambda t: t[1], reverse=True)).items():
        print(i, v)
if __name__ == '__main__':
    main()
