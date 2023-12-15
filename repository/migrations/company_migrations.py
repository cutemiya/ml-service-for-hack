company = '''
create table if not exists company (
    id serial primary key,
    c_name text not null,
    c_description text,
    author_id int references accounts(id)
)
'''

events = '''
create table if not exists events (
    id serial primary key,
    e_name text not null,
    e_description text not null,
    e_author_id int references accounts(id)
);
'''

company_tags = '''
create table if not exists company_tags (
    id serial primary key,
    c_tag text not null,
    c_id int references comapny(id) 
)
'''