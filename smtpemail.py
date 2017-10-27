import smtplib
#sTATRTING A LOCAT SMTP SERVER USIGN THE COMMAND:
# python -m smtpd -n -c DebuggingServer localhost:1025
sender = raw_input("Enter your mail address: ")
receavers = list(raw_input("Enter email address of receivers saperated by spaces\n").split())

msg = raw_input("Enter message: ")

message = """ From : From address <%s>
To: To address <%s>
Subject: SMTP e-mail Test

%s """ % (sender,receavers,msg)


try:
	smtpObj = smtplib.SMTP(host ="localhost" , port =1025)
	smtpObj.sendmail(sender,receavers,message)
	print "Email sent Successfully"

except Exception as e:
	print "Error: unable to send email: " , e