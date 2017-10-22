# irkcmd
A IRKit control CLI Script.
This script works only private networks. (Design without using external server)

## Requirements
tested with Linux (Raspberry pi) and macOSX 10.13

* python 2.7.x

## How to Install
* Install PIP.
* Clone this repository.
```
git clone https://github.com/thesaitama/irkcmd.git
```   
* Install dependencies.
```
cd irkcmd
pip install -r requirements.txt
```
* Configure JSON Settings file.
  + Rename sample JSON File.
  ```
  mv irkconfig.sample.json irkconfig.json
  ```
  + Edit irkconfig.json
  ```
  {
    {
    "<NAME>": {
        "memo": "<MEMO>",
        "target": "<IRKIT_HOST>", "format": "raw", "freq": 38,
        "data": [<DATA>]
    }
  }
  ```
  e.g. 
  ```
  "l-aircon-on": {
        "memo": "AirConditioner - On",
        "target": "192.168.1.141", "format": "raw", "freq": 38,
        "data": [815,904,2537,904,2537,904,815,904,815,904,815,904,2537,904,2537,904]
   },
   "l-aircon-off": {
        "memo": "AirConditioner - Off",
        "target": "192.168.1.141", "format": "raw", "freq": 38,
        "data": [2537,873,873,873,2537,873,873,873,873,873,873,873,2537,873,2537,873]
    }
  ```

## How to Operate
### Show command list
```
python irkcmd.py cmdlist
```
command list will be displayed:
```
l-aircon-off        : AirConditioner - Off
l-aircon-on         : AirConditioner - On
```

### Run command
```
python irkcmd.py <cmd>
```

## Links
* IRKit
 http://getirkit.com/

## License
MIT

## Maintainer
* Kazuhiro Komiya

