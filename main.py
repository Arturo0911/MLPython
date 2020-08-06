
iteration ={
    'net1': [0,0],
    'net2': [0,1],
    'net3': [1,0],
    'net4': [1,1]
}

def Net_calculate(X1,W1, X2,W2, B):

    #print("Function Net_calculate")
    net = int((X1*W1 + X2*W2)+B)
    return net


# To handle value of error
def Function_Y_get(net):

    # Here we define a variable called Y_obtenida
    Y_obtenida = 0
    if (net > 0):
        Y_obtenida = 1
        return Y_obtenida
    elif(net<=0):
        Y_obtenida = 0
        return Y_obtenida


def Error_calculate(Y_esperada, Y_obtenida):

    error = int(Y_esperada - Y_obtenida)
    return error



# Here to fix values, both weights and Bias
def Fix_weights(W1,X1, W2,X2,B, error):

    #print("Function Fix_weights")
    WK1 = W1 + (error * X1)
    WK2 = W1 + (error * X2)
    BK = B + (error)

    new_weights = [WK1,WK2,BK]

    return new_weights



def Continue_cases(error):

    
    if (error == 0):
        
        return True
    elif(error !=0):
        
        return False


def Confirm_procedure(W1, W2, B):
    lista_ = []
    counter = 0
    for i in iteration:
        Y_waiting = 1
        for j in iteration[i]:
            Y_waiting = Y_waiting * j
        
        Net = (((iteration[i][0]*W1) + (iteration[i][1]*W2) + B))
        Get_Y = Function_Y_get(Net)
        Get_err = Error_calculate(Y_waiting,Get_Y)
        Get_verify = Continue_cases(Get_err)
        if (Get_verify is True):
            lista_.append(Get_verify)

    for k in lista_:
        if (k == True):
            counter = counter + 1
    if ( counter == 4):
        print("Successfully process")
    else:
        print("There some error to fix")






def main():
    print("Main Function ")


    # ------ Variables into the function -------
    Weight1= 10
    Weight2= 10
    Bias= -8


    for i in iteration:
        #print("Las variables son: ", [Weight1,Weight2,Bias])
        Y_esperada = 1
        for x in iteration[i]:
            Y_esperada = Y_esperada * x



        NET = Net_calculate(iteration[i][0], Weight1, iteration[i][1], Weight2, Bias)
        
        Y_obtenida_get = Function_Y_get(NET)
        Error_get = Error_calculate(Y_esperada,Y_obtenida_get)
        Verify_error = Continue_cases(Error_get)
        
        if (Verify_error is not True):
            Weight1 = Fix_weights(Weight1,iteration[i][0], Weight2,iteration[i][1],Bias,Error_get)[0]
            Weight2 = Fix_weights(Weight1,iteration[i][0], Weight2,iteration[i][1],Bias,Error_get)[1]
            Bias = Fix_weights(Weight1,iteration[i][0], Weight2,iteration[i][1],Bias,Error_get)[2]
        """   
        else:
            print("Hay que corregir porque el error dio %s "%Error_get)
            

            # Here we asign the new values to variables. 
            Weight1 = Fix_weights(Weight1,iteration[i][0], Weight2,iteration[i][1],Bias,Error_get)[0]
            Weight2 = Fix_weights(Weight1,iteration[i][0], Weight2,iteration[i][1],Bias,Error_get)[1]
            Bias = Fix_weights(Weight1,iteration[i][0], Weight2,iteration[i][1],Bias,Error_get)[2]
        """
            
    Confirm_procedure(Weight1,Weight2,Bias)
       



if __name__ == "__main__":
    #print("Hola")
    main()
    #lista = [True, True,True, True]
    #print(lista)
    #print("hola")