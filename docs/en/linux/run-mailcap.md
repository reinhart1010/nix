---
layout: page
title: linux/run-mailcap (English)
description: "Run MailCap Programs."
content_hash: c9f9245577e53d032a845a308a5f93621d906b04
---
# run-mailcap

Run MailCap Programs.
Run mailcap view, see, edit, compose, print - execute programs via entries in the mailcap file (or any of its aliases) will use the given action to process each mime-type/file.
More information: <https://manned.org/run-mailcap>.

- Individual actions/programs on run-mailcap can be invoked with action flag:

`run-mailcap --action=ACTION [--option[=value]]`

- In simple language:

`run-mailcap --action=ACTION `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Turn on extra information:

`run-mailcap --action=ACTION --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Ignore any "copiousoutput" directive and forward output to standard output:

`run-mailcap --action=ACTION --nopager `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Display the found command without actually executing it:

`run-mailcap --action=ACTION --norun `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>
