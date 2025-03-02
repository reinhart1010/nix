---
layout: page
title: common/sgpt (English)
description: "Command-line productivity tool powered by OpenAI's GPT models."
content_hash: 1f24c7b02c4a9122a71549efbd859aceb9409022
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/common/sgpt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sgpt

Command-line productivity tool powered by OpenAI's GPT models.
More information: <https://github.com/TheR1D/shell_gpt#readme>.

- Use it as a search engine, asking for the mass of the sun:

`sgpt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mass of the sun</span>`"`

- Execute Shell commands, and apply `chmod 444` to all files in the current directory:

`sgpt --shell "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make all files in current directory read only</span>`"`

- Generate code, solving classic fizz buzz problem:

`sgpt --code "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">solve fizz buzz problem using Python</span>`"`

- Start a chat session with a unique session name:

`sgpt --chat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">session_name</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">please remember my favorite number: 4</span>`"`

- Start a `REPL` (Read-eval-print loop) session:

`sgpt --repl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Display help:

`sgpt --help`
