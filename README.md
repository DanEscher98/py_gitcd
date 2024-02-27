# git-cd: A git subcommand

This subcommand is intended to be used in workflows where there's a branch and
directory same named and related

## Usage

```bash
git-cd .    # it coordinates branch and actual directory
git-cd ../
git-cd dir
```

```
if is_inside_a_gitrepo(dir):
    repo_st = git_get()
    if repo_st.branch == dir:
        // do nothing
        return "."
    if dir is repo_st.get_parent_dir():
        
    elif repo_st.has_branch(dir):
        // git branch dir
        // git checkout dir
        return dir
        
```

| hi   | there |
| :--- | ---   |
| adf  | asdf  |
