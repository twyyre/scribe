
import os


class Scribe:
    def __init__(self):
        self.internal_path = "logs/"
        self.relative_path = True
        self.f = None
        path = file_path = os.path.dirname(os.path.abspath(__file__))+'/'
        self.page_template = self.f_read(_filename=path+"/templates/page_template.html")
        self.scribble_template = self.f_read(_filename=path+"/templates/scribble_template.html")
        self.scribe_count = 0

    def new_page(self, _filename: str, _type: str=".html"):
        import datetime
        date = self.get_time()
        filename = f"logs/{_filename}{date}.html"
        self.f_write(_filename=filename, _content=self.page_template)

        self.f = filename
        
        self.fill_argument("{{page_name}}", "report", self.f)
        self.fill_argument("{{page_date}}", self.get_time(), self.f)
        self.fill_argument("{{column_1}}", "#", self.f)
        self.fill_argument("{{column_2}}", "automated step", self.f)
        self.fill_argument("{{column_3}}", "expected result", self.f)
        self.fill_argument("{{column_4}}", "actual result", self.f)

        return self.f
    
    def find_line(self, _filename, _content):
        with open(_filename) as f:
            for (i, line) in enumerate(f):
                if _content in line:
                    return i
            return False

    def get_arguments(self, _template):
        template = self.f_read(_template)
        openning_bracket_list = []
        closing_bracket_list = []

        for char in template:
            if(char == "{{"):
                openning_bracket_list.append(char)
                continue
            if(char == "}}"):
                closing_bracket_list.append(char)
                continue

    def arg_replace(self, _file, _arg, _value):
        return _file.replace(_arg, _value)

    def record(self, _content):
        pass

    def recall(self, _filename):
        self.f = self.f_read(_filename=_filename)

    def modify(self, _filename, _content):
        self.f = self.f_read(_filename=_filename)

    def fill_argument(self, _arg, _value, _file):
        file_content = self.f_read(self.f)
        file_content = self.arg_replace(file_content, _arg, _value)
        self.f_write(self.f, file_content)
    
    def scribble(self, _arg, _value):
        file_content = self.f_read(self.f)
        file_content = self.arg_replace(file_content, _arg, _value)
        self.f_write(self.f, file_content)

    def f_write(self, _filename, _content, _encoding="utf-8-sig"):
        file = open(_filename, "w", encoding=_encoding)
        file.write(str(_content))
        file.close()

    def f_append(self, _filename, content, encoding="utf-8-sig"):
        file = open(_filename, "a", encoding=encoding)
        file.write(str(content))
        file.close()

    def f_read(self, _filename, encoding="utf-8-sig"):
        file = open(_filename, "r", encoding=encoding)
        content = file.read()
        file.close()
        return content

    def f_read_int(self, _filename):
        file = open(_filename, "r")
        content = int(file.read())
        file.close()
        return content

    def f_read_once(self, _filename):
        file = open(_filename, "r")
        content = file.read()
        file.close()
        return content

    def f_read_lines(self, _filename):
        file = open(str(_filename))
        lines = file.readlines()
        for line in lines:
            lines[lines.index(line)] = line.replace("\n", "")
        return lines

    def get_time(arg=None):
        import datetime
        return f" {datetime.date.today().year}-{datetime.date.today().month}-{datetime.date.today().day}-{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}"
