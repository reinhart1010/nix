---
layout: page
title: common/git-bugreport (English)
description: "Captures debug information from the system and user, generating a text file to aid in the reporting of a bug in Git."
content_hash: 410f14d8ba4a2ebca0d547823e476e05a29b1cb6
last_modified_at: 2024-10-13
related_topics:
  - title: Indonesia version
    url: /id/common/git-bugreport.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bugreport.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bugreport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bugreport

Captures debug information from the system and user, generating a text file to aid in the reporting of a bug in Git.
More information: <https://git-scm.com/docs/git-bugreport>.

- Create a new bug report file in the current directory:

`git bugreport`

- Create a new bug report file in the specified directory, creating it if it does not exist:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output-directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a new bug report file with the specified filename suffix in `strftime` format:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--suffix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
