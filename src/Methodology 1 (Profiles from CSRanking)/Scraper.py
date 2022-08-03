#-- coding: utf-8 --
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
def edit_centre_name(name):
	temp = name.split()
	return temp[0] + " " + temp[len(temp)-1]

n=open('names.txt','r')
names=n.readlines()

fault_names = open('fault_names.txt','w')


for j in range(0,len(names)):
	name = edit_centre_name(names[j])

	profile = webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.http", '51.77.215.51')
	profile.set_preference("network.proxy.http_port", '3128')
	profile.set_preference("network.proxy.ssl", '51.77.215.51')
	profile.set_preference("network.proxy.ssl_port", '3128')
	browser = webdriver.Firefox(profile)

	# browser = webdriver.Firefox()
	time.sleep(2)
	browser.get('https://scholar.google.com/')

	search = browser.find_element_by_name('q')
	time.sleep(2)
	search.send_keys(name)
	search.send_keys(Keys.RETURN) # hit return after you enter search text
	time.sleep(1) # sleep for 5 seconds so you can see the results

	try:
		link1_search = "User profiles for " + name
		try:
			link1 = browser.find_element_by_link_text(link1_search)
			link1.click()
		except:
			link1_search = "User profiles for " + name.lower()
			link1 = browser.find_element_by_link_text(link1_search)
			link1.click()
		
		alllinks = browser.find_elements_by_tag_name('a')

		for x in alllinks:
			try:
				if x.text == name or x.text == name.lower():
					x.click()
					break
			except:
				print '2error'

		count =0;
		while count <10: 
			try:
				browser.find_element(By.ID, "gsc_bpf_more").click()
				count+=1
			except:
				break
		time.sleep(10)
		page_url = browser.current_url
		total_citations = browser.find_elements_by_class_name("gsc_rsb_std") #use index 0 for total citations
		titles = browser.find_elements_by_class_name("gsc_a_at")
		citation_counts =browser.find_elements_by_class_name("gsc_a_ac")
		authors_pubs = browser.find_elements_by_class_name("gs_gray")
		print "Citations:", citation_counts[0].text
		print "Authors: ", authors_pubs[0].text
		print "Publication", authors_pubs[1].text
		print total_citations[0].text
		f=open(name+'.txt','w')
		f.write(page_url+'\n')
		f.write("Total Citations = "+total_citations[0].text)
		f.write('\n')
		f.write('\n')
		#print len(titles)
		#print page_url
		for i in range(0,len(titles)):
			f.write(str((i+1))+'. '+ titles[i].text.encode('utf-8')+'\n')
			f.write( "Citations:"+ citation_counts[i].text.encode('utf-8')+'\n')
			f.write ("Authors: "+ authors_pubs[2*i].text.encode('utf-8')+'\n')
			f.write( "Publication: "+ authors_pubs[2*i+1].text.encode('utf-8')+'\n')
			f.write('\n')
			# print titles[0].get_property('attributes') # get all atts of obj
			#print "Title:", titles[35].text
			# y = browser.find_element_by_link_text(titles[0].text).get_attribute("1")
			# print y, '\n\n\n'
			
		
			
	except:
		print name
		fault_names.write(name)

	time.sleep(3)
	browser.quit()

fault_names.close()