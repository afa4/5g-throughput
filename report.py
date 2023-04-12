from main import calculate_throughput
import random

def random_modulation_order_list():
  return [
      random.randint(0, 27),
      random.randint(0, 27),
      random.randint(0, 27)
  ]


if __name__ == '__main__':
    report = open("report.txt", "a")
    for numerology in [0,1,2,3]:
        for modulation_order in random_modulation_order_list():
            for bandwidth in [20, 50, 100, 400]:
                for mimo_layers in [1, 2, 4]:
                    for link_type in [0, 1]:
                        link_type_str = 'downlink' if link_type == 0 else 'uplink'
                        result = calculate_throughput(
                            [numerology, modulation_order, bandwidth, mimo_layers, link_type])
                        report_line = f'input - numerology: {numerology}, modulation_order: {modulation_order}, bandwidth: {bandwidth}, mimo_layers: {mimo_layers}, link_type: {link_type_str} - calculated 5g throughput: {result} Mbps\n'
                        report.write(report_line)
    report.close()


