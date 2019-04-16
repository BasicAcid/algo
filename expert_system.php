// Try edit msg
$nbCote = 3;
$nbAnglesDroits = 0;
$nbCotesPara = 0 ;
$nbCoteMemeLg = 2;
$trouve = 0 ;

if ($nbCote > 1){
    if ($nbCote == 3){
        // triangle
        echo 'Triangle';
        exit();
        if ($nbCoteMemeLg >= 2){
            // isocèle
            echo 'Triangle isocèle';
            if ($nbAnglesDroits == 1) {
                // tri rect isocèle
                echo 'Triangle rectangle isocèle';
            }
            if ($nbCoteMemeLg == 3){
                // tri equilateral
                echo 'Triangle equilatéral';
            }
        }
        if ($nbAnglesDroits == 1){
            // tri rect
            echo 'Triangle rectangle';
        }
    }
    if ($nbCote == 4){
        // Quadrilateral
        echo 'Quadrilatère';
        if ($nbCotesPara >= 2){	    
            // trapeze (A trapezoid is a quadrilateral with exactly one pair of parallel sides)
            echo 'Trapèze';
            if ($nbCotesPara == 4){
                // parallelogramme
                echo 'Parallelogramme';
                if ($nbAnglesDroits == 4){
                    // rectangle
                    echo 'Rectangle';
                    if ($nbCoteMemeLg == 4){
                        // carré
                        echo 'Carré';
                    }
                }
                if ($nbCoteMemeLg == 4){		    
                    // losange
                    echo 'Losange';
                }	    
            }
        }	
        if ($nbCoteMemeLg == 2){
            if ($nbAnglesDroits == 0){
                // Kite (kite A kite is a quadrilateral with two distinct pairs of adjacent sides that are congruent.)
                echo 'Kite';
            }
        }
    }       
}

if($nbCote==5){
    echo 'Pentagone';
}
if($nbCote==6){
    echo 'Hexagone';
}
if($nbCote==8){
    echo 'Heptagone';
}
if($nbCote==8){
    echo 'Hoctogone';
}
