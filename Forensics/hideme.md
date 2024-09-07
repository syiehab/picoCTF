# Hideme

### The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.


Given an image file ```flag.png```

![image](https://github.com/user-attachments/assets/fe325652-3af4-4add-96e5-060863b1e703)


Use ```binwalk``` to find hidden files inside the image 

![image](https://github.com/user-attachments/assets/f65f4ff3-f5d9-4cef-9ee7-d074b61c3539)


Extract all the file by using ```binwalk --dd=.* flag.png``` command

![image](https://github.com/user-attachments/assets/416eeb71-c138-4474-9004-7e8b49765fac)


Checking all file type that has been extracted byb ```file *``` inside the extracted directory

![image](https://github.com/user-attachments/assets/7bb89ca1-09f5-4fb1-be9d-f81bf7cfc9b2)


Since there are some zip files, try to extract one by one to the their content

![image](https://github.com/user-attachments/assets/ecdc853e-3b0a-4b99-abb4-e99b753823a8)


It shows that theres another png image inside ```secret/``` directory. Open it up and we get the flag.

![image](https://github.com/user-attachments/assets/4eb8953b-4cdb-4f12-b005-81493b9678a2)


flag = picoCTF{Hiddinng_An_imag3_within_@n_ima9e_82101824}

