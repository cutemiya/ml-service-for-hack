user_events = '''
CREATE TABLE IF NOT EXISTS user_events (
    id serial primary key,
    event_id int references event(id),
    account_id int references account(id),
    place int default 0,
    status int default 0 -- 0 - идет, 1 - прошло
);
'''

