## Bulk csv-xlsx converter
Bash program for converting sets of .csv files into .xslx (and vice versa)

## Motivation
Although worksheets are far from being the ideal format to work with datasets, it is very common for people related to Data Analysis roles to come across then.

If you have to present a curation of data or a report that generated many .csv files (separated by month, or by sector), this may help you.

## Tech used

<b>Requirements</b>
- [Python 3](https://www.python.org/)
- [pandas](https://pandas.pydata.org/) *

*If you don't have 'pandas' installed, there is a built-in option that will ask if you want to install it via 'pip'.
 
## Installation
Clone this repository

'''
git clone https://github.com/jvtartaglia/csv-xlsx-converter.git
'''

Copy the 'bulk' file into /usr/local/bin/

'''
cp ./csv-xlsx-converter/bulk /usr/local/bin/
'''

Copy the 'bulk_converting.py' file into /usr/local/lib/

'''
cp ./csv-xlsx-converter/bulk_converting.py /usr/local/lib/
'''

## Usage

Call it using the command 'bulk'. It takes 4 arguments in this order:

- Origin file format (csv or xlsx)
- Destination file format (csv or xlsx)
- Origin directory
- Destination directory *

So the final command would look like:

'''
bulk <origin_format> <destination_format> <origin_directory> <destination_directoryr>
'''

*If the destination directory does not exist it will be created.

## Example

Here's an example. Let's take a look at the original directory:

<img src="https://i.imgur.com/PMnqXuV.png" width=50% height=50%> 

<br>Let's say I want to convert .csv into .xslx from '~/Documents/csv/' to '~/Documents/xslx/'.

<img src="https://i.imgur.com/8lNTSUw.png" width=100% height=100%>

<br>The output:

<img src="https://i.imgur.com/cK6NzbY.png" width=100% height=100%>

<br>Now let's see the results:

<img src="https://i.imgur.com/DCpsFRZ.png" width=50% height=50%>