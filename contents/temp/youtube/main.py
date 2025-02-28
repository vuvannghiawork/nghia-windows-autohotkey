import os
import time
import pyautogui


TIMEOUT_SECONDS = 60
TIME_SLEEP = 1


def main():
    file = os.path.abspath(__file__)
    folder = os.path.dirname(file)
    image_skip_path = os.path.join(folder, 'screenshot_cursor.png')

    if not os.path.exists(image_skip_path):
        print("Image not found")
        exit()

    start_time = time.time()

    while time.time() - start_time < TIMEOUT_SECONDS:
        try:
            location = pyautogui.locateOnScreen(image_skip_path, confidence=0.7, grayscale=True)

            if location:
                print(f"Đã tìm thấy ảnh tại: {location}")
                pyautogui.click(location)
                break

        except pyautogui.ImageNotFoundException:
            print("Không tìm thấy ảnh, tiếp tục kiểm tra...")
        time.sleep(TIME_SLEEP)


if __name__ == "__main__":
    main()
