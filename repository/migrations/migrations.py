user_info = '''
create table if not exists user_info(
    Id serial primary key,
    first_name text not null,
    last_name text not null,
    partinomyc text not null,
    bd timestamp not null,
    city text not null,
    account_id int references accounts(id)
);'''

user_tags = '''
create table if not exists user_tags (
    id serial primary key,
    tag text not null,
    account_id int references accounts(id)
);
'''

user_events = '''
create table if not exists user_events (
    id serial primary key,
    tag text not null,
    account_id int references accounts(id)
);
'''