import requests,os,time,sys
from requests import ConnectionError
# import ugex gamnteng:v

'''

	~ Coded By Ugex95.
	-------
	Pastebin   :  /u/Ugex95
	Github     :  Din-zUgex95
	Instagram  :  @ugex95       !!!
	Youtube    :  Din-zUgex95   !!!

	Heh...


'''


os.system('clear')

### Ie Dev_key na pake akun temp-mail ehehe:' ###
### jadi lamun dah limit bikin akun lagi oghe ###
### pake temp-mail:v                          ###
devKey = '8QR3_43BbKYWfYmYcECz7PB6_h85OaSW'

### Nulis ###
def wrt(teks, tme):
	for i in teks + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(tme)

### Kolor ###
a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

### WM Ugex95 ###
banner = f'''{p}
─────────────────────────────────────
{bn}  PASTEBIN GUEST UPLOADER BY Ugex95  {o}
{p}─────────────────────────────────────
  {m}- {p}Github {m}: {a}Din-zUgex95
  {m}- {p}Instagram {m}: {a}@ugex95
{p}─────────────────────────
'''

### List ###
format = f'''
{p}[{m}1{p}] PYTHON  {p}[{m}4{p}] JAVASCRIPT
{p}[{m}2{p}] PHP     {p}[{m}5{p}] BASH
{p}[{m}3{p}] HTML    {p}[{m}0{p}] None {m}( {a}Default {m})
'''

expr = f'''
{p}[{m}1{p}] Never       {p}[{m}3{p}] 1 Hour
{p}[{m}2{p}] 10 Minutes  {p}[{m}4{p}] 1 Day
'''

exps = f'''
{p}[{m}1{p}] Public  {p}[{m}2{p}] Unlisted
'''

### Ngadata ###
def main():
	os.system('clear')
	try:
		wrt(banner,0.003)
		file = input(f' {m}- {p}File {m}:{p} ')
		name = input(f' {m}- {p}Paste Name {m}:{p} ')
		print(format)
		formatFile = input(f' {m}- {p}Format File {m}:{p} ')
		print(expr)
		expire = input(f' {m}- {p}Expiration {m}:{p} ')
		print(exps)
		exposure = input(f' {m}- {p}Exposure {m}:{p} ')
		readFile = open(file,'r').read()
		
		### Paste_format ###
		if formatFile =='1':
			_format = 'python'
		elif formatFile =='2':
			_format = 'php'
		elif formatFile =='3':
			_format = 'html5'
		elif formatFile == '4':
			_format = 'javascript'
		elif formatFile =='5':
			_format = 'bash'
		elif formatFile =='0':
			_format = ''
		else:
			_format = ''
		
		### Paste_Expired ###
		if expire == '1':
			xpr='Never'
			_expire = 'N'
		elif expire == '2':
			xpr='10 Minutes'
			_expire = '10M'
		elif expire == '3':
			xpr='1 Hour'
			_expire = '1H'
		elif expire == '4':
			xpr='1 Day'
			_expire = '1D'
		else:
			xpr='1 Hour'
			_expire = '1H'
		
		### Paste_Visibility ###
		if exposure == '1':
			xps='Public'
			_exposure = '0'
		elif exposure == '2':
			xps='Unlisted'
			_exposure = '1'
		else:
			xps='Unlisted'
			_exposure = '1'
		
	### Didie Errorna ###
	except FileNotFoundError:
		wrt(f'\n{p}[{m}!{p}] {a}{file} {p}File Not Found\n',0.01)
		exit()
	except KeyboardInterrupt:
		wrt(f'\n{p}[{m}!{p}] Exit\n',0.01)
		exit()
	except: # tololl
		pass
	try:
		Ugex95 = {
			'api_option':'paste',
			'api_dev_key': devKey,
			'api_paste_code': readFile,
			'api_paste_name': name,
			'api_paste_format': _format,
			'api_paste_expire_date': _expire,
			'api_paste_private': _exposure
			}
			
		url = 'https://pastebin.com/api/api_post.php'
		resp = requests.post(url,data=Ugex95).text

		add = open('pasteList.txt','a')
		add.write('\n- My Paste Link : '+resp)
		add.close()

	except ConnectionError:
		wrt(f'\n{p}[{m}!{p}] {k}Connection Error\n',0.01)
		exit()
	except KeyboardInterrupt:
		wrt(f'\n{p}[{m}!{p}] Exit\n',0.01)
		exit()
	except:
		pass

	if _format =='':
		_format = 'None'
	if name =='':
		name='Untitled'
	
	hasil = f'''
{p}─────────────────────────────────────────
{bn}       PASTEBIN UPLOADER BY Ugex95       {o}
{p}─────────────────────────────────────────
 {m}• {p}Paste File {m}:{p} {file}
 {m}• {p}Paste Name {m}:{p} {name}
 {m}• {p}Paste Format {m}:{p} {_format}
 {m}• {p}Paste Expiration {m}:{p} {xpr}
 {m}• {p}Paste Visibility {m}:{p} {xps}
 {m}• {p}List Of Link  {m}:{a} ./pasteList.txt

 {m}• {p}Link {m}:{b} {resp}

{p}─────────────────────────────────────────
'''
	### Nampilken Hasilna ###
	os.system('clear')
	wrt(hasil,0.0001)
	hah = input(f'{m}- {p}Pastebin Again{m}({a}y{p}/{a}n{m}) {m}:{p} ')
	if hah == 'y':
		main()
	elif hah == 'n':
		wrt(f'\n{p}[{m}!{p}] Exit\n',0.01)
		exit()
	else:
		wrt(f'\n{p}[{m}!{p}] Exit\n',0.01)
		exit()
	

main()

# Rapih
	# Ti web API pastebin

	# https://pastebin.com
	# https://pastebon.com/u/Ugex95
