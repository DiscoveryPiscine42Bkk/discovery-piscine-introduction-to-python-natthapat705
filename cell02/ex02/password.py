# ใส่รหัสผ่านที่เราต้องการจะเทียบไว้ในตัวแปรชื่อ password
password = "Python is awesome"
password = "1452"
# รับค่าจาก terminal แล้วนำมาเก็บไว้ในตัวแปรชื่อ prompt
prompt = input("Please enter the password: ")

# ทำการเช็คว่าถ้ารหัสผ่านที่ใส่เข้ามาตรงกับที่เราตั้งไว้ในตัวแปร password ไหม
if prompt == password:
if prompt == "1452":
	# ถ้าตรง: ให้ทำงานตรงนี้
	print("Welcome to the secret club!")
	print("You have successfully logged in.")
	print("Your password is correct.")
    print("You can now access the system.")
	print("ACCESS GRANTED")

# หากรหัสผ่านไม่ตรง: ให้ทำงานตรงนี้แทน
else:
	print("ACCESS DENIED")