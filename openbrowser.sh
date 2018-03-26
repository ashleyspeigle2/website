#!/bin/bash
if [ -n $BROWSER ]; then
  $BROWSER 'https://docs.python.org/3/'
elif which xdg-open > /dev/null; then
  xdg-open 'https://docs.python.org/3/'
elif which gnome-open > /dev/null; then
  gnome-open 'https://docs.python.org/3/'

else
  echo "Could not detect the web browser to use."

fi
 
done
