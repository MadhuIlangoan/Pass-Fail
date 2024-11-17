student=1
while student<40:
        name=str(input("ENTER YOUR NAME  "))
        Tamil=int(input("ENTER TAMIL MARKS"))
        Religion=int(input("ENTER RELIGION MARKS"))
        Maths=int(input("ENTER MATHS MARKS"))
        Science=int(input("ENTER SCIENCE MARKS"))
        History=int(input("ENTER HISTORY MARKS"))
        English=int(input("ENTER ENGLISH MARKS"))
        Bucket_01=int(input("ENTER BUCKET 01 MARKS"))
        Bucket_02=int(input("ENTER BUCKET 02 MARKS"))
        Bucket_03=int(input("ENTER BUCKET 03 MARKS"))
        print("YOUR TAMIL MARKS IS",Tamil)
        print("YOUR RELIGION MARKS IS",Religion)
        print("YOUR MATHS MARKS IS",Maths)
        print("YOUR SCIENCE MARKS IS",Science)
        print("YOUR HISTORY MARKS IS",History)
        print("YOUR ENGLISH MARKS IS",English)
        print("YOUR BUCKET 01 MARKS IS",Bucket_01)
        print("YOUR BUCKET 02 MARKS IS",Bucket_02)
        print("YOUR BUCKET 03 MARKS IS",Bucket_03)
        Total_Marks =Tamil+Religion+Maths+Science+History+English+Bucket_01+Bucket_02+Bucket_03
        print("TOTAL MARKS= ", Total_Marks)
        Average =Total_Marks/9
        print("AVERAGE= ", Average)
        if Average<40 :
            print("YOU ARE FAIL")
        else:
            print("YOU ARE PASS")
           

