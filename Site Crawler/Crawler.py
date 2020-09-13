import urllib.request
from requests_html import HTML, HTMLSession


url = 'https://who.is/whois/bluewolfwebdesign.com/'
url = 'https://who.is/whois/prestigefarms.com/'

finalPrint = ""
try:
    session = HTMLSession()
    r = session.get(url)

    page = r.html.find('html', first=True)

    text = page.find('.rawWhois', first=True).text
    text2 = page.find('.col-md-7', first=True).text

    start = text.find("Registrant Contact Information:")
    end = text.find("Administrative Contact Information:")
    #line = text[start+32:end+18]
    line = text[start:end]
    #print(line)

    # - - Pulling Name - -
    start = line.find("Name")
    end = text.find("Organization")
    finalPrint = line[start+5:end-1]

    if(finalPrint.find("Contact Privacy Inc. Customer") != -1):
        print("The domain " + url +" is private")
    else:
        print("Domain is not private")
        print("Name: " + finalPrint)
        output = "Name: " + finalPrint

        # - - Pulling Organization - -
        start = line.find("Organization")
        end = line.find("Address")
        finalPrint = line[start+13:end-1]
        print("Organization: " + finalPrint)
        output = "Organization: " + finalPrint

        # - - Pulling Address - -
        start = line.find("Address")
        end = line.find("City")
        finalPrint = line[start+8:end-1]
        print("Address: " + finalPrint)
        output = "Address: " + finalPrint

        # - - Pulling City - -
        start = line.find("City")
        end = line.find("State / Province")
        finalPrint = line[start+5:end-1]
        print("City: " + finalPrint)

        # - - Pulling State / Province - -
        start = line.find("State / Province")
        end = line.find("Postal Code")
        finalPrint = line[start+17:end-1]
        print("State / Province: " + finalPrint)

        # - - Postal Code - -
        start = line.find("Postal Code")
        end = line.find("Country")
        finalPrint = line[start+12:end-1]
        print("Postal Code: " + finalPrint)

        # - - Postal Country - -
        start = line.find("Country")
        end = line.find("Phone")
        finalPrint = line[start+8:end-1]
        print("Country: " + finalPrint)

        # - - Postal Phone - -
        start = line.find("Phone")
        end = line.find("Email")
        finalPrint = line[start+6:end-1]
        print("Phone: " + finalPrint)

        htmlcode = urllib.request.urlopen("https://who.is/whois/prestigefarms.com/")
        pagecode = htmlcode.read()
        page = pagecode.decode("utf8")
        htmlcode.close()
        start = page.find("/tools/stringImage")
        new = page[start:start+100]
        end = new.find(">")-1
        print("Email URL: https://who.is" + new[0:end])
except:
  print("The URL (" + url +") does not exist")
