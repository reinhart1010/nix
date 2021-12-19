---
layout: page
title: common/supervisord (English)
description: "Supervisor is a client/server system for controlling some processes on UNIX-like operating systems."
content_hash: 080ebc7f3825022ded570a080d1271657d0b77e1
---
# supervisord

Supervisor is a client/server system for controlling some processes on UNIX-like operating systems.
Supervisord is the server part of supervisor; it is primarily managed via a configuration file.
More information: <http://supervisord.org>.

- Start supervisord with specified configuration file:

`supervisord -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Run supervisord in the foreground:

`supervisord -n`
