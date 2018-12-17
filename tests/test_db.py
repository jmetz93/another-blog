import sqlite3

import pytest
from app.db import get_db

'''The get_db function should return the same connection everytime and close the connection after it is done'''
def test_get_close_db(app):
	with app.app_context():
		db = get_db()
		assert db is get_db()

	with pytest.raises(sqlite3.ProgrammingError) as e:
		db.execute('SELECT 1')
	
	assert 'closed' in str(e)


'''The init-db command should call the init_db function and output a message.'''
def test_init_db_command(runner, monkeypatch):
	class Recorder(object):
		called = False

	def fake_init_db():
		Recorder.called = True

	'''Don't want to actually call the function, just record that it was called'''
	monkeypatch.setattr('app.db.init_db', fake_init_db)
	result = runner.invoke(args=['init-db'])
	assert 'Initialized' in result.output
	assert Recorder.called