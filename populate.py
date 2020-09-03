import django

from django.conf import settings
from django.core.management import call_command

DATABASE_NAME = "database.db"

settings.configure(
    DEBUG=True,
    # Set the installed app
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'biotaxa',
    ),

    # Configure the database
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            'NAME': DATABASE_NAME,
        }

    }
)

# Required to use.
django.setup()

# Import all local models once Django has been setup

from biotaxa.models import Category


def add_to_db(fname):
    """
    Add contents of file to database
    """
    return



def test_queries():
    """
    Run simple queries to test performance of different tree representations.
    """
    return


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--makemigrations', action='store_true',
                        help='Used to create migration files when models are changed in app.')
    parser.add_argument('--migrate', action='store_true',
                        help='Apply migrations to database')

    parser.add_argument('--fname', type=str, help='Add the contents of file into database')

    parser.add_argument('--test', action='store_false',
                        help='Run a test query using all three tree representations, and print results.')

    args = parser.parse_args()

    makemig = args.makemigrations
    migrate = args.migrate

    fname = args.fname
    test = args.test

    # Make any migrations neccessary first.
    if makemig:
        call_command('makemigrations', 'biotaxa')

    # Apply any migrations that might have been made
    if migrate:
        call_command('migrate', 'biotaxa')

    # Add to database after migrations are done.
    if fname:
        add_to_db(fname=fname)

    # Test queries once database is populated.
    if test:
        test_queries()
