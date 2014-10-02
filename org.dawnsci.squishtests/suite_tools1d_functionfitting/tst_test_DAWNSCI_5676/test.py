source(findFile("scripts", "function_fitting_common.py"))

def main():
    
    startFunctionFitting()
    setFunctionFittingRegion(45, 10)
    
    # maximise Function Fitting
    doubleClick(waitForObject(":Function Fitting_CTabItem"))
    
    # insert a Gaussian and check the initial parameters
    insertFunction("Gaussian")
    checkGaussian(fitted=False, posn_user_value=0.0)
    
    # Set the posn to 50 and ...
    setField(["Gaussian", "posn"], VALUE_COL, 50.0)
    # ... make sure it ...
    test.verify(float(getField(["Gaussian", "posn"], VALUE_COL)) == 50.0)
    # ... and nothing else is changed
    checkGaussian(fitted=False, posn_user_value=50.0)

    # click fit once ...
    clickButton(waitForObject(":Function Fitting.Fit Once_Button"))
    # ... and make sure that only fitted column has changes in it 
    # This is where the first symptom of DAWNSCI-5676 was picked up, 
    # the value column would change for all the parameters
    checkGaussian(fitted=True, posn_user_value=50.0)
    # set the posn to a new value ...
    setField(["Gaussian", "posn"], VALUE_COL, 1000.0)
    # ... and make sure that only the posn Value changed
    # This is the second symptom of DAWNSCI-5676, changing the 
    # value would also change the fitted value, even though
    # not fit has been done
    checkGaussian(fitted=True, posn_user_value=1000.0)
    
    
    closeOrDetachFromDAWN()


def checkGaussian(fitted, posn_user_value):
    tree_texts = get_swt_tree_texts(waitForObject(":Function Fitting_Tree"))
    test.log(str(tree_texts))

    gaussian = tree_texts.children[0]
    test.verify(gaussian.column.Function_Name == "Gaussian", "Gaussian Function Exists")
    gaussian_posn = gaussian.children[0]
    test.verify(gaussian_posn.column.Function_Name == "posn", "posn parameter exists")
    test.verify(float(gaussian_posn.column.Value) == posn_user_value, "posn == " + str(posn_user_value))
    
    test.verify(gaussian_posn.column.Lower_Limit == "Min Double", "posn lower limit Min Double")
    test.verify(gaussian_posn.column.Upper_Limit == "Max Double", "posn lower limit Max Double")
    if fitted:
        test.verify(abs(50.0 - float(gaussian_posn.column.Fitted_Parameters)) < 5.0, "posn fitted paramter within 5.0 of 50.0")
    else:
        test.verify(gaussian_posn.column.Fitted_Parameters == "Not defined", "posn fitted paramter while not fitted is 0.0")
    del gaussian_posn
    
    gaussian_fwhm = gaussian.children[1]
    test.verify(gaussian_fwhm.column.Function_Name == "fwhm", "fwhm parameter exists")
    test.verify(float(gaussian_fwhm.column.Value) == 0.0, "fwhm == 0.0")
    test.verify(float(gaussian_fwhm.column.Lower_Limit) == 0.0, "fwhm lower limit 0.0")
    test.verify(gaussian_fwhm.column.Upper_Limit == "Max Double", "fwhm lower limit Max Double")
    if fitted:
        test.verify(abs(2.5 - float(gaussian_fwhm.column.Fitted_Parameters)) < .25, "fwhm fitted paramter within .25 of 2.5")
    else:
        test.verify(gaussian_fwhm.column.Fitted_Parameters == "Not defined", "fwhm fitted paramter while not fitted is 0.0")
    del gaussian_fwhm

    gaussian_area = gaussian.children[2]
    test.verify(gaussian_area.column.Function_Name == "area", "area parameter exists")
    test.verify(float(gaussian_area.column.Value) == 0.0, "area == 0.0")
    test.verify(gaussian_area.column.Lower_Limit == "Min Double", "area lower limit Min Double")
    test.verify(gaussian_area.column.Upper_Limit == "Max Double", "area lower limit Max Double")
    if fitted:
        test.verify(abs(500.0 - float(gaussian_area.column.Fitted_Parameters)) < 50.0, "area fitted paramter within 50.0 of 500.0")
    else:
        test.verify(gaussian_area.column.Fitted_Parameters == "Not defined", "area fitted paramter while not fitted is 0.0")
    del gaussian_area
    
    del gaussian
    
    add_new = tree_texts.children[1]
    test.verify(add_new.column.Function_Name == "Add new function", "Add new function is present")

