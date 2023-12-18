import smtplib


def main():
    smtp_obj = smtplib.SMTP('smtp.mail.me.com', 587)
    smtp_obj.starttls()
    smtp_obj.login('mailaddress', 'Passwort')

    pairs = {'name_1': 'lmuehrke@mac.com', 'name_2': 'lmuehrke@me.com'}

    try:
        for name in pairs.keys():
            msg = ('From: {}\r\nTo: {}\r\n\r\nHi, {}'.format(smtp_obj.user,
                                                            pairs.get(name),
                                                            name))

            print('Sending email to {} at {}...'.format(name, pairs.get(name)))

            send_status = smtp_obj.sendmail(from_addr=smtp_obj.user,
                                            to_addrs=pairs.get(name),
                                            msg=msg)

            if send_status != {}:
                print('There was a problem sending mail to {}.\n{}'.format(name, send_status))
    finally:
        smtp_obj.quit()

if __name__ == '__main__':
    main()
