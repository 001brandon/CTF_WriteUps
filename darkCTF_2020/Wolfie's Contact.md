# Web/Source

### Problem Description

Wolfie is doing some Illegal Work with his friends, find his contacts.
Category: Forensics 221

### File
EO1 Drive





## Solving the Challenge
When loading up the E01 Drive into FTK Imager we are given a scanned windows hard drive that we can nagvigate through.
Seeing that we are looking for contacts we can navigate to the contacts directory and take a look.
Here we find several names and files that look like this.
![alt_text](https://github.com/001brandon/CTF_WriteUps/blob/master/darkCTF_2020/Capture.PNG)
All names of files 1 contain windows logs but all files of size 2 contain parts of the flag in the notes section.
Here we can see in this notes section the portion of the flag is 1mp0rtant.
Going through these contancts and parsing the bits of the flag together we get the final flag to be.


### FLAG
darkCTF{C0ntacts_4re_1mp0rtant}
