while True:
    sts=input()
    count=0
    if (sts=='#'):
        break;
    else:
        for i in sts:
            ascii=ord(i)
            if (ascii==97 or ascii==101 or ascii ==105 or ascii==111 or ascii==117 or ascii==65 or ascii==69 or ascii==73 or ascii==79 or ascii==85):
                count+=1
    print(count)

    


        
        



    