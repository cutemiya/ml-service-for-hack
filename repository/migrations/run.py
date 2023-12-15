from repository.migrations import migrations


def run(conn):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(migrations.user_info)
            cursor.execute(migrations.user_tags)
