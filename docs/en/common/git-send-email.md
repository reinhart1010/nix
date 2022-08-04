---
layout: page
title: common/git-send-email (English)
description: "Send a collection of patches as emails."
content_hash: 78455f58958d457c0941584d06c3d75a0d44e749
related_topics:
  - title: français version
    url: /fr/common/git-send-email.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-send-email.html
    icon: bi bi-globe
---
# git send-email

Send a collection of patches as emails.
Patches can be specified as files, directions, or a revision list.
More information: <https://git-scm.com/docs/git-send-email>.

- Send the last commit in the current branch:

`git send-email -1`

- Send a given commit:

`git send-email -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Send multiple (e.g. 10) commits in the current branch:

`git send-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10</span>

- Send an introductory email message for the patch series:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_commits</span>` --compose`

- Review and edit the email message for each patch you're about to send:

`git send-email -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_commits</span>` --annotate`
