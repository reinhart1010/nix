---
layout: page
title: common/exercism (English)
description: "Download and solve problems from the command-line."
content_hash: f4e42642bc6db7692ffa74eb61e0b494fcaded90
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># exercism

Download and solve problems from the command-line.
More information: <https://exercism.org/docs/using/solving-exercises/working-locally>.

- Configure the application token and the preferred workspace for Exercism:

`exercism configure --token=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your-application-token</span>` --workspace=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/preferred/workspace</span>

- Download a specific exercise:

`exercism download --exercise=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exercise_slug</span>` --track=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">track_slug</span>

- Submit an exercise:

`exercism submit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the path to the solution workspace:

`exercism workspace`
