---
layout: page
title: common/git-diff-index (English)
description: "Compare the working directory with a commit or tree object."
content_hash: fd5c02940c47835f1a36eb3ef933090bfeae78bc
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# git diff-index

Compare the working directory with a commit or tree object.
More information: <https://git-scm.com/docs/git-diff-index>.

- Compare the working directory with a specific commit:

`git diff-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compare a specific file or directory in working directory with a commit:

`git diff-index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Compare the working directory with the index (staging area) to check for staged changes:

`git diff-index --cached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Suppress output and return an exit status to check for differences:

`git diff-index --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
