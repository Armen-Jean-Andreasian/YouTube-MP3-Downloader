class ReadFile:
    filepath = 'archive/links.txt'

    @staticmethod
    def read():
        with open(ReadFile.filepath) as files:
            content = files.readlines()
        return content
