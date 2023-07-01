'''BusStop I'''
def main(cap):
    '''BusStop I'''
    arrived = 0
    on_board = []
    park = int(input())
    pass_stop = [x for x in range(1, park + 1)]
    allstop = [[] for _ in range(park)]

    for i in allstop:
        get = input().split()
        i.extend(map(int, get))

    allstop.sort()
    for queue in allstop:

        # pull over
        # # # # queue = input().split()
        stop = queue[0]
        pass_stop.remove(int(queue[0]))
        queue.pop(0)

        # get off
        down = on_board.count(stop)
        for i in range(down):
            on_board.remove(stop)
        arrived += down

        # get on
        for i in queue:
            if i == stop:  # not stop sign
                continue

            elif int(i) in pass_stop and len(on_board) < cap:
                on_board.append(i)
            elif len(on_board) == cap:  # full
                break

    print(arrived)


main(int(input()))