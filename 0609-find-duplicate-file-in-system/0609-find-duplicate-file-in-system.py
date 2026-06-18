class Solution(object):
    def findDuplicate(self, paths):
        c_map = defaultdict(list)
        for path in paths:
            parts = path.split(" ")
            root = parts[0]
            for file in parts[1:]:
                name, c = file.split("(")
                c= c[:-1] 
                full_path = root + "/" + name
                c_map[c].append(full_path)
        return [g for g in c_map.values() if len(g) > 1]

        