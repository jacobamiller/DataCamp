def SFZ():
    M = ['01','02','03','04','05','06','07','08','09','10','11','12']
    D = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    # 123456 2001 MM DD 1111
    for num1 in range(0,10):
        for num2 in range(0,10):
            for num3 in range(0,10):
                       for num4 in range(0,10):
                                  for num5 in range(0,10):
                                             for num6 in range(0,10):
                                                 for year in range(1970,2014):
                                                     for m in range(len(M)):
                                                         for d in range(len(D)):
                                                             for x1 in range(0,10):
                                                                 for x2 in range(0,10):
                                                                     for x3 in range(0,10):
                                                                         for x4 in range(0,10):
                                                                             print str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(year) + M[m] + D[d] + str(x1) + str(x2) + str(x3) + str(x4)                                                                                                                    
def PinNumbers():
    for num1 in range(0,10):
        for num2 in range(0,10):
            for num3 in range(0,10):
                       for num4 in range(0,10):
                                  for num5 in range(0,10):
                                             for num6 in range(0,10):
                                                 print str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6)


def LandLinePhone():
    for num1 in range(0,10):
       for num2 in range(0,10):
          for num3 in range(0,10):
             for num4 in range(0,10):
                for num5 in range(0,10):
                   for num6 in range(0,10):
                      for num7 in range(0,10):
                          print "8" + str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7)
                          
                          
def MobileNumbers():
    NPA = ['130', '131','132', '133', '134', '135', '136', '137', '138', '139', '145', '147', '150', '151', '152', '153', '155', '156', '157', '158', '159', '180', '182', '183', '185', '186', '187', '188', '189']
    
    for n in range(len(NPA)):
        for num1 in range(0,10):
            for num2 in range(0,10):
                for num3 in range(0,10):
                    for num4 in range(0,10):
                        for num5 in range(0,10):
                            for num6 in range(0,10):
                                for num7 in range(0,10):
                                    for num8 in range(0,10):
                                        print NPA[n] + str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num8)
                                        
    
    NPA2 = ['1340', '1341', '1342', '1343', '1344', '1345', '1346', '1347', '1348']
    
    for n in range(len(NPA2)):
        for num1 in range(0,10):
            for num2 in range(0,10):
                for num3 in range(0,10):
                    for num4 in range(0,10):
                        for num5 in range(0,10):
                            for num6 in range(0,10):
                                for num7 in range(0,10):
                                    for num8 in range(0,10):
                                        print NPA2[n] + str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7)
                                        
def alpha3():
    for chr1 in range(0,10):
        for chr2 in range(0,10):
            for chr3 in range(0,10):
                for chr4 in range(0,10):
                    print chr(chr1) + chr(chr2) + chr(chr3)

def alpha4():
    for chr1 in range(0,10):
        for chr2 in range(0,10):
            for chr3 in range(0,10):
                for chr4 in range(0,10):
                    print chr(chr1) + chr(chr2) + chr(chr3) + chr(chr4)

def alpha5():
    for chr1 in range(0,10):
        for chr2 in range(0,10):
            for chr3 in range(0,10):
                for chr4 in range(0,10):
                    for chr5 in range(0,10):
                        print chr(chr1) + chr(chr2) + chr(chr3) + chr(chr4) + chr(chr5)

def alpha6():
    for chr1 in range(0,10):
        for chr2 in range(0,10):
            for chr3 in range(0,10):
                for chr4 in range(0,10):
                    for chr5 in range(0,10):
                        for chr6 in range(0,10):
                            print chr(chr1) + chr(chr2) + chr(chr3) + chr(chr4) + chr(chr5) + chr(chr6)

def alpha7():
    for chr1 in range(0,10):
        for chr2 in range(0,10):
            for chr3 in range(0,10):
                for chr4 in range(0,10):
                    for chr5 in range(0,10):
                        for chr6 in range(0,10):
                            for chr7 in range(0,10):
                                print chr(chr1) + chr(chr2) + chr(chr3) + chr(chr4) + chr(chr5) + chr(chr6) + chr(chr7)

def alpha8():
    for chr1 in range(0,10):
        for chr2 in range(0,10):
            for chr3 in range(0,10):
                for chr4 in range(0,10):
                    for chr5 in range(0,10):
                        for chr6 in range(0,10):
                            for chr7 in range(0,10):
                                for chr8 in range(0,10):
                                    print chr(chr1) + chr(chr2) + chr(chr3) + chr(chr4) + chr(chr5) + chr(chr6) + chr(chr7) + chr(chr8)
   
   
def HK_ID_Card():
    CheckSum = ['0','1','2','3','4','5','6','7','8','9','A']
    X = ['UQ', 'UW', 'UE', 'UR', 'UT', 'UY', 'UU', 'UI', 'UO', 'UP', 'UA', 'US', 'UD', 'UF', 'UG', 'UH', 'UJ', 'UK', 'UL', 'UZ', 'UX', 'UC', 'UV', 'UB', 'UN', 'UM']
    for d1 in range(len(X)):
        for num1 in range(0,10):
            for num2 in range(0,10):
                for num3 in range(0,10):
                    for num4 in range(0,10):
                        for num5 in range(0,10):
                            for num6 in range(0,10):
                                for c in range(len(CheckSum)):
                                    print X[d1] + str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + CheckSum[c]

#alpha3()
#alpha4()
#alpha5()
#alpha6()
#alpha7()
#PinNumbers()
#LandLinePhone()
MobileNumbers()
#HK_ID_Card()                                  
#alpha8() 
