---
layout: page
title: common/git-count-objects (English)
description: "Count the number of unpacked objects and their disk consumption."
content_hash: 9b77716c15e93737464c9620290829330dcd0ceb
last_modified_at: 2023-11-12
related_topics:
  - title: Türkçe version
    url: /tr/common/git-count-objects.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git count-objects

Count the number of unpacked objects and their disk consumption.
More information: <https://git-scm.com/docs/git-count-objects>.

- Count all objects and display the total disk usage:

`git count-objects`

- Display a count of all objects and their total disk usage, displaying sizes in human-readable units:

`git count-objects --human-readable`

- Display more verbose information:

`git count-objects --verbose`

- Display more verbose information, displaying sizes in human-readable units:

`git count-objects --human-readable --verbose`
