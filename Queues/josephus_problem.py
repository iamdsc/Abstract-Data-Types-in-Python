from queueADT import Queue
# Implementing Hot-Potato Game / Josephus Problem

def hot_potato(name_list, num):
    q = Queue()
    for name in name_list:
        q.enq(name)
    while q.size() > 1:
        for i in range(num):
            q.enq(q.dq())
        q.dq()

    return q.dq()

print(hot_potato( ["Bill","David","Susan","Jane","Kent","Brad" ], 7))
