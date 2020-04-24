# Zeek Threat Intel Feed Parser
This script parses line-separated indicators from an input file and exports them to an output file in the intelligence data format. You can either run the script manually and enter the required parameters when prompted or pass it parameters if you want to automate the process.

Jump To:

* [Getting Started](https://github.com/CriticalPathSecurity/zeek-threat-intel-parser#getting-started)
* [Usage](https://github.com/CriticalPathSecurity/zeek-threat-intel-parser#usage)

## Getting Started

These instructions will get you a copy of the project up and running.

### Dependencies

* [Python3](https://www.python.org/download/releases/3.0/)

### Installing

Install Python3

```
sudo apt-get install python3
```

Clone the repository into `/opt`

```
cd /opt
git clone https://github.com/CriticalPathSecurity/zeek-threat-intel-parser.git
```

## Usage

Navigate to `/opt/zeek-threat-intel-parser`

```
cd /opt/zeek-threat-intel-parser
```

And then run the parser using one of the following options

### Manual Usage

```
python3 parser.py
```

### Automated Usage

You can also pass arguments directly to the script and bypass user input which allows you to automate the parsing.

Example CRON job to run every nth minute

```
*/N * * * * python3 /opt/zeek-threat-intel-parser/parser.py type source description /input/file/path /output/file/path
```

### Output Format

* Intelligence data format

Example output:

```
#fields	indicator	indicator_type	meta.source	meta.do_notice	meta.desc
indicator	Intel::type	source	F	description
indicator	Intel::type	source	F	description
indicator	Intel::type	source	F	description
indicator	Intel::type	source	F	description
indicator	Intel::type	source	F	description
```
