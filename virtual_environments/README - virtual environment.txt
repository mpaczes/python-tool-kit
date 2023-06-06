
(1) Dlaczego używa się 'virtual environments' :

	instalacja pakietów które są specyficzne dla określonego projektu;
	
	potrzebny jest Python w wersji 3.3 albo wyższej.

(2) Tworzenie nowego środowiska wirtualnego :

	cd C:\devel_python\virtual_environments
	
	co jest zainstalowane w systemie operacyjnym jeżeli chodzi o Python :
	
		pip list
		
	komendy :
	
		python -m venv <NAZWA_SRODOWISKA_WIRTULANEGO> czyli np. :
		
			python -m venv project_env
			
		dir - powinien utworzyć się katalog 'project_env'
		
		project_env\Scripts\activate.bat - aktywacja środowiska wirtualnego
		
		where python - pokaże scieżki do komendy 'python.exe'
		
	UWAGA : wersja Pythona użyta w środowisku wirtualnym będzie dokładnie taka jakiej użyliśmy do utworzenie tego środowiska

	komendy :
	
		pip list - przy aktywnym środowisku wirtualnym powinna pokazać tylko zainstalowane pip i setuptools

		załóżmy że nasz projekt wymaga bibliotek requests i pytz : 
		
			pip install requests
			pip install pytz
			
		pip list - powinno się pokazać wiecej pakietów

(3) Tworzenie pliku 'requirements.txt' :

	pip freeze - przy włączonym środowisku wirtualnym; powinna pokazać się lista zainstalowanych pakietów z wersjami; i z tego tworzymy plik 'requirements.txt'
	
	pip freeze --local - pakiety zainstalowane w tym środowisku
	
	komendy :
	
		deactivate - deaktywacja środowiska wirtualnego
		
		rmdir project_env /s - usuwanie środowiska wirtualnego, czyli usuwanie po prostu latalogu z dysku
		
(4) Jak się powinno postępować z projektem :

	mkdir my_project
	
	python -m venv my_project\venv
	
	my_project\ven\Scripts\activate.bat
	
	pip install -r requirements.txt
	
	pip list
	
	deactivate
	
	UWAGI :
	
		(1) zaleca się umieścić środowisko wirtualne wewnątrz projektu, ale nie powinno się umieszczać plików projektu wewnątrz środowiska wirtualnego
		
		(2) środowisko wirtualne powinno być czymś co można wyrzucić i zbudować od początku
		
		(3) nie powinno się wrzucać środowiska wirtualnego do repozytorium projektu
		
		(4) w repozytorium projektu powinien być plik 'requirements.txt' żeby ludzie mogli zbudować swoje własne środowisko
		
(5) Jak utworzyć środowisko wirtualne z dostępem do pakietów systemowych ('system packages') :

	pip list - w środowisku gdzie zainstalowany jest Python (czyli nie jest to środowisko wirtualne), czyli jest to globalna instalacja Pythona
	
	rmdir my_project\venv /s - usunięcie poprzedniego środowiska wirtualnego
	
	python -m venv my_project\venv --system-site-packages
	
	my_project\ven\Scripts\activate.bat
	
	pip list - powinna się pokazać lista zainstalowanych również pakietów systemowych w środowisku wirtualnym
	
	pip install SQLAlchemy - zainstalouje ten pakiet tylko w środowisku wirtualnym
	
	pip list
	
	pip list --local - lista pakietów zainstalowanych tylko w środowisku wirtualnym; powinno się pokazać tylko : pip, setuptools i SQLAlchemy
	
	