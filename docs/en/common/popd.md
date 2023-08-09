---
layout: page
title: common/popd (English)
description: "Remove a directory placed on the directory stack via the pushd shell built-in."
content_hash: 676c07791b39ef733de26548d2d941ef4f8fbb3d
last_modified_at: 2023-08-09
related_topics:
  - title: dansk version
    url: /da/common/popd.html
    icon: bi bi-globe
---
# popd

Remove a directory placed on the directory stack via the pushd shell built-in.
See also `pushd` to place a directory on the stack and `dirs` to display directory stack contents.
More information: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Remove the top directory from the stack and cd to it:

`popd`

- Remove the Nth directory (starting from zero to the left from the list printed with `dirs`):

`popd +N`

- Remove the Nth directory (starting from zero to the right from the list printed with `dirs`):

`popd -N`

- Remove the 1st directory (starting from zero to the left from the list printed with `dirs`):

`popd -n`
