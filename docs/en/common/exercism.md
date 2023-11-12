---
layout: page
title: common/exercism (English)
description: "Download and solve problems."
content_hash: 9a039f95b6756ac795ebd38bda821a0290c6ae0b
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# exercism

Download and solve problems.
More information: <https://exercism.org/docs/using/solving-exercises/working-locally>.

- Configure the application token and the preferred workspace for Exercism:

`exercism configure --token=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">your-application-token</span>` --workspace=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/preferred/workspace</span>

- Download a specific exercise:

`exercism download --exercise=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exercise_slug</span>` --track=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">track_slug</span>

- Submit an exercise:

`exercism submit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print the path to the solution workspace:

`exercism workspace`
