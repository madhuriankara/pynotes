# notes
Basic Template

## To Verify in your local browser
1. Run `jupyter nbconvert --to notebook --execute make.ipynb`
2. Run `cd hugo-site`
3. Run `hugo server -D`
4. Check here: http://localhost:1313/hugobase-new/

## To Deploy

1. Run `jupyter nbconvert --to notebook --execute make.ipynb`
2. Run `cd hugo-site`
3. Run `hugo`
4. Run `git add -A`
5. Run `git commit -m "commit message`
6. Run `git push`

Site's html is in the master branch's `/docs` folder.

## Note

make.ipynb does not work on Windows
