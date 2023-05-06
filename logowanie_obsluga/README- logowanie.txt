
(1) moduł 'logging' jest wbudowany w Pythona, więc nie trzeba go dodawać;

(2) logging levels, czyli poziomy logowania :

	DEBUG, INFO, WARNING, ERROR, CRITICAL

	domyślny poziom logowania jest ustawiony na WARNING, czyli logowane jest wszystko co jest WARNING i powyżej, czyli ERROR i CRITICAL

(3) żeby zalogować DEBUG albo INFO trzeba ustawić to :

	logging.basicConfig(level=logging.DEBUG, filename='test.log', format='%(asctime)s:%(levelname)s:%(message)s')
	
	gdzie : filename to nazwa pliku do którego będą zapisane logi z uruchomionego skryptu

(4) formaty logowania można znaleźć na stronie : 

	'https://docs.python.org/3/library/logging.html#logrecord-attributes' :

	przykładowe formatowanie logowania :
	
		%(asctime)s
		%(levelname)s
		%(message)s
