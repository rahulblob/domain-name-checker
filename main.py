import os
import requests as r

# add domain extention here as much as you can
domains = {
  # domain extentions
".com",".net",".in",".org",".pro",".live",".uk.org",".me",".pro",".edu",".mit.edu",".mit",".uk",".eu.org",".in"
}

if __name__ == "__main__":
  # change the input text if you want else leave it as it is
  testName = input('enter name to test alternatives -> ')

def checkDomain():
  for i in domains:
    try:
      testStart = r.get(f"https://{testName}{i}")
      if testStart.status_code == 200:
        # avilable message
        print(f"{testName}{i} - not-avilable \n")
    except:
        # not avilable message
      print(f"{testName}{i} - avilable \n")

if __name__ == "__main__":
  checkDomain()
  # 
  print("end testing")
