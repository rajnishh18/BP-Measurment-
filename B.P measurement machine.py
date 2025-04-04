name=input("Name:")
age=int(input("Age :"))
disease=input("Disease:")
sugar=int(input("Sugar level is :"))
b_p=input("B.P (Format: 120/80):")


systolic,diastolic = map(int,b_p.split("/"))

print("Hii ",name,"I am Dr. XYZ")
print("Your age is ",age,"years old")
print("You are suffering from",disease)
print("Sugar is ",sugar)
print("B.P is ",b_p)



if ((systolic ==120 and diastolic == 80 and sugar == 100)):
    print("You do  not have B.P and Sugar.")
    print("You have only Viral infection.")
elif (systolic >130 and diastolic>80 and sugar == 110 ):
    print("Your B.P is high but Sugar is normal.")
    print("You avoid eat more salt and take medicine at time minimum 7 days.")

elif (systolic<120 and diastolic<80 and sugar > 125 ):
    print("Your B.P is low and sugar is high.")
    print("You  eat more salt and take medicine at time minimum 7 days.")
    print("your sugar is high so you do not eat more oily and spices food. ")

elif (systolic>130 and diastolic>80 and sugar > 125 ):
    print("Your B.P is high and also sugar is high.")
print("You avoid eat more salt and take medicine at time minimum 7 days. ")
print("you also have high sugar so you do not eat more oily and spices food .")