import math
import sys
from time import process_time
from scapy.layers.inet import *

import helper.ping_helper as ping_helper


if __name__ == '__main__':
    # Variables
    params = sys.argv
    _msg = ''

    host = ping_helper.extract_host(params)
    packet_number = ping_helper.extract_packetsNu(params)
    packet_size = ping_helper.extract_packetsSize(params)
    ttl = ping_helper.extract_ttl(params)
    time_out = ping_helper.extract_time_out(params)

    for _index in range(0, packet_number):
        packet = IP(dst=host, ttl=ttl)/ICMP()
        start_time = process_time()
        reply = sr1(packet, timeout=time_out)
        stop_time = process_time()
        if not (reply is None):
            __time = (stop_time-start_time)
            _msg += ping_helper.formatPacketOutput(
                _index, reply.src, packet_size, ttl, __time)

    if(_msg != ''):
        print(_msg)

    else:
        print('TimeOut ...')
