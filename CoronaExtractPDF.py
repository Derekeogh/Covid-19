import PyPDF2
from PyPDF2 import PdfFileReader
# Script to create a CSV text file for WHO situation reports
path = (r'D:\Derek\Documents\Dump\20200412-sitrep-83-covid-19.pdf')
pdfFileObj = open(path,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# Preassigned Vars
a=0
pageObjS=str()
# Read PDF by page, manually select start and end pages
pageObj1 = pdfReader.getPage(1)
pageObj2 = pdfReader.getPage(2)
pageObj3 = pdfReader.getPage(3)
pageObj4 = pdfReader.getPage(4)
pageObj5 = pdfReader.getPage(5)
pageObj6 = pdfReader.getPage(6)
# Extract text from each page of the document
j1 = pageObj1.extractText()
j2 = pageObj2.extractText()
j3 = pageObj3.extractText()
j4 = pageObj4.extractText()
j5 = pageObj5.extractText()
j6 = pageObj6.extractText()
j5 = j5.replace('\n\n','\nCôte d’Ivoire\n')     # Common error patched
j5 = j5.replace('\n \n \n \n','\n Clusters \n') # Common error patched
pageObj = j1+j2+j3+j4+j5+j6        # Add each page into one string
Start = pageObj.find('China')      # First page: starting word
Endof = pageObj.find('Subtotal')-2 # Last page: end word
pageObj = pageObj[Start:Endof]     # crop string between first and last word
pageObj = pageObj.replace(' ','\t')   # Replace space with tab
pageObj = pageObj.replace('\n','')    # Remove new line only
# loop for each string, using tap with number before or after 
for gr in range(0,len(pageObj)):
    if pageObj[gr]==('\t') and pageObj[gr-1]==('1'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('1'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('2'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('2'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('3'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('3'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('4'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('4'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('5'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('5'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('6'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('6'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('7'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('7'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('8'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('8'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('9'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('9'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr-1]==('0'):
        pageObjS = pageObjS+str('\n')
    elif pageObj[gr]==('\t') and pageObj[gr+1]==('0'):
        pageObjS = pageObjS+str('\n')
    else:
        pageObjS = pageObjS+pageObj[gr] # If not a number add to string

TTT = pageObjS # For fault checking

# Common phrases replaced or removed, (not all needed or used)
pageObjS = pageObjS.replace('\t',' ') # Replace remaing tabs with space
pageObjS = pageObjS.replace('Territories**',' ')
pageObjS = pageObjS.replace('Kosovo[1]','Kosovo')
pageObjS = pageObjS.replace('South\n-\nEast Asia Region\n','')
pageObjS = pageObjS.replace(',','')
pageObjS = pageObjS.replace('European Region','')
pageObjS = pageObjS.replace('Eastern Mediterranean Region','')
pageObjS = pageObjS.replace('Region of the Americas','')
pageObjS = pageObjS.replace('African Region','')
pageObjS = pageObjS.split('\n')
# Pull out information needed from list of strings
Newdatahead = pageObjS[::7] # Country
NewData2 = pageObjS[1::7]   # Total Cases
NewData3 = pageObjS[2::7]   # New Cases
NewData4 = pageObjS[3::7]   # Total Deaths
NewData5 = pageObjS[4::7]   # New Deaths
txt = (Newdatahead)         # For fault check and loop size

lude = [] # New Variable assigned as list

# Loops to arrange data into new format for printing
for n in range(0,len(txt)):
    texd = [[Newdatahead[n]]+[NewData2[n]]+[NewData3[n]]+[NewData4[n]]+[NewData5[n]]]
    lude = lude + texd
for m in range(0,len(txt)):
    for o in range(1,5):
        lude[m][o] = (lude[m][o])
        luder = lude[m][0]     # 
        luder = luder.lstrip() # removes leading and trailing spaces
        lude[m][0] = luder

# Create a new file and writes each charater to file 
with open(r'D:\Derek\Documents\Dump\Proreport83.txt','w') as file_dump:
    for lists in range(0,len(txt)):
        for lists1 in range(0,5):
            if lists1 == 4:
                file_dump.write('%s' % lude[lists][lists1]) # last of each row no , needed
            else:
                file_dump.write('%s,' % lude[lists][lists1]) # Adds , after each string
        file_dump.write('\n') # New line at end of each iteration
        
print(pageObjS) # Check output
