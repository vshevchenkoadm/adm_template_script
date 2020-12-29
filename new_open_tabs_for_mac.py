import webbrowser
import requests
from bs4 import BeautifulSoup
import browser_cookie3

cj = browser_cookie3.chrome(domain_name='.admitad.com')

#очистка кук
for key in list(cj._cookies):
	if not ((key == '.admitad.com') or (key == '.account.admitad.com')):
		cj.clear(key)
for key in list(cj._cookies['.admitad.com']['/']):
	if not ((key == 'user_default_language') or (key == 'public_role') or (key == 'public_username') or (key == 'section')):
		cj.clear('.admitad.com', '/', key)
for key in list(cj._cookies['.account.admitad.com']['/']):
	if not ((key == 'sessionid') or (key == 'csrf_tn')):
		cj.clear('.account.admitad.com', '/', key)

print('Введите id программы и нажмите "Enter":')
offer_id=int(input())

url = ('https://account.admitad.com/ru/hq/advertiser/advcampaign/?id=%d' % offer_id)

headers = {
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

r = requests.get(url, headers=headers, cookies=cj)
soup = BeautifulSoup(r.text)
url_advertiser_lk = soup.find('a', {'class':'ir action login-as'}).get('href')
url_advertiser_lk_stats = url_advertiser_lk + 'statistics/actions/'

# penkows
webbrowser.open_new_tab('https://account.admitad.com/sid13130/ru/webmaster/websites/22162/offers/%d/##deeplink' % offer_id)

# настройки кампании в hq
webbrowser.open_new_tab('https://account.admitad.com/ru/hq/advertiser/advcampaign/%d/change/' % offer_id)

# логи запросов
webbrowser.open_new_tab('https://account.admitad.com/ru/hq/statistics/orderrequestloghq/?advcampaigns=%d' % offer_id)

# статистика ЛК рекла
webbrowser.open_new_tab(url_advertiser_lk_stats)
