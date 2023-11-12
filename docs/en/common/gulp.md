---
layout: page
title: common/gulp (English)
description: "JavaScript task runner and streaming build system."
content_hash: 3e1b4c038239dece039614ce4d90ab07a9f5b95e
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/gulp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gulp

JavaScript task runner and streaming build system.
Tasks are defined within `gulpfile.js` at the project root.
More information: <https://github.com/gulpjs/gulp-cli>.

- Run the default task:

`gulp`

- Run individual tasks:

`gulp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">task</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">othertask</span>

- Print the task dependency tree for the loaded gulpfile:

`gulp --tasks`
