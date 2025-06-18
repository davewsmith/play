#!/bin/bash

# Playing with an idea from https://crawshaw.io/blog/programming-with-agents

rm -f test.db

cat <<EOF | sqlite3 test.db
pragma foreign_keys=on;

create table user (
    username varchar not null primary key
);

insert into user (username) values ('dave');

create table if not exists test (
    json jsonb  not null,
    id int      not null as (json->>'id') stored,
    username varchar     as (json->>'username') stored references user (username) on delete cascade,
    value text           as (json->>'value')
);
EOF

json=$(jq -c . test.json)
# this keeps bash from eating the quotes
insert=$(echo -n "insert into test (json) values('"; echo -n $json ; echo "');")
echo $insert | sqlite3 test.db

sqlite3 test.db <<QUERIES
pragma foreign_keys=on;

select "-- expect 1 user named dave";
select count(*) from user where username = 'dave';

select "-- expect 1 test with a username of dave";
select count(*) from test where username = 'dave';

select "-- expect 1 join on username";
select 1 from user join test on user.username = test.username;

select "-- deleting user dave";
delete from user where username = 'dave'; -- this should cascade

select "-- expect 0 user";
select count(*) from user;

select "-- expect 0 test";
select count(*) from test;

QUERIES
