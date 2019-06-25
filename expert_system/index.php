<html>
 <head>
  <title>Test PHP</title>
 </head>
 <body>

 <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
   <p>
       <label for="cotes">nombre de côtés ?</label><br />
       <input type="text" name="cotes" id="cotes">
   </p>
   <p>
       <label for="angles">nombre d'angles droits' ?</label><br />
       <input type="text" name="angles" id="angles">
   </p>
   <p>
       <label for="para">nombre de côtés parallèles ?</label><br />
       <input type="text" name="para" id="para">
   <p>
       <label for="longueur">nombre de côtés de même longueurs ?</label><br />
       <input type="text" name="longueur" id="longueur">
   </p>
   <input type="submit" id="submit" name="submit" value="envoyer">
</form>

<?php 


$link = mysqli_connect('localhost', 'root', '')
or die('Impossible de se connecter : ' . mysql_error());
//echo 'Connected successfully';
mysqli_select_db($link,'Formes') or die('Impossible de sélectionner la base de données');


getFormes($link);


if ( isset( $_POST['submit'] ) ) {
    $nbCote = $_POST["cotes"];
    //var_dump($nbCote);
    $nbAnglesDroits = $_POST["angles"];
    //var_dump($nbAnglesDroits);
    $nbCotesPara = $_POST["para"];
    //var_dump($nbCotesPara);
    $nbCoteMemeLg = $_POST["longueur"];
    //var_dump($nbCoteMemeLg);
    

    $nomForme = '';

    if(!getForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg)){

    if ($nbCote > 1){
        if ($nbCote == 3){
            if ($nbAnglesDroits > 1){
                echo 'Forme invalide';
                exit();
                
            }
            if ($nbCotesPara != 0){
                echo 'Forme invalide';
                exit();
            }
            if ($nbCoteMemeLg > 3){
                echo 'Forme invalide';
                exit();
            }
            // triangle
            if ($nbCoteMemeLg == 2){
                // isocèle
                if ($nbAnglesDroits == 1) {
                    // tri rect isocèle
                    echo 'Triangle rectangle isocèle';
                    $nomForme = 'Triangle rectangle isocèle';
                    insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                    
                }  
                echo 'Triangle isocèle';
                $nomForme = 'Triangle isocèle';
                insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
            }
            if ($nbCoteMemeLg == 3){
                // tri equilateral
                echo 'Triangle equilatéral';
                $nomForme = 'Triangle equilatéral';
                insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                
            }
            if ($nbAnglesDroits == 1){
                // tri rect
                echo 'Triangle rectangle';
                $nomForme = 'Triangle rectangle';
                insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
               
            }
            echo 'Triangle';
            $nomForme = 'Triangle';
            insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
        }
        if ($nbCote == 4){
            // Quadrilatere
            if ($nbAnglesDroits > 4){
                echo 'Forme invalide';
                exit();
                
            }
            if ($nbCotesPara > 4){
                echo 'Forme invalide';
                exit();
                
            }
            if ($nbCoteMemeLg > 4){
                echo 'Forme invalide';
                exit();
                
            }
            if ($nbCotesPara >= 2){
                // trapeze (A trapezoid is a quadrilateral with exactly one pair of parallel sides)
                if ($nbCotesPara == 4){
                    // parallelogramme
                    if ($nbAnglesDroits > 1){
                        if ($nbCoteMemeLg == 4){
                            // carré
                            echo 'Carré';
                            $nomForme = 'Carré';
                            insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                            
                        }
                        // rectangle

                        if ($nbCoteMemeLg == 2){
                        echo 'Rectangle';
                        $nomForme = 'Rectangle';
                        insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                        
                        }
                    }
                    if ($nbCoteMemeLg == 4){
                        // losange
                        echo 'Losange';
                        $nomForme = 'Losange';
                        insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                        
                    }
                }
                if ($nbCotesPara == 2){
                    echo 'Trapèze';
                    $nomForme = 'Trapèze';
                    insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                    
                }
                
                echo 'Parallelogramme';
                $nomForme = 'Parallelogramme';
                insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                
            }
            if ($nbCoteMemeLg == 2){
                if ($nbAnglesDroits == 0){
                    // Kite (kite A kite is a quadrilateral with two distinct pairs of adjacent sides that are congruent.)
                    echo 'Kite';
                    $nomForme = 'Kite';
                    insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
                    
                }
            }
            echo 'Quadrilatère quelconque';
            $nomForme = 'Quadrilatère quelconque';
            insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
            
            }      
    }
     
    if($nbCote==5){
        echo 'Pentagone';
        $nomForme = 'Pentagone';
        insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
    }

    if($nbCote==6){
        echo 'Hexagone';
        $nomForme = 'Hexagone';
        insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg);
    }
    
    if($nbCote==8){
        echo 'Octogone';
        $nomForme = 'Octogone';
        insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCotesPara,$nbCoteMemeLg);
    }
}
}


function build_table($array){
    // start table
    $html = '<table border="1">';
    // header row
    $html .= '<tr>';

    
    foreach($array[0] as $key=>$value){
            $html .= '<th>' . htmlspecialchars($key) . '</th>';
        }
    $html .= '</tr>';

    // data rows
    foreach( $array as $key=>$value){
        $html .= '<tr>';
            foreach($value as $key2=>$value2){
            $html .= '<td>' . htmlspecialchars($value2) . '</td>';
            
        }
        $html .= '</tr>';
    }
        // finish table and return it
        $html .= '</table>';
        return $html;
    
}



function getFormes($link){
    // Exécution des requêtes SQL
    $query = 'SELECT * FROM Formes';
    $result = mysqli_query($link,$query, MYSQLI_USE_RESULT) or die('Échec de la requête : ' . mysqli_error());

    $array = array(
        array('Forme'=>'', 'Nombre côtés'=>'', 'Nombre angles droits'=>'', 'Nombre côtés prallèles'=>'','Nombre côtés même longueur'=>''));
    
        $i=0;

    while ($row=mysqli_fetch_row($result)) {
        
            $array[$i]=array('Forme'=>$row[1], 'Nombre côtés'=>$row[2], 'Nombre angles droits'=>$row[3],
             'Nombre côtés prallèles'=>$row[4],'Nombre côtés même longueur'=>$row[5]);
             $i++;
    }
    echo build_table($array);

}




function getForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg){

    $query = 'SELECT nomForme FROM Formes WHERE nbCotes = '.$nbCote.' AND nbAngleDroits = '.$nbAnglesDroits.' AND nbCotesParallele ='.$nbCotesPara.' AND nbCoteMLong ='.$nbCoteMemeLg;

    if($result = mysqli_query($link,$query, MYSQLI_USE_RESULT)){

        while ($row=mysqli_fetch_row($result)) {

            echo $row[0] . ' deja connu';
            return TRUE;
        }
    }
    return FALSE;
       
    
}


function insertForme($link,$nomForme,$nbCote,$nbAnglesDroits,$nbCotesPara,$nbCoteMemeLg){
    
    $query = "INSERT INTO Formes (nomForme,nbCotes,nbAngleDroits,nbCotesParallele,nbCoteMlong) VALUES ('"
        .$nomForme."',".$nbCote.','.$nbAnglesDroits.','.$nbCotesPara.','.$nbCoteMemeLg.');';

        if (mysqli_query($link,$query, MYSQLI_USE_RESULT)) {
        } 
        else 
        {
            echo 'Échec de la requête : ' . mysqli_error($link);
        }
        header("Refresh:0");
    exit();
    
}


?>
 </body>
</html>