---
layout: page
title: common/cloc (English)
description: "Count, and compute differences of, lines of source code and comments."
content_hash: defbfafaabd8e454ce524bfe28c565528a26f5ac
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/cloc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cloc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cloc

Count, and compute differences of, lines of source code and comments.
More information: <https://github.com/AlDanial/cloc>.

- Count all the lines of code in a directory:

`cloc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Count all the lines of code in a directory, displaying a progress bar during the counting process:

`cloc --progress=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Compare 2 directory structures and count the differences between them:

`cloc --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/one</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory/two</span>

- Ignore files that are ignored by VCS, such as files specified in `.gitignore`:

`cloc --vcs git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Count all the lines of code in a directory, displaying the results for each file instead of each language:

`cloc --by-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
