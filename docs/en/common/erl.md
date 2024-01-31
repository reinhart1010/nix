---
layout: page
title: common/erl (English)
description: "Run and manage programs in the Erlang programming language."
content_hash: e212720edaa3c1d3f045c52c984f346e06c0783c
last_modified_at: 2024-01-31
related_topics:
  - title: italiano version
    url: /it/common/erl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# erl

Run and manage programs in the Erlang programming language.
More information: <https://www.erlang.org>.

- Compile and run sequential Erlang program as a common script and then exit:

`erlc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>` && erl -noshell '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mymodule:myfunction(arguments)</span>`, init:stop().'`

- Connect to a running Erlang node:

`erl -remsh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodename</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` -sname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">custom_shortname</span>` -hidden -setcookie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookie_of_remote_node</span>

- Tell the Erlang shell to load modules from a directory:

`erl -pa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory_with_beam_files</span>
