# how to add new features

> again read the contribution guideline to control what you sow

> derived from official pytorch wiki (contribution guide)
```bash
git fetch origin main
git checkout -b my_new_feature origin/main
git push -u origin my_new_feature

git pull --rebase origin main

# Delete a branch
git checkout main
git branch -D my_new_feature
git push --delete origin my_new_feature
```
