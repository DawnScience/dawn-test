source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))


def main():

    startOrAttachToDAWN()
    # Open data browsing perspective 
    openPerspective("Data Browsing (default)")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "Workflow"))
    expand(waitForObjectItem(":Project Explorer_Tree", "output"))
    expand(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    
    for child in children:
        if "Export.h5" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
    
    snooze(2)
    #mouseClick(waitForObjectItem(":Data_Table", "0/0"), 8, 5, 0, Button.Button1)
    snooze(5)
    

    clickTab(waitForObject(":Data_CTabItem"), 39, 19, 0, Button.Button1)
    clickTab(waitForObject(":Data_CTabItem"), 39, 19, 0, Button.Button3)
    activateItem(waitForObjectItem(":Pop Up Menu", "Size"))
    activateItem(waitForObjectItem(":Size_Menu", "Left"))
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    type(waitForObject(":_Sash"), "<Left>")
    clickTab(waitForObject(":Data_CTabItem"), 33, 27, 0, Button.Button1)

    mouseClick(waitForObject(":Edit the slice with different editors._ToolItem"), 29, 10, 0, Button.Button1)
    activateItem(waitForObjectItem(":Pop Up Menu", "Slice index (only)"))
    mouseClick(waitForObjectItem(":Data_Table_2", "0/2"), 89, 18, 0, Button.Button1)
    snooze(1)
    for i in range(0,100,10):
        setValue(waitForObject(":Data_Spinner"), i)
        snooze(0.01)

    mouseClick(waitForObject(":Slice as line plots_ToolItem"), 13, 10, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/2"), 91, 23, 0, Button.Button1)
    snooze(1)
    for i in range(0,2000,100):
        setValue(waitForObject(":Data_Spinner"), i)
        snooze(0.01)


        
    mouseClick(waitForObject(":Slice as image_ToolItem"), 10, 13, 0, Button.Button1)
    mouseClick(waitForObject(":Keep aspect ratio_ToolItem"), 7, 6, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/2"), 84, 16, 0, Button.Button1)
    snooze(1)

    mouseClick(waitForObjectItem(":Data_Table_2", "0/1"), 45, 16, 0, Button.Button1)
    mouseClick(waitForObject(":Data_CCombo"), 48, 27, 0, Button.Button1)
    mouseClick(waitForObjectItem(":_List", "Y"), 22, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/2"), 26, 22, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/3"), 64, 45, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Data_Table_2", "1/2"), 90, 32, 0, Button.Button1)

    for i in range(0, 2000, 100):
        setValue(waitForObject(":Data_Spinner"), i)

        snooze(0.01)
    
    mouseClick(waitForObject(":Export.h5_CTabCloseBox"), 7, 4, 0, Button.Button1)
    openPerspective("Data Browsing (default)")
    mouseClick(waitForObject(":Show Welcome Screen_ToolItem"), 12, 19, 0, Button.Button1)
    closeOrDetachFromDAWN()