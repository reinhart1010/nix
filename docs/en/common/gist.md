---
layout: page
title: common/gist (English)
description: "Upload code to https://gist.github.com."
content_hash: 48f234ca7f1aab27a82134e82a19971d58e73304
last_modified_at: 2023-11-12
related_topics:
  - title: українська version
    url: /uk/common/gist.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gist

Upload code to https://gist.github.com.
More information: <https://github.com/defunkt/gist>.

- Log in in gist on this computer:

`gist --login`

- Create a gist from any number of text files:

`gist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.txt</span>

- Create a private gist with a description:

`gist --private --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A meaningful description</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>` `

- Read contents from `stdin` and create a gist from it:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "hello world"</span>` | gist`

- List your public and private gists:

`gist --list`

- List all public gists for any user:

`gist --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Update a gist using the ID from URL:

`gist --update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GIST_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.txt</span>
