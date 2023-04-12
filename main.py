import sys
import math

bits_per_symbol_table = {
    0: 0.2344,
    1: 0.377,
    2: 0.6016,
    3: 0.877,
    4: 1.1758,
    5: 1.4766,
    6: 1.6953,
    7: 1.9141,
    8: 2.1602,
    9: 2.4063,
    10: 2.5703,
    11: 2.7305,
    12: 3.0293,
    13: 3.3223,
    14: 3.6094,
    15: 3.9023,
    16: 4.2129,
    17: 4.5234,
    18: 4.8164,
    19: 5.1152,
    20: 5.332,
    21: 5.5547,
    22: 5.8906,
    23: 6.2266,
    24: 6.5703,
    25: 6.9141,
    26: 7.1602,
    27: 7.4063
}

slot_time_ms = 0.5
slot_subcarier_frequency_khz = 30 
slot_subcariers = 12
bandwidth_mhz = 100 
resource_blocks_guards = 4
resource_blocks = math.floor((bandwidth_mhz * 1000) / (slot_subcariers * slot_subcarier_frequency_khz) - resource_blocks_guards)

modulation_order = 27
data_symbols = 11 # 14 - 2 for DRMS and 1 for PDCCH
bits_per_symbol = bits_per_symbol_table.get(modulation_order)
bits_per_slot = math.floor(slot_subcariers * data_symbols * bits_per_symbol)

link_slots = 1600 # downlink or 1500 uplink 
mimo_layers = 4
throughput = math.floor(((bits_per_slot * resource_blocks * link_slots * mimo_layers) / 1024) / 1024)


def calc():
    print(throughput)


if __name__ == '__main__':
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        print(f"Argument {i:>6}: {arg}")
    calc()
