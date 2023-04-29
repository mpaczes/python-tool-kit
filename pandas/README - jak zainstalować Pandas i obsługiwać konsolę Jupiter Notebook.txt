
(1) Co trzeba zainstalować żeby używać pakietu Panda w Pythonie :

	pip install pandas

	
(2) Plik z przykładowymi danymi dla pakietu Panda :

	StackOverflow Survey Download Page - http://bit.ly/SO-Survey-Download
	
	Dane są w spakowanym pliku o nazwie 'stack-overflow-developer-survey-2019.zip'.
	
	Rozpakowałem ten plik do folderu i nazwałem go 'data'.
	
(3) Instalacja Jupter Notebook - pzreglądarkowa konsola do Pandy :

	pip install jupyterlab
	
	Jak używać konsoli Jupiter Notebook :
	
		jupyter notebook
		
	Tej komendy używamy tam gdzie jest katalog 'data'. 
	
	Uruchomi się serwer Jupyter i przeglądarka z adresem : http://localhost:8888/tree
	
	W przeglądarce kliknąć : 'New' -> 'Python 3' żeby utworzyć nowy 'Notebook' o nazwie 'Pandas demo'.
	
	W konsoli 'Jupter' wpisujemy : 'import pandas as pd' -> 'Run'.
	
	Od teraz możemy przetwarzać nasze dane, które są w formacie 'CSV'.

(4) Przetwarzanie przykładowych danych w formacie 'CSV' (używamy konsoli 'Jupyter') :

	df = pd.read_csv('data/survey_results_public.csv')		# data frame, czyli wiersze i kolumny
	
	df -> Run		# pokaże się tabela z danymi
	
	df.shape 		# zwróci (88883, 85), czyli liczbę wierszy i kolumn
	
	df.info()		# informacja o liczbie wierszy i kolumn, a także o typach danych: typy danych : int64, object (czyli string), float64
	
	pd.set_option('display.max_columns', 85)
	pd.set_option('display.max_rows', 85)
	
	schema_df = pd.read_csv('data/survey_results_schema.csv')
	
	schema_df		# kolumny i ich opisy

	df.head()		# wyświetla pięć pierwszych wierszy

	df.head(10)		# wyświetla dziesięć pierwszych wierszy
	
	df.tail()		# działa podobnie do 'head()' tylko od końca
	df.tail(10)
	
(5) Obsługa 'Data frame' w 'Pandas' :

	(5.1) Pandas i Python, czyli jak są przechowywane wiersze i kolumny 'Data frame' :
	
		tak to wygląda na przykładzie :
		
			# słownik Pythona
			people = {
				'first' : ['Jane', 'John'],
				'last' : ['Doe', 'Doe'],
				'email' : ['JaneDoe@email.com', 'JohnDoe@email.com']
			}
			
		czyli mamy słownik (dictionary) Pythona - klucze to kolumny, listy to wiersze

			people['email'] -> ['JaneDoe@email.com', 'JohnDoe@email.com']
	
		import pandas as pd
		df = pd.DataFrame(people)
		df		# zwróci tabelę z wierszami i kolumnami
		
		df['email']		# zwróci listę, czyli wiersze z kolumny 'email'
		type(df['email'])	# zwróci typ panda.code.series.Series
	
	(5.2) co to jest obiekt typu 'Series' :
	
		'Series' to są wiersze pojedynczej kolumny

		df[['last', 'email']]	# zwróci Data frame (tabelę) złożony z kolumn 'last' i 'email'
		
		df.columns	# lista kolumn Date frame
		
		df.iloc[0]		# zwróci pierwszy wiersz DF
		df.iloc[[0, 1]]		# zwróci pierwszy i drugi wiersz DF i wszystkie kolumny
		df.iloc[[0, 1], 2]	# jw tylko z trzecią kolumną
		
		df.loc[0]	# pierwszy wiersz
		df.loc[[0, 1]]	# DF z pierwszym i drugim wierszem
		df.loc[[0, 1], 'email']
		df.loc[[0, 1], ['email', 'last']]
		