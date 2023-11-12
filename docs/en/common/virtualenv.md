---
layout: page
title: common/virtualenv (English)
description: "Create virtual isolated Python environments."
content_hash: 132b0050af898fd4460b318c3cf970b26cb0a363
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/common/virtualenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virtualenv

Create virtual isolated Python environments.
More information: <https://virtualenv.pypa.io/>.

- Create a new environment:

`virtualenv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>

- Customize the prompt prefix:

`virtualenv --prompt=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt_prefix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>

- Use a different version of Python with virtualenv:

`virtualenv --python=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/pythonbin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>

- Start (select) the environment:

`source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/venv</span>`/bin/activate`

- Stop the environment:

`deactivate`
