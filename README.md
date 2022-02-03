# plr-parser

Get the data from the player file and change the data.

## Getting Started

For decryption and encryption you will need openssl, the player file is encrypted with aes-128-cbc algorithm.

### Prerequisites

You need to install the software:

```
apt install openssl-tools
```

### Installing


It is enough to enter the following command:

```bash
pip install plr-parser
```

or

```bash
pipenv install plr-parser
```

## Running the tests

Importing the library

```python
import plr_parser
```

### Get data

Let's get the data from the player file:

```python
plr_parser.get_data(file_name: str)
```

return data:

```python
version: uint32
company: str
fileType: uint8
name_lenght: uint8
name: str
difficulty: int8
playTime: int
statLife: int32
statLifeMax: int32
statMana: int32
statManaMax: int32
extraAccessory: bool
taxMoney: int32
armor: dict[{'id': int32, 'prefix': uint8}]
acsesuars: dict[{'id': int32, 'prefix': uint8}]
dye: dict[{'id': int32, 'prefix': uint8}]
inventory: dict[{'id': int32, 'stack': int32, 'prefix': uint8, 'favorites': bool}]
```

### Get bytes map

For editing, it is enough to get the raw of all values:

```python
plr_parser.get_bytes_map(file_name: str)
```

return data:

```python
dict[source_bytes, bytes_map]
```

### Save raw bytes to plr file

To get the player's working file, you need to encrypt it again:

```python
plr_parser.save(file_name: str, raw_bytes: bytes)
```

## Authors

* **Li** -  [Telegram](https://t.me/liriondev)

## License

This project is licensed under the GNU General Public License v3.0

 - see the [LICENSE.md](LICENSE.md) file for details
