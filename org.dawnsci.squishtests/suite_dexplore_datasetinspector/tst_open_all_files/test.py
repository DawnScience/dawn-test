source(findFile("scripts", "dawn_global_startup.py"))
source(findFile("scripts", "dawn_global_plot_tests.py"))
source(findFile("scripts", "use_case_utils.py"))

def main():
    startOrAttachToDAWN()
    
    openPerspective("DExplore")
    
    system = getPlottingSystem("Dataset Plot")
    
    expand(waitForObjectItem(":Project Explorer_Tree", "data"))
    expand(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    children = object.children(waitForObjectItem(":Project Explorer_Tree", "examples"))
    
    data = None
    for child in children:
        if not "." in child.text or "spec" in child.text or "nxs" in child.text:
            continue
        
        doubleClick(child, 5, 5, 0, Button.Button1)
        snooze(5)
        data_new = system.getTraces().toArray().at(0).getData()
        test.verify(data != data_new)
        data = data_new
        
    
    closeOrDetachFromDAWN()