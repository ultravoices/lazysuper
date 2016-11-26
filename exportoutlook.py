import win32com.client

def send_mail_via_com(text, subject, recipient, profilename="Outlook2003"):
    s = win32com.client.Dispatch("Mapi.Session")
    o = win32com.client.Dispatch("Outlook.Application")
    s.Logon(profilename)

    Msg = o.CreateItem(0)
    Msg.To = recipient

    Msg.CC = "moreaddresses here"
    Msg.BCC = "address"

    Msg.Subject = subject
    Msg.Body = text

    attachment1 = "Path to attachment no. 1"
    attachment2 = "Path to attachment no. 2"
    Msg.Attachments.Add(attachment1)
    Msg.Attachments.Add(attachment2)

    Msg.Send()