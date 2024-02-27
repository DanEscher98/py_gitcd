from typing import Optional
from git.repo import Repo
from git import GitCommandError, \
    InvalidGitRepositoryError, NoSuchPathError


def find_parent_branch(repo_path: str, branch_name: str) -> Optional[str]:
    try:
        repo = Repo(repo_path)
    except (InvalidGitRepositoryError, NoSuchPathError) as e:
        print(f"Error: {e}")
        return None

    if branch_name not in repo.branches:
        print(f"Error: Branch '{branch_name}' does not exist")
        return None

    branch = repo.branches[branch_name]

    # Find the commit where the branch was created
    # (first parent of the first commit in the branch)
    try:
        branch_base = branch.commit.parents[0]
    except IndexError:
        print(f"Error: Branch '{branch_name}' does not have any commits")
        return None

    parent_branch = None
    for b in repo.branches:
        if b == branch:
            continue
        if branch_base in b.commit.iter_parents():
            parent_branch = b
            break

    if parent_branch is None:
        print(f"No parent branch found for '{branch_name}'")
        return None

    return parent_branch.name
