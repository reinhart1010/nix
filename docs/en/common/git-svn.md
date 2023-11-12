---
layout: page
title: common/git-svn (English)
description: "Bidirectional operation between a Subversion repository and Git."
content_hash: c878e97eb7691e8725572d765e9a5787e06bf2f8
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/git-svn.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-svn.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-svn.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-svn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git svn

Bidirectional operation between a Subversion repository and Git.
More information: <https://git-scm.com/docs/git-svn>.

- Clone an SVN repository:

`git svn clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/subversion_repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_dir</span>

- Clone an SVN repository starting at a given revision number:

`git svn clone -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>`:HEAD `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://svn.example.net/subversion/repo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_dir</span>

- Update local clone from the remote SVN repository:

`git svn rebase`

- Fetch updates from the remote SVN repository without changing the Git HEAD:

`git svn fetch`

- Commit back to the SVN repository:

`git svn dcommit`
