# Authentication bypass via encryption oracle

1. I logged in with given credentials and marked "Stay logged in" option, while analyzing the logging in operation I noticed that there is a "stay-logged-in" cookie with encrypted value.

![stay-logged-in cookie](1.1.png)

2. After analyzing the domain, I found out another cookie (notification=KjJkERAiMgGCezLyx8%2b6yNgtet6I7vV5sQBED4E6W70%3d), which is set up after giving wrong address email, while commenting. And after failed comment, the error occurs.

![commenting](2.1.png)

![notification cookie](2.2.png)

![notification](2.3.png)

3. When, in post's GET request, I put the value of "stay-logged-in" cookie into "notification" cookie, except of error message I got decrypted content of "stay-logged-in" cookie, which is "wiener:1675788781469". I knew then, that the "stay-logged-in" cookie is an encrypted in format user:timestamp. 

![discovering decryption mechanism](3.1.png)

4. I named comment's POST request "encrypt" and post's GET request "decrypt". 

5. I decided to encrypt administrator:my-timestamp and it worked, but then I needed to get rid of the first 23 characters of the decrypted message "Invalid email address: ". 

![testing decryption mechanism](5.1.png)

6. In Burp decoder I firstly URL-decoded, then Base64-decoded and then deleted first 23 bytes. When I removed this prefix, I re-encoded the message and tried to decrypt it. 

![decoding and deleting first 23 bytes](6.1.png)

![re-encoding](6.2.png)

7. After I sent a request except of decrypted message I got an error saying "Input length must be multiple of 16 when decrypting with padded cipher", so I added 9 letters of padding, before administrator. 

![error](7.1.png)

![message with padding](7.2.png)

8. In Burp decoder, I've done the same, but this time I removed 32 bytes. 

![decoding and deleting first 32 bytes](8.1.png)

![re-encoding](8.2.png)

9. Finally, I constructed a right value, to insert into the stay-logged-in cookie. 

![final construction](9.1.png)

10. I intercepted the request to an admin panel, removed a session cookie and changed the value of "stay-logged-in" cookie to crafted message. I accessed the admin panel and removed carlos. The lab is solved. 

![intercepting](10.1.png)

![admin panel](10.1.png)

![solved](10.3.png)

