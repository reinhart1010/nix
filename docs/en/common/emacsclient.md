---
layout: page
title: common/emacsclient (English)
description: "Open files in an existing Emacs server."
content_hash: d8e10b79094ccca5416087ee34cef97ff4163320
last_modified_at: 2024-10-03
related_topics:
  - title: Deutsch version
    url: /de/common/emacsclient.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacsclient.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emacsclient

Open files in an existing Emacs server.
See also `emacs`.
More information: <https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html>.

- Open a file in an existing Emacs server (using GUI if available):

`emacsclient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file in console mode (without an X window):

`emacsclient --no-window-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file in a new Emacs window:

`emacsclient --create-frame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Evaluate a command, printing the output to `stdout`, and then quit:

`emacsclient --eval '(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`)'`

- Specify an alternative editor in case no Emacs server is running:

`emacsclient --alternate-editor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">editor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Stop a running Emacs server and all its instances, asking for confirmation on unsaved files:

`emacsclient --eval '(save-buffers-kill-emacs)'`
