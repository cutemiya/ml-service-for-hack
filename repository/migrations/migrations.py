events = '''
create table if not exists event (
    id serial primary key,
    title text not null,
    description text not null,
    company_id int references public.CompanyDetails(id)
);
'''

user_tags = '''
create table if not exists usertag (
    id serial primary key,
    tag text not null,
    account_id int references account(id)
);
'''

user_events = '''
CREATE TABLE IF NOT EXISTS user_events (
    id serial primary key,
    event_id int references event(id),
    account_id int references account(id),
    place int default 0,
    status int default 0 -- 0 - идет, 1 - прошло
);
'''

