import pyautogui as py
import time
def sleep2():
    time.sleep(2)


time.sleep(5)
# Get the current position of the mouse
x, y = py.position()

# Print the x and y coordinates
print(f"Mouse position: ({x}, {y})")

for i in range(50):

#Click the item description and copy
    py.click(3125, 519, 2)
    py.hotkey('ctrl', 'a')
    py.hotkey('ctrl', 'c')

    sleep2()

#move to the chrome tab and paste the copied description
    py.click(568, 191, 2)
    py.hotkey('ctrl', 'a')
    py.hotkey('ctrl', 'v')
    sleep2()
    py.hotkey('enter')
    time.sleep(7)
    sleep2()

# Click the picture icon
    py.click(4251, 460, 2)
    py.click(4241, 541, 2)
    py.click(3700, 784, 2)

    sleep2()

    py.move(2695, 221, 2)
    py.rightClick()
    py.click(2748, 1005, 2)

    sleep2()

    py.moveTo(129, 487, 2)
    py.dragTo(2894, 406, 2)
    py.click(3204, 875, 2)

    sleep2()

    py.click(4753, 740, 2)


time.sleep(10)
