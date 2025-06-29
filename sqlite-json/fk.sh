#!/bin/bash
#
# A sanity check on enforcing 'on delete cascade'

rm -f fk.db

cat <<EOF | sqlite3 fk.db
pragma foreign_keys=on;

create table user (
    username varchar not null primary key
);

insert into user (username) values ('dave');

create table test (
    id integer primary key,
    username varchar references user (username) on delete cascade
);

create index test_username on test (username);


insert into test (username) values ('dave');

select "-- expect 1 user";
select count(*) from user;
select "-- expect 1 test";
select count(*) from test;

select "-- deleting user dave";
explain query plan delete from user where username = 'dave'; -- this should cascade

select "-- expect 0 user";
select count(*) from user;
select "-- expect 0 test";
select count(*) from test;
EOF
