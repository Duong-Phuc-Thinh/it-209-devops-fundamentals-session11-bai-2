import os
import re
import sys

WORKFLOW_PATH = os.path.join(".github", "workflows", "ci.yml")

def validate_workflow(filepath: str) -> bool:
    """Kiểm tra tính hợp lệ và các yêu cầu đề bài trong file workflow ci.yml."""
    if not os.path.isfile(filepath):
        print(f"[LỖI] Không tìm thấy tệp workflow: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("actions/checkout@v4", "Bước checkout mã nguồn (actions/checkout@v4)"),
        ("actions/setup-java@v4", "Bước cấu hình Java JDK (actions/setup-java@v4)"),
        ("./gradlew test", "Bước chạy kiểm thử unit test"),
        ("./gradlew bootJar", "Bước biên dịch và đóng gói bootJar (./gradlew bootJar)"),
        ("actions/upload-artifact@v4", "Action lưu trữ artifact (actions/upload-artifact@v4)"),
        ("name: app-jar", "Tên artifact là 'app-jar'"),
        ("path: build/libs/*.jar", "Đường dẫn tệp artifact là 'build/libs/*.jar'")
    ]

    print("=" * 60)
    print("KIỂM TRA CẤU HÌNH WORKFLOW GITHUB ACTIONS")
    print("=" * 60)

    all_passed = True
    for pattern, description in checks:
        if pattern in content:
            print(f" [V] {description}: ĐẠT")
        else:
            print(f" [X] {description}: THIẾU")
            all_passed = False

    print("=" * 60)
    if all_passed:
        print("-> Workflow đã đáp ứng đầy đủ tất cả tiêu chí của Bài 2!")
    else:
        print("-> Cần kiểm tra lại nội dung tệp workflow.")
    print("=" * 60)
    return all_passed

def simulate_local_packaging():
    """Mô phỏng quá trình tạo thư mục build/libs và file jar giả lập để kiểm thử."""
    output_dir = os.path.join("build", "libs")
    os.makedirs(output_dir, exist_ok=True)
    sample_jar = os.path.join(output_dir, "demo-app-0.0.1-SNAPSHOT.jar")
    
    with open(sample_jar, "wb") as f:
        # Header tối thiểu của file ZIP/JAR (PK\x03\x04)
        f.write(b"PK\x03\x04\x14\x00\x00\x00\x08\x00MOCK_SPRING_BOOT_JAR_PAYLOAD")
        
    print(f"[INFO] Đã tạo thành công tệp giả lập artifact: {sample_jar}")

def main():
    print("Bắt đầu kiểm tra hệ thống CI/CD...")
    simulate_local_packaging()
    success = validate_workflow(WORKFLOW_PATH)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
