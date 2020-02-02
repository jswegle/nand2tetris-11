
class Main(object):
    def __init__(self, filepath):
        self.fileOrDir(filepath)
        for file in self.jackfiles:
            print(file)
            tokenizer = Tokenizer(filepath)
            outputname = filepath.split('.')[0]+"my.xml"
            print(outputname)
            #compEngine = compilationEngine(tokenizer, outputname)

    def fileOrDir(self, filepath):
        if '.jack' in filepath:
            self.jackfiles = [filepath]
        else:
            pathelements = filepath.split('/')
            for root, dirs, files in os.walk(filepath):
                for file in files:
                    if ".jack" in file:
                        self.jackfiles.append(root + '/' + file)






if __name__ == "__main__":
    import os
    import sys
    from JackTokenizer import Tokenizer
    filepath = sys.argv[1]
    Main(filepath)
