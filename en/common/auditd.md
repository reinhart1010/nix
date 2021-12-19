---
layout: page
title: common/auditd (English)
description: "This responds to requests from the audit utility and notifications from the kernel."
content_hash: 91f3cb5577c09fe3e732a2ac766286592dff2b4a
---
# auditd

This responds to requests from the audit utility and notifications from the kernel.
It should not be invoked manually.
More information: <https://manned.org/auditd>.

- Start the daemon:

`auditd`

- Start the daemon in debug mode:

`auditd -d`

- Start the daemon on-demand from launchd:

`auditd -l`
