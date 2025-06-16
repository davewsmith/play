#!/bin/bash

# Playing with an idea from https://crawshaw.io/blog/programming-with-agents

cat <<EOF | sqlite3 test.db
create table if not exists test (
    json jsonb  not null,
    id int      not null as (json->>'id') stored,
    key varchar          as (json->>'key'),
    value text           as (json->>'value')
);
EOF

json=$(jq -c . test.json)
# this keeps bash from eating the quotes
insert=$(echo -n "insert into test (json) values('"; echo -n $json ; echo "');")
echo $insert | sqlite3 test.db

sqlite3 test.db <<QUERIES
select _rowid_, id, json from test where id=1; -- stored fields
select "";
select _rowid_, id, json from test where key='42'; -- a non-stored field
QUERIES
