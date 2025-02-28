import os


file_setup = os.path.abspath(__file__)
code = os.path.join(os.path.dirname(file_setup), "code")
startup_folder = os.path.expanduser("~/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")


for file in os.listdir(code):

    if file.endswith(".ahk"):
        print(f"File: {file}")

        file_link = os.path.join(startup_folder, file)
        print(f"file_link: {file_link}")

        try:
            if os.path.exists(file_link):
                os.remove(file_link)
                print(f"Đã xóa symlink: {file_link}")
            os.symlink(os.path.abspath(os.path.join(code, file)), file_link)
            print(f"Tạo link: {file_link}")
        except OSError as e:
            print(f"Lỗi: {e}")
