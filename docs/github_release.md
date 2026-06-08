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

Before making or updating the repository public, confirm that no patient data, checkpoints, private paths, or unreleased manuscript files have been added.

## Pre-Submission Checklist

- Run `python -m compileall -q scripts shield`.
- Run every command in the README with `--dry-run`.
- Confirm repository-wide search returns no local home directories, cloud-sync paths, private training-log paths, patient names, hospital IDs, or checkpoint references outside documented example paths.
- Confirm `git status --ignored --short` only lists ignored cache files such as `.DS_Store` or `__pycache__`.
- Confirm `LICENSE`, `NOTICE.md`, and `THIRD_PARTY_NOTICES.md` are present.
- Confirm README and project-page links match the public GitHub repository URL.
