-- Set up a scenario where delete the one side of a many-to-one
-- relationship should cascade deletes to the many side.

drop table if exists one;
create table one (
    id integer primary key,
    data char(128)
);

drop table if exists many;
create table many (
    id integer primary key,
    one_id integer references one(id) on delete cascade,
    data char(128)
);

insert into one (id, data) values (1, 'base');
insert into many (id, one_id, data) values(1, 1, 'first of many');
insert into many (id, one_id, data) values(2, 1, 'second of many');

select 'pragma foreign_keys';
pragma foreign_keys;

select 'many before delete of one', count(*) from many;
delete from one where id=1;
select 'many after delete of one', count(*) from many;
