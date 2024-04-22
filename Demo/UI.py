class UIComponent:
    def draw(self):
        print("Drawing UI component")

class Button(UIComponent):
    def click(self):
        print("Button clicked")

class Checkbox(Button):
    def toggle(self):
        print("Checkbox toggled")

class Switch(Checkbox):
    def switch_on(self):
        print("Switch turned on")

class ToggleButton(Switch):
    def click(self):  # Method overriding
        print("Toggle button clicked and toggled")

def display_ui():
    toggle = ToggleButton()
    toggle.draw()
    toggle.click()  # Should trigger the overridden method
    toggle.toggle()
    toggle.switch_on()

if __name__ == "__main__":
    display_ui()