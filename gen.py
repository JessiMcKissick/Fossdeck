import var



def cls():#clear screen   
    var.oled.fill(0)
    var.oled.show()
    
def smm(inp):#system_menu_master
    eval(inp + "()")