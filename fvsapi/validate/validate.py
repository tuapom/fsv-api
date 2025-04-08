import base64


def is_valid_pid(pid):
    # ตรวจสอบว่าเป็นตัวเลข 13 หลักหรือไม่
    if not pid.isdigit() or len(pid) != 13:
        return False

    # คำนวณเลขตรวจสอบ (Check digit)
    total = 0
    for i in range(12):
        total += int(pid[i]) * (13 - i)
    check_digit = (11 - (total % 11)) % 10

    # เปรียบเทียบกับหลักที่ 13
    return check_digit == int(pid[-1])


def is_base64(s):
    try:
        # แปลง string เป็น bytes ถ้ายังไม่ใช่
        if isinstance(s, str):
            s = s.encode("utf-8")

        # ลอง decode base64
        decoded = base64.b64decode(s, validate=True)

        # Encode กลับมาแล้วต้องเหมือนเดิม (ตัด padding ออกเพื่อความยืดหยุ่น)
        if base64.b64encode(decoded).rstrip(b"=") != s.rstrip(b"="):
            return False, "Invalid base64 encoding"

        # คำนวณขนาดไฟล์หลัง decode
        file_size_kb = len(decoded) / 1024  # KB

        if file_size_kb < 15:
            return False, "File too small (must be ≥ 15KB)"
        elif file_size_kb > 1024:
            return False, "File too large (must be ≤ 1MB)"

        return True, round(file_size_kb, 2)

    except Exception:
        return False, "Invalid base64 format"
