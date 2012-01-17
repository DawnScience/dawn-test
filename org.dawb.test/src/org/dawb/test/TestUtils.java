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

import org.osgi.framework.Bundle;

public class TestUtils {

	/**
	 * 
	 * @param relPath = to pluging
	 * @return
	 */
	public static String getAbsolutePath(final Bundle bundle, final String relPath) {
		String dir = cleanPath(bundle.getLocation());
		return dir+relPath;
	}

	
	public static String cleanPath(String loc) {
		
		// Remove reference:file: from the start. TODO find a better way,
	    // and test that this works on windows (it might have ///)
        if (loc.startsWith("reference:file:")){
        	loc = loc.substring(15);
        } else if (loc.startsWith("file:")) {
        	loc = loc.substring(5);
        } else {
        	return loc;
        }
        
        loc = loc.replace("//", "/");
        loc = loc.replace("\\\\", "\\");

        return loc;
	}

}
