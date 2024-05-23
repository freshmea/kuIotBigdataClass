class Note():
    def __init__(self, contents = None):
        self.contents = contents

    def write_contents(self, contents):
        self.contents = contents

    def remove_all(self):
        self.contents = ""

    def __str__(self):
        if self.contents:
            return self.contents
        else:
            return "삭제된 노트입니다."

class NoteBook():
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = dict()

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                if page in self.notes.keys():
                    print("해당 페이지에는 이미 노트가 존재합니다.")
                else:
                    self.notes[page] = note
                    self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")
            return

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())
    
    def get_number_of_all_characters(self):
        all_contents = ""
        for key in self.notes.keys():
            all_contents += self.notes[key].contents
        return len(all_contents)

    def __str__(self):
        return f"{self.title} : {self.get_number_of_pages()}페이지 / {self.get_number_of_all_characters()}글자"

    def print_page(self, page_number):
        if page_number in self.notes.keys():
            print(self.notes[page_number].contents)
        else:
            print("해당 페이지는 존재하지 않습니다.")

    def print_all_page(self):
        for key in self.notes.keys():
            print(f"{key} : {self.notes[key].contents}")

def main():
    note1 = Note()
    note1.write_contents("안녕하세요.")
    note2 = Note("방갑습니다.")
    note3 = Note("하루에 3시간을 걸으면 7년 후에 지구를 한 바퀴 돌 수 있다. -사무엘존슨-")
    note4 = Note("행복의 문이 하나 닫히면 다른 문이 열린다. 그러나 우리는 종종 닫힌 문을 멍하니 바라보다가 우리를 향해 열린 문을 보지 못하게 된다. -헬렌켈러-")
    print(note1)
    print(note2)
    # note2.remove_all()
    print(note2)
    wise_saying_notebook = NoteBook("명언 노트")
    wise_saying_notebook.add_note(note1)
    wise_saying_notebook.add_note(note2)
    wise_saying_notebook.add_note(note3)
    wise_saying_notebook.add_note(note4)
    print(wise_saying_notebook.get_number_of_pages())
    print(wise_saying_notebook.get_number_of_all_characters())

    wise_saying_notebook.remove_note(2)
    print(wise_saying_notebook.get_number_of_pages())
    wise_saying_notebook.add_note(note1, 3)
    print(wise_saying_notebook.get_number_of_pages())
    print(wise_saying_notebook)
    wise_saying_notebook.print_page(1)
    wise_saying_notebook.print_page(2)
    wise_saying_notebook.print_page(3)
    wise_saying_notebook.print_all_page()
    # for i in range(300):
    #     wise_saying_notebook.add_note(note1, i)

if __name__ == '__main__':
    main()
