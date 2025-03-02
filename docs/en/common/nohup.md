---
layout: page
title: common/nohup (English)
description: "Allows for a process to live when the terminal gets killed."
content_hash: 182e76d000fc73101dc2411cd90d8c0e8ac53c9d
last_modified_at: 2025-03-02
related_topics:
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nohup.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nohup.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/nohup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nohup

Allows for a process to live when the terminal gets killed.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

- Run a process that can live beyond the terminal:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Launch `nohup` in background mode:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>` &`

- Run a shell script that can live beyond the terminal:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sh</span>` &`

- Run a process and write the output to a specific file:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` &`
