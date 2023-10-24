class ReadFile:
    filepath = 'archive/links.txt'

    @staticmethod
    def read(file_with_urls=None):
        if file_with_urls:
            ReadFile.filepath = file_with_urls

        with open(ReadFile.filepath) as files:
            content = files.readlines()
        return content
