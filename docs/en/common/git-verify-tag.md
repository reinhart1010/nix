---
layout: page
title: common/git-verify-tag (English)
description: "Check for GPG verification of tags."
content_hash: 4069655cfa5bee8e554772a4c9ba83d0879c7e51
---
# git verify-tag

Check for GPG verification of tags.
If a tag wasn't signed, an error will occur.
More information: <https://git-scm.com/docs/git-verify-tag>.

- Check tags for a GPG signature:

`git verify-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag1 optional_tag2 ...</span>

- Check tags for a GPG signature and show details for each tag:

`git verify-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag1 optional_tag2 ...</span>` --verbose`

- Check tags for a GPG signature and print the raw details:

`git verify-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag1 optional_tag2 ...</span>` --raw`
