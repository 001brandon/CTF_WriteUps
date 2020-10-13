# Web/Source

### Problem Description

Don't Try to break this jail

ssh wolfie@linuxstarter.darkarmy.xyz -p 8001 password : wolfie
Category: Web 101





## Solving the Challenge
When you ssh into the terminal you get greeted with a darkCTF printout and a restricted bash shell.
The bash shell inhibits you from using ls to list the files or cd to change directories. I figured the file had to 
be in one of the home directories so I was able to bypass not being able to use ls or cd by just using echo.
I would type echo * to have the files and directories listed then echo inside of those in order to find more files.
After playing around I was able to find the solution file and cat it for the output.
![alt_text](https://github.com/001brandon/CTF_WriteUps/blob/master/darkCTF_2020/CTF%20linux.PNG)

### FLAG
darkCTF{h0pe_y0u_used_intended_w4y}
