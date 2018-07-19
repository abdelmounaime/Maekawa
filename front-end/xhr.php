<?php
/**
 * Created by PhpStorm.
 * User: magic
 * Date: 19/06/2018
 * Time: 01:31
 */


if (isset($_GET['cpt'])) {
    if (file_exists('output/'.$_GET['cpt'] . '.txt'))
    {
        $file = fopen('output/'.$_GET['cpt'] . '.txt', 'r');
        $line = fgets($file);
        fclose($file);
        unlink('output/'.$_GET['cpt'] . '.txt');
        echo $line;
    }
    else
    {
        echo '0';
    }

}
else
{
    echo '0';
}