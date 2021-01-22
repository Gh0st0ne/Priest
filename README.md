<h1 align="center">
  <br>
  <a href="https://github.com/sinsinsecurity/Priest"><img src="https://i.ibb.co/gWz3LTX/priest.png" alt="Arjun"></a>
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
in order to make our lives easier, a simple python3-WebServer script has been included which will server http on http://0.0.0.0/8000(default) and when a browser requests the address all the information will get extracted and shown in the webpage, this is useful in pdf exports, controllable headless browsers, etc.
