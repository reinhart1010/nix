---
layout: page
title: linux/lynis (English)
description: "System and security auditing tool."
content_hash: 813477bc757e7aece0853e1a08045ca9ddc45e01
---
# lynis

System and security auditing tool.
More information: <https://cisofy.com/documentation/lynis/>.

- Check that Lynis is up-to-date:

`sudo lynis update info`

- Run a security audit of the system:

`sudo lynis audit system`

- Run a security audit of a Dockerfile:

`sudo lynis audit dockerfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dockerfile</span>
