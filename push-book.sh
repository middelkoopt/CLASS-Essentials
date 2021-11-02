#!/bin/bash

# Set origin to $1 with a default of "private"
ORIGIN="${1:-private}"
echo "push-book.sh ORIGIN:${ORIGIN}"

BRANCH=$(git symbolic-ref --short HEAD)
git branch -D gh-pages
git checkout -b gh-pages

rm -rf docs/
cp -av content/_build/html/ docs/
touch docs/.nojekyll ## config static

git add docs/
git commit -m "Publish Jupyerbook" docs/

git push --force ${ORIGIN} gh-pages

git checkout ${BRANCH}
