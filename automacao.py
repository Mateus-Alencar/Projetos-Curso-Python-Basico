import pyautogui
import time

def realizar_cliques():

    time.sleep(2)  

    posicao = pyautogui.position()
    print(posicao)
    pyautogui.click(1240, 583)
    pyautogui.click(1240, 619)
    pyautogui.click(1240, 661)
    pyautogui.click(1240, 711)
    pyautogui.click(1240, 749)
    pyautogui.click(1240, 859)
    pyautogui.click(1240, 900)
    pyautogui.click(1240, 952)
    time.sleep(1) 
    pyautogui.click(1386, 210)

for _ in range(1800):
    realizar_cliques()


# x=1240, y=583
# x=1240, y=619
# x=1240, y=661
# x=1240, y=711
# x=1242, y=749

