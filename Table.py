from itertools import combinations


def common_trans(previous, item_set):
    flag = True
    trans = set()
    for record in previous.table:
        if record.set_item <= item_set:
            if flag:
                trans = record.set_freq
                flag = False
            else:
                trans = trans.intersection(record.set_freq)
    return trans


class Iteration:
    def __init__(self):
        self.table = list()

    def add(self, item, trans):
        for i in self.table:
            if item == i.set_item:
                i.add_trans(trans)
                return
        new_record = ItemSet(item)
        new_record.add_trans(trans)
        self.table.append(new_record)

    def print(self):
        print("\t<========================== Support Items ===============================>\n")
        for record in self.table:
            print("\t\t", record.set_item, "\t>>\t", record.set_freq)
        print("\n\t<========================== it's good :)  ===============================>")

    @staticmethod
    def next_iteration(previous, satisfy_item, iter_nums):
        next_iterate = Iteration()
        for subset in combinations(satisfy_item, iter_nums):
            trans = common_trans(previous, set(subset))
            record = ItemSet(set(subset), trans)
            next_iterate.table.append(record)
        return next_iterate


class ItemSet:
    def __init__(self, set_item, set_freq=None):
        self.set_item = set_item
        self.set_freq = set()
        if set_freq is not None:
            self.set_freq = set_freq

    def add_trans(self, trans_number):
        self.set_freq.add(trans_number)


class Conf:
    def __init__(self, satisfy_supp, satisfy_item):
        self.table = list()
        size = len(satisfy_supp.table[0].set_item)
        for i in satisfy_supp.table:
            for j in range(1, size):
                for subset in combinations(i.set_item, j):
                    s = i.set_item.difference(set(subset))
                    s_freq = len(i.set_freq)
                    f = set(subset)
                    f_freq = len(common_trans(satisfy_item, f))
                    conf = s_freq / f_freq * 100
                    new_record = ConfItem(s, f, conf)
                    self.table.append(new_record)

    def print(self):
        print("\t<========================== Confides Items ===============================>\n")
        for record in self.table:
            print("\t\t", record.s, "\t=>\t", record.f, "\t=\t", record.conf, " %")
        print("\n\t<========================== it's good :)  ===============================>")


class ConfItem:
    def __init__(self, s, f, conf):
        self.s = s
        self.f = f
        self.conf = conf
