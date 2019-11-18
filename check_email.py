### não necessita instalação, a biblioteca email é nativa do python
#from email.utils import parseaddr

### é necessária a instalação da biblioteca 'v'alidate_email' e da biblioteca 'py3dns'
from validate_email import validate_email

### Valida apenas se o email esta escrito de forma correta
#print(parseaddr('diemisrl@gmail.com'))

### Valida se o email está escrito de forma correta, e valida o DNS do email, assim sabendo se ele existe ou não
is_valid = validate_email('diemisrl12345678@gmail.com', check_mx=True, verify=True)
print(is_valid)