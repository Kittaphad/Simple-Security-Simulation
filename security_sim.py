import random
import time
import string

characters = string.ascii_letters + string.digits
secret_code = ''.join(random.choice(characters) for i in range(6))

print("ระบบทดลองการโจมตีข้อมูล")
print("คอมพิวเตอร์สุ่มรหัสผ่าน 6 หลักสำเร็จแล้ว (A-Z, a-z, 0-9)")

max_attempts = 3

for i in range(max_attempts):
    guess = input(f"รอบที่ {i+1}: ลองเดารหัสผ่านดูสิ: ")

    if guess == secret_code:
        print(f"ยินดีด้วย คุณแฮ็กรหัสผ่าน {secret_code} ได้สำเร็จ")
        break
    else:
        print("รหัสไม่ถูกต้อง")
        
else:
    print("ตรวจพบการบุกรุก ระบบทำลายตัวเองเริ่มทำงาน")
    for count in range(5, 0, -1):
        print(f"ระเบิดในอีก...{count}")
        time.sleep(1)
    print("BOOM ข้อมูลทั้งหมดถูกทำลายทิ้ง")