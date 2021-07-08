# Bell 4G LTE Data Quote Notifier
### _Using python selenium_

As Bell 4G internet provider has no API for requesting remainnig data quotes, this script is based on selenium on browser headless mode. 

## Dependencies

[`python3`](https://www.python.org/)

`pip3`

`selenium`

[`geckodriver`](https://github.com/mozilla/geckodriver/releases) for Firefox or [`chrome-driver`](https://chromedriver.chromium.org/downloads) for chromium based browsers

Install selenium using pip:
```
pip install selenium
or
pip3 install selenium
```
In order to make this given python script you have to add webdriver to your PATH. In Debian,
```
sudo cp geckodriver /usr/local/bin/
```
For windows make a environmental variable for the webdriver.

#

You can use this script in your polybar by adding this module block and updating directory of the script.
```
[module/bell4g]
type = custom/script

label-font = 2
format-underline = #2aa889
format-background = ${colors.background-alt}
label-padding = 1
label = %output%
exec = echo "<your icon here>"
click-left = python3 /path/to/script/bell-notify.py
```
#### Screenshot
![cool image here](https://i.imgur.com/Gn4bBmw.png)
