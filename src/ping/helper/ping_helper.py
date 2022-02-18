
def formatPacketOutput(seq, host, packetSize, ttl, time_out):
    """ Format output message to match linux output """
    print(time_out)
    print("there")
    return str(packetSize) + " bytes from " + host + " seq=" + str(seq) + " ttl=" + str(ttl) + " time=" + str(time_out)[0:5] + " ms"+"\n"


def extract_host(args: list):
    """ Extract host from args """
    return str(args[1]).strip().split('=')[1]


def extract_packetsNu(args: list):
    """ Extract packet number from args """
    return int(str(args[2]).strip().split('=')[1])


def extract_packetsSize(args: list):
    """ Extract packet size from args """
    return int(str(args[3]).strip().split('=')[1])


def extract_ttl(args: list):
    """ Extract ttl from args """
    return int(str(args[4]).strip().split('=')[1])


def extract_time_out(args: list):
    """ Extract timeout from args """
    print(float(str(args[5]).strip().split('=')[1]))
    return float(str(args[5]).strip().split('=')[1])
