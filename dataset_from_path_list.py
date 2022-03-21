import ijson

class dataset_from_path_list:
    def __init__(self, datapathlist):
        self.datapathlist = datapathlist
        self.objlist = []
        self.obj = None
        self.num = 0

        for datapath in self.datapathlist:
            data = open(datapath, 'r')
            self.objlist.append(ijson.parse(data))

    def __iter__(self):
        self.num = 0
        self.objlist = []
        for datapath in self.datapathlist:
            data = open(datapath, 'r')
            self.objlist.append(ijson.parse(data))
        self.obj = self.objlist[self.num]
        return self

    def __next__(self):
        result = []
        while True:
            temp = next(self.obj)
            if temp is None:
                self.num += 1
                if self.num == len(self.objlist):
                    raise StopIteration
                self.obj = self.objlist[self.num]
                temp = next(self.obj)
            if temp[1] == 'end_array':
                break
            elif temp[1] == 'string':
                result.append(temp[2])
        return result
