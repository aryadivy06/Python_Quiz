marks=0
answer=[]
an={"Section 1":"DSA"}
def dsa():
    
    ans=0
    a=[ ["Que1.What is the full form of DSA","1.Data Structure and algorithm","2.Data Science Algorithm","3.Data Sort Algorithm ","4.Domain Search Algorithm",1],
        ["Que2.What is the average time complexity of searching for an element in a balanced binary search tree (BST)","1.O(1)","2.O(log n)","3.O(n)","4.O(n log n)",4],
    ["Que3.Which data structure uses LIFO (Last In First Out) principle?","1.Queue","2.Stack","3.Array","4.Linkedlist",2],
    ["Que4.What is the time complexity of accessing an element in an array?","1.O(n)","2.O(1)","3.O(log n)","4.O(n log n)",2],
    ["Que5.Which algorithm is used to find the shortest path in a graph?","1.Depth-First Search","2.Breadth-First Search","3.Dijkstra's Algorithm","4.Kruskal's Algorithm",3]
   ]
    for i in range(len(a)):
        for j in range(0,5):
           print(a[i][j])
        answer.append(a[i][-1])
        an[a[i][0]]=a[i][a[i][-1]]

        ans1=int(input("Enter your answer: "))
        print("\n")
        if ans1==a[i][-1]:
           ans=ans+1
    
    return ans
  
       
def dbms():
    an["Section 2"]=["DBMS"]
    ans=0
    a=[["Que1.Which of the following is a primary key?","1.A unique identifier for each record in a table","2.A key that can accept null values","3.A key that is used to create relationships between tables ","4.A key that allows duplicate values",1],
    ["Que2. What does ACID stand for in the context of database transactions?","1.Atomicity, Consistency, Isolation, Durability","2.Accuracy, Consistency, Integrity, Durability","3.Atomicity, Coherence, Isolation, Data","4.Availability, Consistency, Isolation, Durability",1],
    ["Que3. Which of the following SQL statements is used to create a table?","1.INSERT INTO","2.UPDATE","3.CREATE TABLE ","4.ALTER TABLE",3],
    ["Que4.Which type of join returns all rows when there is a match in either of the tables?","1.INNER JOIN","2.LEFT JOIN","3.RIGHT JOIN ","4.FULL JOIN",4],
    ["Que5.What is the purpose of normalization in a database?","1.To reduce redundancy and improve data integrity","2.To increase data redundancy","3.To ensure data is stored in a single table","4.To reduce the complexity of queries",1]]
    for i in range(len(a)):
        for j in range(0,5):
           print(a[i][j])
        answer.append(a[i][-1])
        an[a[i][0]]=a[i][a[i][-1]]
        ans1=int(input("Enter your answer: "))
        print("\n")
        if ans1==a[i][-1]:
           ans=ans+1
    
    return ans
  
def python():
    an["Section 3"]=["Python"]
    ans=0
    a=[["Que1.Which of the following is a mutable data type in Python?","1. Tuple","2.List","3.String","4.integer",2],
    ["Que2.Which keyword is used to create a function in Python?","1.func","2.define","3.function ","4.def",4],
    ["Que3.Which of the following functions can be used to get the length of a string in Python?","1. length()","2.strlen()","3. len()","4.size()",3],
    ["Que4.Which of the following is the correct way to declare a variable and assign the value 5 to it?","1.int x = 5","2.x = 5","3.declare x=5 ","4.x:=5",2],
    ["Que5.What is the data type of print(type(3.14)) in Python?","1.int","2.float","3.double","4.string",2]]
    for i in range(len(a)):
        for j in range(0,5):
           print(a[i][j])
        answer.append(a[i][-1])
        an[a[i][0]]=a[i][a[i][-1]]
        ans1=int(input("Enter your answer: "))
        print("\n")
        if ans1==a[i][-1]:
           ans=ans+1
    
    return ans
  
def answ():
    print("Do you want to see the answers then enter 1 else 0")
    f=int(input("Enter your choice="))
    print("\n")
    if f==0:
        return
    else:
        for i in an:
            
             print(f"{i}\nanswer={an[i]}\n")
        

print("----------------Online Test------------------\n\n")
print("             Register as a user           ")
name=input("Enter your name: ").lower()
password=input("Enter your password:").lower()
n=False
l=False

print("              Login          ")
while l!=True:
    m=input("Enter your user name: ").lower()
    if m!=name:
       print("Invalid credentials\n Renter your details")
       l=False
    else:
        l=True
        while n!=True:
            k=input("Enter your password:").lower()
            print("\n")
            if k!=password:
               print("Invalid password")
               n=False
            else:
                n=True
                print("----------Quiz--------\n")
                print("Quiz Details\n\nQuiz Contains 3 sections\n 1.DSA\n 2.DBMS\n 3.Python\n")
                print("1.Each section contains 5 question carrying 1 mark for correct answer.")
                print("2.To clear the quiz you have to score minimum 6 marks.")
                print("3.Read all questions carefully and the enter your answer.")
                print("4.All the best for quiz")
                print("\n\n")
                print("Section 1:DSA\n")
                
                d=dsa()
                print("Section 2:DBMS\n")
                e=dbms()
                print("Section 3:Python\n")
                f=python()
                marks=d+e+f
                answ()
                
                if marks<6:
                    print(f"You fail the quiz and your  marks:{marks}")
                    print("Try better next time")
                    
                else:
                    print(f"You Passed the quiz with marks={marks}")
