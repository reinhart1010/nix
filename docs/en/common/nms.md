---
layout: page
title: common/nms (English)
description: "Command-line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers from stdin."
content_hash: 30a0cce80e9c4300c70ce6c6786a09e3133a0c11
related_topics:
  - title: español version
    url: /es/common/nms.html
    icon: bi bi-globe
---
# nms

Command-line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers from stdin.
More information: <https://github.com/bartobri/no-more-secrets>.

- Decrypt text after a keystroke:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hello, World!</span>`" | nms`

- Decrypt output immediately, without waiting for a keystroke:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -la</span>` | nms -a`

- Decrypt the content of a file, with a custom output color:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` | nms -a -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue|white|yellow|black|magenta|green|red</span>

- Clear the screen before decrypting:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | nms -a -c`
