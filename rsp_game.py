import random
def rsp_play(value):
    input_list=['ROCK','PAPER','SCISSORS']
    output_list=[value]
    if value not in input_list:
        #print(value)
        output_list.extend(['','Enter a Valid Input'])
    else:   
        user_input=input_list.index(value) 
        computer_choice=random.randint(0,2)
        output_list.append(input_list[computer_choice])
	#00 11 22
        if computer_choice==user_input:
            output_list.append("It's a draw...")
	#20 
        elif user_input==2 and computer_choice==0:
            output_list.append("You lose")
	#02
        elif user_input==0 and computer_choice==2: 
            output_list.append("You won")
	#01 12
        elif computer_choice>user_input:
            output_list.append("You lose")
	#10 21
        elif user_input>computer_choice:
            output_list.append("You won")
    return output_list
	
#rsp_output=rsp_play('ROCK')
#print(rsp_output[0])
#print(rsp_output[1])