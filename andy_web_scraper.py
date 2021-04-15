from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request


driver = webdriver.Chrome("C:\Users\Owner\Downloads\chromedriver_win32 (1)\chromedriver.exe")

def login(email,password):
	driver.get('https://seminar.minerva.kgi.edu/?password=1')
	driver.find_element_by_id("js-email").send_keys(email)
	driver.find_element_by_id("js-password").send_keys(password)
	driver.find_element_by_id("sign-in").click()

def fetch_lectures(coursetitle,sectiontitle,old):
	if old == True:
		pastcourse = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Past Courses')))
		pastcourse.click()
		course = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, sectiontitle)))
		course.click()
	else:
		course = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, coursetitle + ' - ' + sectiontitle)))
		course.click()
	show_more = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'show-more-or-less')))
	show_more.click()
	pastclassbox = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "past-classes-region")))
	classtitles = pastclassbox.find_elements_by_class_name("title")
	classcount = len(classtitles)
	global titlelist
	global linklist
	titlelist = []
	linklist = []
	for i in range(classcount):
		titlelist.append(classtitles[i].text)
		linklist.append(classtitles[i].get_attribute('href'))
	for k in range(2):
		driver.find_element_by_class_name('next-page').click()
		time.sleep(2)
		pastclassbox = driver.find_element_by_class_name("past-classes-region")
		classtitles = pastclassbox.find_elements_by_class_name("title")
		classcount = len(classtitles)
		for i in range(classcount):
			titlelist.append(classtitles[i].text)
			linklist.append(classtitles[i].get_attribute('href'))
	titlelist.reverse()
	linklist.reverse()
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace(':','')
	for i in range(len(titlelist)):
		titlelist[i] = titlelist[i].replace('?','')


def download(address):
	totalclasscount = len(titlelist)
	vlinklist = []
	addresslist = []
	for i in range(totalclasscount):
		driver.get(linklist[i])
		button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "View your assessment. »")))
		button.click()
		vlink = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="vjs_video_3_html5_api"]/source')))
		vlinklist.append(vlink.get_attribute('src'))
		addresslist.append(address + "/{}.mp4".format(titlelist[i]))
		urllib.request.urlretrieve(vlinklist[i], addresslist[i])



login('abcde@connect.ust.hk','akjfd83nvd')
fetch_lectures('AH51','McMinn, MW@10:30', False)
download('C:/Users/User/Class Videos')
