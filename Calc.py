q1 = float(input("Q1: "))
q2 = float(input("Q2: "))
p1 = float(input("P1: "))
p2 = float(input("P2: "))
  
    
dq = q2-q1
dp = p2-p1
eq = (dq/dp) * (p1/q1)
eq1 = ((dq/q1)/(dp/p1))
eq2 = (dq/dp) * (p2/p2)

print("DeltaQ: ", dq)
print("DeltaP: ", dp)
print("Elastizitätskoeffizient: ", eq)
print("Elastizitätskoeffizient: " ,eq1)