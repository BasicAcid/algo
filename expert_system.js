// Try edit msg
var nbCote = 3;
var nbAnglesDroits = 0;
var nbCotesPara = 0 ;
var nbCoteMemeLg = 2;
var trouve = 0 ;

if (nbCote > 1){
    if (nbCote == 3){
	// triangle
	document.write('Triangle');
	exit();
	if (nbCoteMemeLg >= 2){
	    // isocèle
	    document.write('Triangle isocèle');
	    if (nbAnglesDroits == 1) {
		// tri rect isocèle
		document.write('Triangle rectangle isocèle');
	    }
	    if (nbCoteMemeLg == 3){
		// tri equilateral
		document.write('Triangle equilatéral');
	    }
	}
	if (nbAnglesDroits == 1){
	    // tri rect
	    document.write('Triangle rectangle');
	}
    }
    if (nbCote == 4){
	// Quadrilateral
	document.write('Quadrilatère');
	if (nbCotesPara >= 2){	    
	    // trapeze (A trapezoid is a quadrilateral with exactly one pair of parallel sides)
	    document.write('Trapèze');
	    if (nbCotesPara == 4){
		// parallelogramme
		document.write('Parallelogramme');
		if (nbAnglesDroits == 4){
		    // rectangle
		    document.write('Rectangle');
		    if (nbCoteMemeLg == 4){
			// carré
			document.write('Carré');
		    }
		}
		if (nbCoteMemeLg == 4){		    
		    // losange
		    document.write('Losange');
		}	    
	    }
	}	
	if (nbCoteMemeLg == 2){
	    if (nbAnglesDroits == 0){
		// Kite (kite A kite is a quadrilateral with two distinct pairs of adjacent sides that are congruent.)
		document.write('Kite');
	    }
	}
    }       
}

if(nbCote==5){
    document.write('Pentagone');
}
if(nbCote==6){
    document.write('Hexagone');
}
if(nbCote==8){
    document.write('Heptagone');
}
if(nbCote==8){
    document.write('Hoctogone');
}
