import pyotp

uniqueId = pyotp.random_base32()

url = pyotp.totp.TOTP(uniqueId).provisioning_uri(name='nigelreign', issuer_name='ReignBee')

qrCode = f"https://www.google.com/chart?chs=200x200&chld=M|0&cht=qr&chl={url}"

# Scan this code using an authenticator app
print(qrCode)
