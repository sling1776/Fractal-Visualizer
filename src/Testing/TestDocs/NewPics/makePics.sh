#!/bin/bash
#echo "hello world" //print to screen
if [[ "$PWD" =~ NewPics ]]
then
    echo "Preparing to run python programs..."
    echo " "

    sed -i '51s/.*/    print("You are Awesome")/' "../../../main.py"

    sed -i '51s/.*/    mainloop()/' "../../../main.py"
#    echo "Creating Mandelbrot Image..."
#    python "../../../main.py" "mandelbrot"
#    echo "Creating Spiral0 Image..."
#    python "../../../main.py" "spiral0"
#    echo "Creating Spiral1 Image..."
#    python "../../../main.py" "Spiral1"
#    echo "Creating Seahorse Image..."
#    python "../../../main.py" "seahorse"
#    echo "Creating Elephants Image..."
#    python "../../../main.py" "elephants"
#    echo "Creating Leaf Image..."
#    python "../../../main.py" "leaf"
#    echo "Creating Full Julia Image..."
#    python "../../../main.py" "fulljulia"
#    echo "Creating Hourglass Image..."
#    python "../../../main.py" "Hourglass"
#    echo "Creating Lakes Image..."
#    python "../../../main.py" "lakes"

else
  echo "Please navigate to the NewPics Directory before running this script."
fi

