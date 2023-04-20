'pip - An in-depth look at the package management system'

W tym pliku opisałem jak działa i co to jest komenda wiersza poleceń o nazwie 'pip'.

    pip help -> opisuje wszystkie komendy i opcje których można używać

    pip help install -> informacje szczegółowe o komendzie 'install'

    pip search Pympler -> informacje o pakiecie 'Pympler'

    pip install Pympler -> instaluje pakiet 'Pympler'

    pip list -> lista zainstalowanych pakietów

    pip unistall Pympler -> odinstalowuje pakiet 'Pympler'

    pip list --outdated -> pokazuje wersję bieżącą i ostatnią któa jest dostępna dla pakietów

    pip install -U setuptools -> aktualizacja pakietu do ostatniej wersji

    pip freeze -> lista zainstalowanych pakietów z wersjami w formacie 'requirements' czyli np. Pympler==0.4

    pip freeze > requirements.txt -> to co wyżej ale zapisane do pliku

    pip install -r <NAZWA PLIKU REQUIREMENTS> -> instaluje wszystkie pakiety z pliku tyou 'requirements', czyli np. pip install -r requirements.txt

    