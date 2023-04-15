import os
import requests as r

domains = {
".com",".net",".in",".org",".pro",".live",".uk.org",".me",".pro",".edu",".mit.edu",".mit",".uk",".eu.org",".in"
}

if __name__ == "__main__":
  testName = input('enter name to test alternatives -> ')

def checkDomain():
  for i in domains:
    try:
      testStart = r.get(f"https://{testName}{i}")
      if testStart.status_code == 200:
        print(f"{testName}{i} - not-avilable \n")
    except:
      print(f"{testName}{i} - avilable \n")

if __name__ == "__main__":
  checkDomain()
  print("end testing")
