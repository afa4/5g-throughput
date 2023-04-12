# 5g throuput calculator

### Usage

```shell
python main.py [numerology] [modulation_order] [bandwidth] [mimo_layers] [optional link_type default is downlink - 0]
```

### Example of execution
```txt
numerology = 1
modulation_order = 27
bandwidth = 100 MHz
mimo_layers = 4
link_type = default (0 downlink)
```

```shell
python main.py 1 27 100 4
```

### Expected result

```shell
1627 Mbps
```

### Example of execution with explicit link_type (downlink)

```shell
python main.py 1 27 100 4 0
```

### Example of execution with explicit link_type (uplink)

```shell
python main.py 1 27 100 4 1
```
