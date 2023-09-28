# Week 1 TPRG 2131 day 4.py A simplistic LCR calculator for TPRG week 2 Asmt 1
# Dustin Horne, 100844416
# TPRG2131 Assignment 1, September 15, 2023
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

""" This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
import math
import sys

print("Series/Parallel resonant circuit and RTC calculator\n\
(type Q or q to quit)")
        
def rfreq(ind, cap):
    return print("The resonant frequency is ""{:.2e}".format(((1/2)\
    *math.pi*math.sqrt(ind*cap))))    #Calculates the resonant frequency
          
def bandp(res1, res2, ind):
    return print("Bandwidth is ""{:.2e}".format(((1/res1)+(1/res2))/ind))    #Calculates the bandwidth for parallel

def bands(res1, res2, ind):
    return print("Bandwidth is ""{:.2e}".format((res1+res2)/ind))    #Calculates the bandwidth for series
        
def qfacs(res1, res2, ind, cap):
    return print("The Q factor is ""{:.2e}".format(((1/(res1+res2))*\
    math.sqrt(ind/cap))))  #Calculates the Q factor for series

def qfacp(res1, res2, ind, cap):
    return print("The Q factor is ""{:.2e}".format((((1/res1)+(1/res2)\
    *math.sqrt(cap/ind)))))    #Calculates the Q factor for parallel

def rtc(res1, cap):
    return print("The RTC is ""{:.2e}".format(res1*cap))    #Calculates the RC time constant

def resp(res1, res2):
    return print("The total resistance is ""{:.2e}".format((1/res1)+(1/res2)))    #Calculates the resistance in parallel

def ress(res1, res2):
    return print("The total resistance is ""{:.2e}".format(res1+res2))    #Calculates the resistance in series
 
while True:
    select = input("Please specify the circuit: s for series,\n"
    "p for parallel, or r for RTC ")
    if select == "Q" or select == "q":
        sys.exit(0)
        
    if select == "s" or select == "p":
        ind = float(input("What is the inductance in mH? "))
        while ind <= 0.0:
            ind = float(input("The value must be greater than zero\n"
            "What is the inductance in mH? "))

    if select == "s" or select == "p" or select == "r":
        cap = float(input("What is the capacitance in uF? "))
        while cap <= 0.0:
            cap = float(input("The value must be greater than zero\n"
            "What is the capacitance in uF? "))

    if select == "s" or select == "p" or select == "r":
        res1 = float(input("What is the first resistance in ohms? "))
        while res1 <= 0.0:
            res1 = float(input("The value must be greater than zero\n"
            "What is the first resistance in ohms? "))
            
    if select == "s" or select == "p":
        res2 = float(input("What is the second resistance in ohms? "))
        while res2 <= 0.0:
            res2 = float(input("The value must be greater than zero\n"
            "What is the second resistance in ohms? "))
            
    while select == "s":
        print("lcr:", ind, cap, ress(res1, res2), rfreq(ind, cap), \
              bands(res1, res2, ind), qfacs(res1, res2, ind, cap), "\n")
        break
    
    while select == "p":
        print("lcr:", ind, cap, resp(res1, res2), rfreq(ind, cap), \
              bandp(res1, res2, ind), qfacp(res1, res2, ind, cap), "\n")
        break
    
    while select == "r":
        print("lcr:", cap, res1, rtc(res1, cap), "\n")
        break
