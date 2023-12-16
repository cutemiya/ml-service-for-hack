user_tags = '''
create table if not exists usertag (
    id serial primary key,
    tag text not null,
    account_id int references "Account"(id)
);
'''

user_events = '''
CREATE TABLE IF NOT EXISTS user_events (
    id serial primary key,
    event_id int references "Event"(id),
    account_id int references "Account"(id),
    place int default 0,
    status int default 0 -- 0 - идет, 1 - прошло
);
'''

