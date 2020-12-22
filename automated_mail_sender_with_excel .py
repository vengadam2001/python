import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
l=[]
def send_test_mail(smail,rmail,j=0):
    sender_email = smail
    receiver_email = rmail
    body=" Mail 's Body content ni html"
    msg = MIMEMultipart()
    msg['Subject'] = 'subject of ur mail '
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)

    # filename = "example.txt"
    # msg.attach(MIMEText(open(filename).read()))
    with open('pic1.jpeg', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="Installation MP-2.jpeg")
        msg.attach(img)
    with open('pic2.jpeg', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="Installation-MP-1.jpeg")
        msg.attach(img)
    with open('pic3.jpeg', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="Installation-SP-1.jpeg")
        msg.attach(img)
    with open('pic4.jpeg', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="FeverTest-MP installation pix.jpeg")
        msg.attach(img)
    
        
    pdf = MIMEApplication(open("pdf1.pdf", 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename= "FeverTest Brochure.pdf")
    msg.attach(pdf)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(smail, "passwd")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        l.append([j,rmail])
data = pd.read_excel ('Excel.xlsx' , sheet_name = 'Sheet1') 
df = pd.DataFrame(data)
j=2
print(df)
print(df['Email Id'])
for i in df['Email Id']:
    if str(i)!='nan':
        send_test_mail("<Sender's Eamil> ",i,j)
        print(str(j)+" mail sent for "+i)
        j+=1
print("the following mail ids are not valid (error thrown by the program)")
for i in l:
    print(str(i[0])+" -- "+str(i[1]))        
send_test_mail("<Senders Email>","<Recivers Email>")
        
