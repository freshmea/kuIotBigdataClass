import re
import urllib.request


def main():
    url = "https://www.google.com/googlebooks/uspto-patents-grants-text.html"

    html = urllib.request.urlopen(url)
    html_contents = str(html.read().decode("utf8"))
    url_list = re.findall(r"(http)(.+)(zip)", html_contents)
    for url in url_list:
        full_url = "".join(url)
        print(full_url)
        try:
            fname, header = urllib.request.urlretrieve(full_url, full_url.split("/")[-1])
            print(f"End Download {fname}")
        except:
            pass


if __name__ == '__main__':
    main()
