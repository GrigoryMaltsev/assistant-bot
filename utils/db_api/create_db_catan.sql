create table if not exists catan
(
    id_game     bigserial      primary key not null,
    date_game   timestamp                  not null,
    winner_game text                       not null
);

alter table catan
    owner to postgres;

create unique index if not exists game_id_uindex
    on catan (id_game);
