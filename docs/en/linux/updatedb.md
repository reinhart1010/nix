---
layout: page
title: linux/updatedb (English)
description: "Create or update the database used by `locate`."
content_hash: bc226495f348b518344613eb600c7a4ceb89f7bc
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# updatedb

Create or update the database used by `locate`.
It is usually run daily by cron.
More information: <https://manned.org/updatedb>.

- Refresh database content:

`sudo updatedb`

- Display file names as soon as they are found:

`sudo updatedb --verbose`
