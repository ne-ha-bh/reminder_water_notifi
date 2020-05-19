from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Have water now!",
            message="It lubricates the joints,It forms saliva, It boosts skin health and beauty,It cushions the brain, spinal cord, and other sensitive tissues,It regulates body temperature,It flushes body waste,It helps maintain blood pressure,The airways need it.",
            app_icon=r"C:\Users\vikas\PycharmProjects\water_reminder\icon.ico",
            timeout=15)
    time.sleep(60 * 60 * 60)
