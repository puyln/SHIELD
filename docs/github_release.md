# Creating the GitHub Repository

The GitHub CLI is not installed in the current local environment, so create the remote repository through the GitHub website.

Recommended steps:

```bash
cd SHIELD-code-project
git init
git add .
git commit -m "Initial SHIELD code release"
git branch -M main
git remote add origin https://github.com/<USER_OR_ORG>/<REPO_NAME>.git
git push -u origin main
```

Recommended repository name:

```text
SHIELD
```

Before making the repository public, confirm that no patient data, checkpoints, private paths, or unreleased manuscript files have been added.

