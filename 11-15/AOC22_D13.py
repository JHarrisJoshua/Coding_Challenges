from ast import literal_eval
from collections import deque


class PacketSort(list):
    def __lt__(packet_1, packet_2):
        return compare_packets(packet_1, packet_2)


def distress_signal(file_name):
    packets, check_sum, i = [[[6]], [[2]]], 0, 1
    with open(file_name, 'r') as infile:
        packet_queue = deque([literal_eval(line.strip())
                              for line in infile if line != '\n'])
    while packet_queue:
        [packets.append(packet_queue.popleft()) for _ in range(2)]
        if compare_packets(packets[-2], packets[-1]):
            check_sum += i
        i += 1
    packets.sort(key=PacketSort)
    signal_idx = packets.index([[2]]), packets.index([[6]])
    return check_sum, packets, (signal_idx[0]+1) * (signal_idx[1]+1)


def compare_packets(line_1, line_2, j=0) -> bool | None:
    while j < len(line_1) or j < len(line_2):
        if j >= len(line_1) or j >= len(line_2):
            return True if j >= len(line_1) else False
        if type(line_1[j]) == int and type(line_2[j]) == int:
            if line_1[j] != line_2[j]:
                return True if line_1[j] < line_2[j] else False
        elif type(line_1[j]) == list or type(line_2[j]) == list:
            cmp_1 = line_1[j] if type(line_1[j]) == list else [line_1[j]]
            cmp_2 = line_2[j] if type(line_2[j]) == list else [line_2[j]]
            if (result := compare_packets(cmp_1, cmp_2)) in [True, False]:
                return True if result else False
        j += 1


if __name__ == '__main__':
    sum_check, sorted_packets, signal = distress_signal("AOC22_D13_inp.txt")
    print(f'Check Sum: {sum_check} \nSignal: {signal}')
