toggle_state = "off"

def toggle():
    global toggle_state
    toggle_state = "off" if toggle_state == "on" else "on"
    return toggle_state
        
        
print(toggle())
print(toggle())