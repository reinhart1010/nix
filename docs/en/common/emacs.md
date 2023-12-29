---
layout: page
title: common/emacs (English)
description: "The extensible, customizable, self-documenting, real-time display editor."
content_hash: ddcbb681ef75b784f73d2dd312acb9f61204a7c6
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/emacs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/emacs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/emacs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# emacs

The extensible, customizable, self-documenting, real-time display editor.
See also `emacsclient`.
More information: <https://www.gnu.org/software/emacs>.

- Start Emacs and open a file:

`emacs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Open a file at a specified line number:

`emacs +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">line_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run an Emacs Lisp file as a script:

`emacs --script `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.el</span>

- Start Emacs in console mode (without an X window):

`emacs --no-window-system`

- Start an Emacs server in the background (accessible via `emacsclient`):

`emacs --daemon`

- Stop a running Emacs server and all its instances, asking for confirmation on unsaved files:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Save a file in Emacs:

`<Ctrl> + X, <Ctrl> + S`

- Quit Emacs:

`<Ctrl> + X, <Ctrl> + C`
