class Solution(object):
    """docstring for Solution"""
    def __init__(self):
        pass
        

    def build_fs(self, string):
        fs = {}
        files = string.split('\n')

        current_path = []
        for file in files:
            indentation = 0
            while '\t' in file:
                indentation += 1
                file = file[1:]

            current_node = fs
            for subdir in current_path[:indentation]:
                current_node = current_node[subdir]

            if '.' in file:
                current_node[file] = True
            else:
                current_node[file] = {}

            current_path = current_path[:indentation]
            current_path.append(file)

        return fs

    def longest_path(self, fs):
        paths = []
        for key, node in fs.items():
            if node == True:
                paths.append(key)
            else:
                paths.append(key+'/'+self.longest_path(node))

        paths = [path for path in paths if '.' in path]
        if paths:
            return max(paths, key=lambda x: len(x))
        else:
            return ''

    def solution(self, string):
        return len(self.longest_path(self.build_fs(string)))