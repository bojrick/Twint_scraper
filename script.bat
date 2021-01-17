git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
twint -s "#trump" -g="48.880048,2.385939,1km" -o #trump_chicago.csv --since "2020-01-01 00:00:00" --min-likes 5 --csv
