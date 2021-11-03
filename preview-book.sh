#!/bin/bash

# Preview html in Visual Studio Code or Cloud Shell preview
python3 -m http.server --directory content/_build/html 8080
