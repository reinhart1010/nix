---
layout: page
title: common/pm2 (English)
description: "Process manager for Node.js."
content_hash: 07f4baa179d33dd5cd81757f6d3465e6a04593b3
---
# pm2

Process manager for Node.js.
Used for log management, monitoring and configuring processes.
More information: <https://pm2.keymetrics.io>.

- Start a process with a name that can be used for later operations:

`pm2 start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- List processes:

`pm2 list`

- Monitor all processes:

`pm2 monit`

- Stop a process:

`pm2 stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Restart a process:

`pm2 restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Dump all processes for resurrecting them later:

`pm2 save`

- Resurrect previously dumped processes:

`pm2 resurrect`
