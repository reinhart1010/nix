---
layout: page
title: common/entr (English)
description: "Run arbitrary commands when files change."
content_hash: 90ac4cd41dff4158ada8800353c420333866fae4
last_modified_at: 2024-03-01
related_topics:
  - title: italiano version
    url: /it/common/entr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/entr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# entr

Run arbitrary commands when files change.
More information: <http://eradman.com/entrproject/>.

- Rebuild with `make` if any file in any subdirectory changes:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ag -l</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">make</span>

- Rebuild and test with `make` if any `.c` source files in the current directory change:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.c</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make && make test'</span>

- Send a `SIGTERM` to any previously spawned ruby subprocesses before executing `ruby main.rb`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.rb</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby main.rb</span>

- Run a command with the changed file (`/_`) as an argument:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.sql</span>` | entr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`

- [c]lear the screen and run a query after the SQL script is updated:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo my.sql</span>` | entr -cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">psql -f</span>` /_`

- Rebuild the project if source files change, limiting output to the first few lines:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find src/</span>` | entr -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'make | sed 10q'</span>

- Launch and auto-[r]eload a Node.js server:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls *.js</span>` | entr -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node app.js</span>
