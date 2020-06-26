import os 
  
# Function to rename multiple files 
def main(): 
    x=os.getcwd()
    i=301
    y=x+"\\vadapav1\\"
    for file in os.listdir(y): 
        dst ="t"+str(i)+".JPG"
        src =y+file 
        dst=y+dst
        i=i+1  
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 