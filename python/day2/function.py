#displaying some some random statements
def dis():
    print(f"good morning") 
#defining the function 
#displaying the area
def display(data):
    print(f"the area is {data}")
#considering inputs
def get_input():
    received_length=input("Length:")
    received_width=input("width:")
    return(received_length,received_width)
#Computing the area   
def compute_area(length,width):
    area=int(length)*int(width)
    return area
#calling the function in main function
def main():
    (length,width)=get_input()
    area=compute_area(length,width)
    display(area)
    dis()
    
main()    