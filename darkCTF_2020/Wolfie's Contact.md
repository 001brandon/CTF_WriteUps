# Web/Source

### Problem Description

Wolfie is doing some Illegal Work with his friends, find his contacts.
Category: Forensics 221

### File





## Solving the Challenge
When logging onto the webpage we are greated with something that looks like this.
``
**WRONG!**
**Ahhhhh, Try not Easy**
``

If we examine the PHP script we can see that it takes User Agent information and stores it in the variable `$web`.
`$web` is then checked to see if it is numeric or not, if it is it checks it's length and value in order to display the flag.
In order to get the flag displayed the string has to be numeric, length less than 4, and value > 10000.

Lets take a closer look at PHP [is_numeric](https://www.php.net/manual/en/function.is-numeric.php) to understand it.
We can see that it accepts expotential values and in order to get a value greater than 10000 that is less than 4 digits,
we must use some sort of operation and expotentiation is great for that.

Now we just have to send the value to webserver and get the flag!
Using curl we can enter
```
brandon@LAPTOP-HRFEV0OI:~$ curl -H "User-Agent:9e6" http://web.darkarmy.xyz/
<html>
    <head>
        <title>SOURCE</title>
        <style>
            #main {
    height: 100vh;
}
        </style>
    </head>
    <body><center>
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<div class="w3-panel w3-green"><h3>Correct</h3>
  <p>darkCTF{changeing_http_user_agent_is_easy}</p></div></center>
<!-- Source is helpful -->
    </body>
</html>brandon@LAPTOP-HRFEV0OI:~$
```
Giving us the flag being: darkCTF{changeing_http_user_agent_is_easy}
