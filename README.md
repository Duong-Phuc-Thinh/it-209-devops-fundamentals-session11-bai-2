# Bài 2: Biên dịch đóng gói tệp ứng dụng .jar với Gradle và lưu trữ Artifacts

## 1. Mục tiêu
- Thực thi lệnh đóng gói ứng dụng Spring Boot thành tệp JAR thực thi: `./gradlew bootJar`.
- Đính kèm và lưu trữ tệp `.jar` từ thư mục `build/libs/` lên GitHub Actions bằng action `actions/upload-artifact@v4` với tên `app-jar`.

## 2. Cấu trúc thư mục
```text
.
├── .github/
│   └── workflows/
│       └── ci.yml        # Kịch bản GitHub Actions hoàn chỉnh
├── main.py               # Script Python kiểm tra tính hợp lệ của workflow và mô phỏng build
└── README.md             # Tài liệu hướng dẫn
```

## 3. Nội dung các bước bổ sung trong Workflow
Trong job `test` tại `.github/workflows/ci.yml`, hai bước mới đã được bổ sung:
```yaml
      - name: Đóng gói tệp JAR với Gradle
        run: ./gradlew bootJar

      - name: Lưu trữ thành phẩm JAR Artifact
        uses: actions/upload-artifact@v4
        with:
          name: app-jar
          path: build/libs/*.jar
```

## 4. Hướng dẫn chạy kiểm thử
Chạy chương trình Python để thẩm định cấu hình workflow:
```bash
python main.py
```

## 5. Kiểm tra trên GitHub Actions
1. Commit và push thay đổi lên nhánh `main`:
   ```bash
   git add .
   git commit -m "feat: add bootJar step and upload-artifact in CI workflow"
   git push origin main
   ```
2. Vào repository trên GitHub -> chọn tab **Actions** -> bấm vào workflow chạy gần nhất.
3. Tại trang **Summary**, cuộn xuống phần **Artifacts**, kiểm tra sự xuất hiện của artifact mang tên `app-jar` và có thể tải về máy.
