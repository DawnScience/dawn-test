/*
 * Copyright (c) 2012 European Synchrotron Radiation Facility,
 *                    Diamond Light Source Ltd.
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 */ 
package org.dawb.test;

import org.junit.runner.RunWith;
import org.junit.runners.Suite.SuiteClasses;

/**
 * Just a collection of suites
 * @author gerring
 *
 */
@RunWith(org.junit.runners.Suite.class)
@SuiteClasses({ 
	
    
    org.dawb.passerelle.actors.test.Suite.class,
    
    // Run last as has memory leak
    org.dawb.common.python.test.Suite.class

})
public class HeadlessTest {
}
