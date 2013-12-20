source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))


def main():

    startOrAttachToDAWN()
    openPerspective("DExplore")
    #Open data browsing perspective 
    
    expand(waitForObjectItem(":Project Explorer_Tree", "Workflow"))
    expand(waitForObjectItem(":Project Explorer_Tree", "output"))
    expand(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "BigData"))
    
    
    for child in children:
        if "Export.h5" in child.text:
            doubleClick(child, 5, 5, 0, Button.Button1)
            break
    
    expand(waitForObjectItem(":Tree_Tree", "entry"))
    expand(waitForObjectItem(":Tree_Tree", "data"))
    doubleClick(waitForObjectItem(":Tree_Tree", "image"), 29, 11, 0, Button.Button1)
    mouseClick(waitForObjectItem(":Tree_Tree", "image"), 13, 12, 0, Button.Button1)
    mouseClick(waitForObject(":_Twistie"), 10, 4, 0, Button.Button1)
    snooze(5)
    setValue(waitForObject(":_Slider_2"), 45)

    mouseClick(waitForObject(":Export.h5_CTabCloseBox"), 7, 4, 0, Button.Button1)
    openPerspective("Data Browsing (default)")
    mouseClick(waitForObject(":Show Welcome Screen_ToolItem"), 12, 19, 0, Button.Button1)
    
    closeOrDetachFromDAWN()