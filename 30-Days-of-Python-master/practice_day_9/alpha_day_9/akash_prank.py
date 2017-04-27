class Akash():


  msg="""
                Seems like you are in trouble now. I can feel that...hahaaa  
                Your name:Akash
                Address:Nepalgunj  

                """


  another="""
  I am not really good friend of yours becauase i am going transfer some viruses from the internet.\n
              I Know everythings about you??:P.....Press Enter extract virus

              """

  last_message = """
  #
   ##
   ###
    ####
     #####
     #######
      #######
      ########
      ########
      #########
      ##########
     ############
   ##############
  ################
   ################                                                 #
    ##############                                                 ###                      Installing viruses....
      ##############                                             ####                         GoodByee...!!
      ##############                                           #####               Computer will turn off in one minute
       ##############                                      #######
       ##############                                 ###########
       ###############                              #############
       ################                           ##############
      #################      #                  ################
      ##################     ##    #           #################
     ####################    ###   ##          #################
          ################   ########          #################
           ################  #######         ###################
             #######################       #####################
              #####################       ###################
                ############################################
                 ###########################################
                 ##########################################
                  ########################################
                  ########################################
                   ######################################
                   ######################################
                    ##########################      #####
                    ###  ###################           ##
                    ##    ###############
                    #     ##  ##########
                              ##    ###
                                    ###
        Ghost Computer              ##
        Arch Linux                  #
        sudo:vimm0                    """






  def question_answer(self):
    var2=[]
    var1 = input("Hello, dear what is your name?: ")
    print("Ohh!! {var1} is nice name to have. ".format(var1=var1))
    var2 = input(
        "Do you want to install virus?")
    print(self.msg)
    print(self.another)
    print(self.last_message)

if __name__=="__main__":
  obj=Akash()
  obj.question_answer()
