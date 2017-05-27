from datetime import datetime, date

bday = datetime.strptime('08/01/1992', '%m/%d/%Y')

today = datetime.strptime(str(date.today()), '%Y-%m-%d')
age = (today - bday).days

print age/365
