<div align="center">
  <br>

# dudb.py
<br>
<p>
RESTful Python API Wrapper to interact with the Discord Dangerous User Database at "discord.riverside.rocks"
</p>
<br>
<p>
<br>
<a href="https://www.pypi.org/package/dudb.py"><img src="https://static.pepy.tech/badge/dudb.py/month" alt="PyPi downloads" /></a>
<a href="https://www.pypi.org/package/dudb.py"><img src="https://api.ghprofile.me/view?username=milanmdev-dudb.py&label=repository%20view%20count&style=flat" alt="Repository view count" /></a>
</p>

<br>

</div>

# Usage

## Add the package
To start, you will need to add the package. To do that, simply run `pip install dudb.py`. In your code, add the following:
```py
import dudb
```
Now you can use any of the functions below!

---

### Checking a user
```py
check = dudb.check("USER_ID")
print(check)
```
The code above should return a 200 OK message. (JSON)

### Reporting a user
```py
report = dudb.report("USER_ID", "API_TOKEN", "REASON")
print(report)
```
The code above should return a 200 OK message. (JSON: Success)
