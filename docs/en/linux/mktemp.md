---
layout: page
title: linux/mktemp (English)
description: "Create a temporary file or directory."
content_hash: cc133be5dad25f9fb46829e07a877a206f1e774a
last_modified_at: 2025-03-02
related_topics:
  - title: 한국어 version
    url: /ko/linux/mktemp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

Create a temporary file or directory.
More information: <https://www.gnu.org/software/coreutils/manual/html_node/mktemp-invocation.html>.

- Create an empty temporary file and print its absolute path:

`mktemp`

- Use a custom directory (defaults to `$TMPDIR`, or `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/tempdir</span>

- Use a custom path template (`X`s are replaced with random alphanumeric characters):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/example.XXXXXXXX</span>

- Use a custom file name template:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.XXXXXXXX</span>

- Create an empty temporary file with the given suffix and print its absolute path:

`mktemp --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.ext</span>

- Create an empty temporary directory and print its absolute path:

`mktemp --directory`
