<h1 align="center">
  <br>
  <a href="https://github.com/sinsinsecurity/Priest"><img src="https://i.ibb.co/gWz3LTX/priest.png" alt="Arjun">
  <img src="https://i.ibb.co/Y8KDsY2/pr-ca.png" alt="Arjun">
  </a>
</h1>


### What is Priest?
Priest is a simple index.html file containing JavaScript code which can extract useful information from Browser SSRF Vulnerabilities

<h6 align="center">
  <br>
  <a href="https://github.com/sinsinsecurity/Priest"><img src="https://i.ibb.co/25FC6Km/carbon.png" alt="Arjun"></a>
</h6>

### What Inforamtion can get extracted:
- Extract complete navigator object
- Browser User-Agent
- OS Platform version
- Language
- Browser Version
- IP Address v4/v6
- ASN Number
- Org Name
- Timezone
- Number of System Logical Processors
- etc.


### How to use:
in order to make our lives easier, a simple python3-WebServer script has been included which will server http on `http://0.0.0.0:8000/index.html` and when a browser requests the address all the information will get extracted and shown in the webpage, this is useful in pdf exports, controllable headless browsers, etc.

#### - Using Seperate index.html
```
git clone https://github.com/sinsinsecurity/priest.git
cd priest
put index.html on a webserver
```


#### - OR Using the priest.py  webserver
```
git clone https://github.com/sinsinsecurity/priest.git
cd priest
chmod +x priest.py
./priest.py 8000
```

#### Result:
This is very useful when dealing with EC2 Servers, Google Clouds and html renderes in order to detect the used technology for further exploitation
<h6 align="center">
  <br>
  <a href="https://github.com/sinsinsecurity/Priest"><img src="https://i.ibb.co/ZBRC4x9/show-case.png" alt="Arjun"></a>
</h6>
