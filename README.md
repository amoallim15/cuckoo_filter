# Cuckoo Filter: Practically Better Than Bloom

This repository is an implementation of [Cuckoo Filter: Practically Better Than Bloom](Cuckoo_Filter_Practically_Better_Than_Bloom.pdf) paper introduced by Bin Fan, David G. Andersen, Michael Kaminsky, and Michael D. Mitzenmacher.

## Installation
Simply clone this repository via

	git clone https://github.com/AXJ15/Cuckoo-Filter.git

## Example

For testing purposes, simply alter and run the example.py file through:

	python ./example.py

Dataset: 
	
	a = ['hello world', 'hey buddy', 'cuckoo!', 'today']

The outputs:
	
	Example: 

	Is "hello world" in the Cuckoo filter: True
	Is "hey buddy" in the Cuckoo filter: False
	Is "cuckoo!" in the Cuckoo filter: True
	Is "today" in the Cuckoo filter: True

	Cuckoo filter load factor: 6.0%

## Dependencies
- Python 3
- Murmur hashing v3

		pip install mmh3

## Contributors
[Ali Moallim](mailto:axj.159@gmail.com)

## License
This code is licensed under [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.en.html).

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
