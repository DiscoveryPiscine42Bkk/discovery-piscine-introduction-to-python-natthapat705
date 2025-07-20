# ใส่รหัสผ่านที่เราต้องการจะเทียบไว้ในตัวแปรชื่อ password
password = "Python is awesome"
# รับค่าจาก terminal แล้วนำมาเก็บไว้ในตัวแปรชื่อ prompt
prompt = input("Please enter the password: ")

# ทำการเช็คว่าถ้ารหัสผ่านที่ใส่เข้ามาตรงกับที่เราตั้งไว้ในตัวแปร password ไหม
if prompt == password:
	# ถ้าตรง: ให้ทำงานตรงนี้
	print("ACCESS GRANTED")

# หากรหัสผ่านไม่ตรง: ให้ทำงานตรงนี้แทน
else:
	print("ACCESS DENIED")