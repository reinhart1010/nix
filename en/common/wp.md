---
layout: page
title: common/wp (English)
description: "The official command-line interface to manage WordPress instances."
content_hash: 81c56c932825184173237bad8f040c7ba99be690
---
# wp

The official command-line interface to manage WordPress instances.
More information: <https://wp-cli.org/>.

- Print information about the operating system, shell, PHP, and WP-CLI (`wp`) installation:

`wp --info`

- Update WP-CLI:

`wp cli update`

- Download a fresh WordPress installation to current directory, optionally specifying the locale:

`wp core download --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locale</span>

- Create basic `wpconfig` file (assuming database on `localhost`):

`wp config create --dbname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dbname</span>` --dbuser=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dbuser</span>` --dbpass=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dbpass</span>

- Install and activate a WordPress plugin:

`wp plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plugin</span>` --activate`

- Replace all instances of a string in the database:

`wp search-replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_string</span>

- Import the contents of a WordPress Extended RSS (WXR) file:

`wp import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.xml</span>
