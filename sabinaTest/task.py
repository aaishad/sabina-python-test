import os,sys
import time
from BrowserSeleninumUtils import WebSeleniumUtils
from xpathsele import CharmHealth
data = {
"name": "Dummy Patient",
"History of Present Illness": "Patient presents today for concerns regarding his palpitations, but nothing he thinks is serious. He notes that he can use his Apple Watch when he experiences these palpitations. He denies having passed out. Patient’s event monitor shows that he had an auto trigger 14 times, but nothing critical. His lowest heart rate was 39 and high highest heart rate was 157. There is only sinus rhythm. When patient passed out on the tilt table, his blood pressure dropped from 109/74 to 80/63 and after his blood pressure dropped, his heart rate that was 90 dropped as well. Patient quit smoking. Current medications include: Cyproheptadine, Lexapro 10mg",
"Physical Examination": {"Template": "IM Skin Growth - PE", "Checkboxes": [["scaling"], ["lesion", "color", "blue"]], "Values": {"Hypomelanotic Size": "70mm"}},
"Diagnoses": [{"Diagnosis": "Essential (primary) hypertension", "Code": "I10"}],
"Url":"https://www.charmhealth.com/"
}
obj = WebSeleniumUtils()
objch = CharmHealth()
url = data["Url"]
name = data['name']
history = data['History of Present Illness']
# login in url
res = objch.checking_for_login(url,obj)
if res is True:
	print("Successfully login")

#clicking on char note
res = objch.click_on_chartnote(obj)
if res is True:
	print("Successfully Click on Chart Note")

#click encounter and search
objch.click_on_encounter(obj,name)

#click histroy
objch.click_on_history(obj)

#closing driver
objch.quitDriver()