create table if not exists users
(
    id_user     bigserial  primary key not null,
    adding_date timestamp              not null,
    user_info   text                   not null
);

alter table users
    owner to postgres;

create unique index if not exists user_id_uindex
    on users (id_user);
