from bs4 import BeautifulSoup
import requests as r, pprint, webbrowser as wb
import find_html as fh, csv as c

base_URL = 'https://esc.berkeley.edu/'
ends_html = fh.get_allfiles()

def parse_thru_web(URL):
	web_page = r.get(URL)

	soup = BeautifulSoup(web_page.text, 'html.parser')
	head = soup.find_all('a')

	URLs_inpage = [each.get('href')for each in soup.find('body').find_all('a') if each.get('href') not in ['#', '#one', '#two', '#three', '#four']]
	return whole_checker(URLs_inpage)

def whole_checker(URLs_inpage):
	def check_link(URL):
		if type(URL) is list:
			whole_TF = []
			for each in URL:
				whole_TF+=[check_link(each)]
			return whole_TF

		if not URL:
			return True, "NoneType"
		elif not (type(URL) ==str):
			return False, 'NOT STRING TYPE'
		elif not ('http' in URL):
			return False, 'HTTP ISSUE'
		else:
			try:
				request = r.get(URL, verify=True)
				if request.status_code == 200:
					return True, "STATUS: OK"
				else:
					return False, "ERROR: "+ str(request.status_code)
			except:
				return False, "ERROR WAS RAISED"



	def verify_link(TF_list, URLs):
		TF = [each[0] for each in TF_list]
		if not (TF.count(True)/len(URLs) == 1):
			broken_list ={}
			for i in range(len(TF)):
				if not TF[i]:
					broken_list.update({URLs[i]:TF_list[i][1]})
			return broken_list
		else:
			return "STATUS: OK"

	r_URL = reformat_URL(URLs_inpage)
	return verify_link(check_link(r_URL), r_URL)

def reformat_URL(URL_list, verified_URLs=ends_html, base=base_URL):
	reformatted_URLs =[]
	for URL in URL_list:
		if URL in verified_URLs:
			reformatted_URLs.append(base+URL)
		else:
			reformatted_URLs.append(URL)
	return reformatted_URLs


check_ESC_wb = {each_page:parse_thru_web(each_page) for each_page in [base_URL+end_html for end_html in ends_html]}
print(check_ESC_wb)
