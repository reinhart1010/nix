---
layout: page
title: common/rails-db (한국어)
description: "Ruby on Rails의 다양한 데이터베이스 관련 하위 명령어."
content_hash: 08084d98d17b57ea5d34251d1c3a2f3f2bf2c99e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rails-db.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rails-db.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rails db

Ruby on Rails의 다양한 데이터베이스 관련 하위 명령어.
더 많은 정보: <https://guides.rubyonrails.org/active_record_migrations.html>.

- 데이터베이스 생성, 스키마 로드 및 시드 데이터로 초기화:

`rails db:setup`

- 데이터베이스 콘솔에 접근:

`rails db`

- 현재 환경에 정의된 데이터베이스 생성:

`rails db:create`

- 현재 환경에 정의된 데이터베이스 삭제:

`rails db:drop`

- 보류 중인 마이그레이션 실행:

`rails db:migrate`

- 각 마이그레이션 파일의 상태 보기:

`rails db:migrate:status`

- 마지막 마이그레이션 롤백:

`rails db:rollback`

- `db/seeds.rb`에 정의된 데이터로 현재 데이터베이스 채우기:

`rails db:seed`
