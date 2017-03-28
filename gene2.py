#by Kent Wong
#contact: kentwong@ucalgary.ca for any concerns or bugs
#UofC Medical Labs
## CONSTANTS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
 
path_to_phantomjs_exe = "C:\Python34\Lib\phantomjs\phantomjs.exe"
path_to_ghostdriver_log = "C:\Python34\Lib\site-packages\selenium-2.44.0-py3.4.egg\selenium\webdriver\phantomjs\ghostdriver.log"
driver = webdriver.PhantomJS(executable_path= path_to_phantomjs_exe, service_log_path= path_to_ghostdriver_log)
 
ids = []
def filelogger():
 
        filename =input("What is the file name?: ")
       
        textreader = open(filename,"r")
        sys.stdout = open("log.txt", "w")
       
        for line in textreader:
                protein_id = line.replace('\n', '')
                theurl = "http://www.ncbi.nlm.nih.gov/protein/"+protein_id
                driver.get(theurl)
               
                elem = driver.find_element_by_id("feature_"+protein_id+"_CDS_0")
                gene = elem.get_attribute('innerHTML')
                gene = gene.splitlines()
               
                for i in gene:
                        if "locus_tag" in i:
                                i = i.replace(' ', '').replace('/locus_tag=', '').replace('"', '')
                                print ((protein_id), "corresponds to", i)
                        else:
                                pass
 
        textreader.close()
       
        driver.quit()
 
def start():
 
        filelogger()
 
start()
