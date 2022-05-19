import pyotp

# make sure this hash is the same with the one generated 
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")

print("Current OTP:", totp.now())
