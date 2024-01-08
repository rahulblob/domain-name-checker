import os
import requests as r

# domain extensions
domains = {
  ".com",".net",".in",".org",
  ".pro",".live",".uk.org",
  ".me",".pro",".edu",
  ".mit.edu",".mit",
  ".uk",".eu.org",
  ".in",".eu",".in.org",
  ".dev",".to",".ml",".tk"
}

if __name__ == "__main__":
  # getting user input
  domain_name_without_ex = input('enter domain without extension -> ')

def check_domain():
  for i in domains:
    try:
      testStart = r.get(f"https://{domain_name_without_ex}{i}")
      if testStart.status_code == 200:
        # if avilable
        print(f"{testName}{i} - not-avilable \n")
    except:
        # if not avilable
      print(f"{testName}{i} - avilable \n")

if __name__ == "__main__":
  checkDomain()
