from Table import Iteration
from Table import Conf
from Excel_File import Excel


class Vertical:
    def __init__(self, min_supp, min_conf):
        file = Excel()
        self.min_conf = min_conf
        self.min_supp = int(min_supp / 100 * (file.sheet.nrows - 1))
        self.my_Items = file.get_data()
        print("\n\n\n\t\t\tmin Support = \t", self.min_supp)
        print("\t\t\tmin Confides = \t", self.min_conf, " %")

    def filter_my_item(self, satisfy_item):
        count = 0
        while count < len(self.my_Items.table):
            if self.my_Items.table[count].set_item <= satisfy_item:
                pass
            else:
                self.my_Items.table.pop(count)
            count += 1

    def filter_min_supp(self, iteration):
        count = 0
        satisfy_item = set()
        while count < len(iteration.table):
            if len(iteration.table[count].set_freq) < self.min_supp:
                iteration.table.pop(count)
            else:
                satisfy_item = satisfy_item.union(iteration.table[count].set_item)
                count += 1
        return satisfy_item

    def filter_min_conf(self, conf):
        count = 0
        while count < len(conf.table):
            if conf.table[count].conf < self.min_conf:
                conf.table.pop(count)
            else:
                count += 1

    def support(self):
        previous = Iteration()
        satisfy = set()
        count = 1
        while True:
            if count == 1:
                iteration = self.my_Items
            else:
                iteration = Iteration.next_iteration(self.my_Items, satisfy, count)
            satisfy = self.filter_min_supp(iteration)
            count += 1
            if len(satisfy) < count:
                break
            self.filter_my_item(satisfy)
            previous = iteration
        previous.print()
        return previous

    def do_confides(self, support):
        table = Conf(support, self.my_Items)
        self.filter_min_conf(table)
        table.print()

    def run_algor(self):
        support = self.support()
        self.conf(support)
