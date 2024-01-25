---
layout: page
title: common/vipe (English)
description: "Run a text editor in the middle of a UNIX pipeline."
content_hash: b1c78ef2f2a97c4a95e61718576268eabd770d01
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# vipe

Run a text editor in the middle of a UNIX pipeline.
More information: <https://joeyh.name/code/moreutils/>.

- Edit the output of `command1` before piping it into `command2`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | vipe | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>

- Buffer the output of `command1` in a temporary file with the specified file extension in order to aid syntax highlighting:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | vipe --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>

- Use the specified text editor:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command1</span>` | EDITOR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vim</span>` vipe | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command2</span>
