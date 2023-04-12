import sys
import math

BITS_PER_SYMBOL_TABLE = {
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
NUMEROLOGY_TABLE_KHZ = {
    0: 15,
    1: 30,
    2: 60,
    3: 120
}
SLOT_TIME_MS = 0.5
RESOURCE_BLOCKS_GUARDS = 4
SLOT_SUBCARIERS = 12
SLOT_SYMBOLS = 14

def throughput5g(input):
    slot_subcarier_frequency_khz = NUMEROLOGY_TABLE_KHZ.get(
        input.get('numerology'))
    resource_blocks = math.floor((input.get('bandwidth') * 1000) / (
        SLOT_SUBCARIERS * slot_subcarier_frequency_khz) - RESOURCE_BLOCKS_GUARDS)

    data_symbols = SLOT_SYMBOLS - 3  # 2 slots for DRMS and 1 for PDCCH
    bits_per_symbol = BITS_PER_SYMBOL_TABLE.get(input.get('modulation_order'))
    bits_per_slot = math.floor(
        SLOT_SUBCARIERS * data_symbols * bits_per_symbol)

    # 1600 downlink - 1500 uplink
    link_slots = 1600 if input.get('link_type') == 0 else 1500

    return math.floor(
        ((bits_per_slot * resource_blocks * link_slots *
         input.get('mimo_layers')) / 1024) / 1024
    )


def validate(input: dict):
    if (input.get('numerology') < 0 or input.get('numerology') > 4):
        raise Exception('invalid numerology, it should be between 1 and 4')
    if (input.get('modulation_order') < 0 or input.get('modulation_order') > 27):
        raise Exception(
            'invalid modulation order, it should be between 1 and 27')
    if (not [20, 50, 100, 400].__contains__(input.get('bandwidth'))):
        raise Exception('invalid bandwidth, valid is 20, 50, 100 or 400 MHz')
    if (not [1, 2, 4].__contains__(input.get('mimo_layers'))):
        raise Exception('invalid mimo layers, valid are: 1, 2 or 4')


def calculate_throughput(args) -> int:
    if (len(args) < 4):
        raise Exception('invalid number of arguments')
    input = {
        'numerology': args[0],
        'modulation_order': args[1],
        'bandwidth': args[2],
        'mimo_layers': args[3],
        'link_type': args[4] if len(args) == 5 else 0
    }
    validate(input)
    return throughput5g(input)


if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        input_as_integers = list(map(lambda i: int(i),  args))
        print(f'{calculate_throughput(input_as_integers)}')
    except Exception as e:
        print(e)
