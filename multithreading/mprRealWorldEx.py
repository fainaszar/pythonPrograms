from multiprocessing import Pool
import BeautifulSoup as bs 
import random
import requests
import string


def random_starting_url():

	starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for  _ in range(5))
	url = ''.join(['http://' , starting , '.com'])
	return url



def handle_local_links(url,link):
	if link.startswith('/'):
		return ''.join([url,link])
	else:
		return link



def get_links(url):
	try:
		resp = requests.get(url)
		soup = bs.BeautifulSoup(resp.text,'lxml')
		body = soup.body
		links = [links.get('href') for link in body.find_all('a')]
		links = [handle_local_links(url,link) for link in links]
		links = [str(link.encode("ascii")) for link in links]

		return links
	except TypeError as e:
		print ("Got a TypeError , probably a None \n Original Excecption: {}".format(e))
		return []
	except IndexError as e:
		print ("We probably didnt find any usefull links \n Original Excecption: {}".format(e))
		return []
	except AttributeError as e:
		print ("Likely got None for links! \n Original Excecption: {}".format(e))
		return []
	except Exception as e:
		print ("Something bad happened \n Original Excecption: {}".format(e))
		return []



def main():
	how_many = 50
	to_parse = [random_starting_url() for _ in range(how_many)]
	pool = Pool(processes=how_many)
	data = pool.map(get_links,[link for link in  to_parse])
	pool.close()


	with open('Aurls.txt','w') as f:
		f.write(str(data))


if __name__ == '__main__':
	main()