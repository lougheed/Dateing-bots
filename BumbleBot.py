from selenium import webdriver
from time import sleep 

#both of these are needed for the GUI


#For the script to work you need to enter your username and password in the code below so it can login you in.


class BumbleBot():#Setting a main class item
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")#Finds the chromedriver, this should be in the same folder as this code on your PC

         
    def login(self):#Handles login
        self.driver.get("https://bumble.com/app")#Opens the webpage
        sleep(2)

        #Find the login button 
        fb_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div/div[2]/div')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        #Find the username & password field enters strings(plan text passwords) and 
      
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys("Your username here")
        
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys("Your password here")
                 
        LoginBTN = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        LoginBTN.click()

        #Flips back to the main page
        self.driver.switch_to_window(base_window)
        sleep(2)

    def dislike(self):#Find the dislike button and click 
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div')
        dislike_btn.click()
    
    def like(self):#Find the like button and click 
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
        like_btn.click()
  
    
    #Lots going on here, will brake it down line by line 
    def swipe(self):#Main mothod
        import random#Need the random library
                
        #Sets the below vars all to zero as  start point so we con increment for use in the main loop
        Number_of_Dislikes =0
        Number_Of_Likes =0
        Number_Of_Likes_count = 0

        print("")
        Log_file = open('BumbleBot_log.txt', 'w+')#opens a text file we will use for the log of how many likes and dislikes we make.

        while True:#starts a while loop
            try:
               #Here we add a bit of randonness to the code to help get around bot detection 
               x = random.randint(5,50)
               When_to_disike = random.randint(0,10)# sets a new var as a random number  
               sleep(2)#wait
               
               self.like()#call like method
               Number_Of_Likes_count += 1#increment how many users we are liked
               if When_to_disike >= x:#if statement to reset the loop and add one dislike so that tinder does not think this is a bot. 
                  self.dislike()#calls dislike
                  Number_of_Dislikes =+ 1#increment how many users we are disliked
               if Number_Of_Likes_count ==3:#every 15 or so likes check to see if the we have a hit and send a few msgs 
                   Log_file.close()
                   self.Messege_bot()
                   
                   continue                    
                   
               if Number_Of_Likes_count == 30:#Caps the whole loop at 2 likes, tweak as you need 
                  print("End of Max loop count")
                  sleep(1)
                  self.driver.close()#close the open broswer window 
                  break
                  exit()#break the loop and end the code  

               Log_file.writelines(["Liked: ",str(Number_Of_Likes_count)," and dislikes: ", str(Number_of_Dislikes), "\n" ]) 
               #Log_file.write(")#Prints out the vars we started to increment so that you who what has happened   
                 
            except Exception:
                Log_file.write("We have come across an error or have max number of likes mathued")
                print("We have come across an error or have max number of likes mathued")
                Log_file.close()
                self.driver.close()
                exit()
                
               
    def Messege_bot(self):
            #Test code will add a working function soon 
            print("Test")
            self.swipe()
            
                            
#Calls  everything we need form the above class         
Bot = BumbleBot()
Bot.login()
sleep(2)
Bot.swipe()



        
        

        
        
        



