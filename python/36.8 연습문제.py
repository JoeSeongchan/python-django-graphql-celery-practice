class AdvancedList(list):
    def replace(self,old,new):
        while old in self:
            self[self.index(old)] = new

        # while self.count(old) != 0:
        #     self[self.index(old)] = new

