create table if not exists cats
(
    user_name          text       primary key not null,
    last_date_cleaning timestamp,
    amount_cleaning    bigint
);

alter table cats
    owner to postgres;

INSERT INTO cats(user_name, last_date_cleaning, amount_cleaning) VALUES ('Гриша', NOW(), 282) ON CONFLICT DO NOTHING;

INSERT INTO cats(user_name, last_date_cleaning, amount_cleaning) VALUES ('Вика', NOW(), 278) ON CONFLICT DO NOTHING;
