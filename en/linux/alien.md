---
layout: page
title: linux/alien (English)
description: "Convert different installation packages to other formats."
content_hash: cff6ab38e3558da93405587160dba064408f4b95
---
# alien

Convert different installation packages to other formats.
More information: <https://manned.org/alien>.

- Convert a specific installation file to Debian format (`.deb` extension):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert a specific installation file to Red Hat format (`.rpm` extension):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert a specific installation file to a Slackware installation file (`.tgz` extension):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Convert a specific installation file to Debian format and install on the system:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
