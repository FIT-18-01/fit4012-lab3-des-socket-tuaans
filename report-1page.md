# Report 1 page - Lab 3

## Thông tin nhóm
- Thành viên 1: Student 1
- Thành viên 2: Student 2

## Mục tiêu
Bài lab xây dựng hệ thống gửi nhận dữ liệu mã hóa DES qua socket TCP. Sender mã hóa bản tin bằng DES-CBC với PKCS#7 padding, gửi key, IV, header độ dài, và ciphertext. Receiver nhận và giải mã. Mục tiêu là hiểu luồng hoạt động, kiểm thử lỗi, và phân tích rủi ro bảo mật.

## Phân công thực hiện
- Thành viên 1 phụ trách Sender và mã hóa.
- Thành viên 2 phụ trách Receiver và giải mã.
- Chung: Tests, logs, threat model, report.

## Cách làm
Sender: Tạo key và IV ngẫu nhiên, mã hóa plaintext với DES-CBC, build packet với key + IV + length + ciphertext, gửi qua socket. Receiver: Lắng nghe socket, nhận packet, parse header, nhận ciphertext, giải mã. Kiểm thử: Unit tests cho padding, encryption; integration test cho roundtrip; negative tests cho wrong key, tamper.

## Kết quả
Hệ thống chạy thành công, sender gửi "Hello Lab3", receiver nhận và giải mã đúng. Logs cho thấy key, IV, ciphertext. Tests pass trừ encoding issue đã fix. Ca kiểm thử: Happy path, wrong key, tamper, padding.

## Kết luận
Bài học kỹ thuật: Socket TCP, DES-CBC, padding PKCS#7, packet structure. Bài học bảo mật: Không gửi key plaintext, cần key exchange an toàn, integrity checks, dùng AES thay DES.
