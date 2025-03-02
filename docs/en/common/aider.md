---
layout: page
title: common/aider (English)
description: "Pair program with the LLM of your choice."
content_hash: e7732604fe2a4ef94984f18b57e23d58edba5050
last_modified_at: 2025-03-02
related_topics:
  - title: español version
    url: /es/common/aider.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aider

Pair program with the LLM of your choice.
More information: <https://github.com/Aider-AI/aider>.

- Start a new project or work with an existing code base:

`aider --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model_name</span>` --api-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your_api_key</span>

- Add new features or test cases to specific files:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Describe a bug and let `aider` fix it:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --describe "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bug_description</span>`"`

- Refactor code in a specific file:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --refactor`

- Update documentation:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --update-docs`

- Display help:

`aider --help`
