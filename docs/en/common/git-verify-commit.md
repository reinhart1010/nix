---
layout: page
title: common/git-verify-commit (English)
description: "Check for GPG verification of commits."
content_hash: d8d833e1f713e83af9e459f83d6188d9bfd87d47
---
# git verify-commit

Check for GPG verification of commits.
If no commits are verified, nothing will be printed, regardless of options specified.
More information: <https://git-scm.com/docs/git-verify-commit>.

- Check commits for a GPG signature:

`git verify-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash1 optional_commit_hash2 ...</span>

- Check commits for a GPG signature and show details of each commit:

`git verify-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash1 optional_commit_hash2 ...</span>` --verbose`

- Check commits for a GPG signature and print the raw details:

`git verify-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash1 optional_commit_hash2 ...</span>` --raw`
