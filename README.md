# PythonTest


Для запуска решения необходимо загрузить файлы .py в одну директорию и первым делом запустить генератор тестов(TestCreator.py). После запуска в текущей директории будут созданы 20 директорий с тестами(test0, test1, ... , test19). Делее просто запускается файл source.py. После каждого запуска TestCreator.py тесты пересоздаются!!

Есть возможность запуска программы с некоторыми флагами: TestCreator.py -lt or --lowtests - генерация маленьких тестов

source.py -a or --answer - Чистый вывод числа верхней директории. При запуске программы без данных флагов для каждого теста буду выведены путь каждой поддиректории и ее число
Ответы на тесты могут быть очень большими числами!

Примеры работы программы (на одном тесте!):
koko@koko-HP-Notebook:~/PythonTest/Files$ python TestCreator.py -lt
koko@koko-HP-Notebook:~/PythonTest/Files$ python source.py -a
2220460334504927150980055419
koko@koko-HP-Notebook:~/PythonTest/Files$ python source.py
test01 --->
/home/koko/PythonTest/Files/test01/add/add/add/add/add ----> 14
/home/koko/PythonTest/Files/test01/add/add/add/add ----> 52
/home/koko/PythonTest/Files/test01/add/add/add/mul ----> 430160855040
/home/koko/PythonTest/Files/test01/add/add/add ----> 430160855189
/home/koko/PythonTest/Files/test01/add/add ----> 430160855342
/home/koko/PythonTest/Files/test01/add/mul/mul/add ----> 90
/home/koko/PythonTest/Files/test01/add/mul/mul ----> 9559130112000
/home/koko/PythonTest/Files/test01/add/mul ----> 2220460334504926720819200000
/home/koko/PythonTest/Files/test01/add ----> 2220460334504927150980055419
2220460334504927150980055419



koko@koko-HP-Notebook:~/PythonTest/Files$ python TestCreator.py --lowtests
koko@koko-HP-Notebook:~/PythonTest/Files$ python source.py --answer
8091103227903598131318620160000000
koko@koko-HP-Notebook:~/PythonTest/Files$ python source.py
test01 --->
/home/koko/PythonTest/Files/test01/mul/add ----> 57
/home/koko/PythonTest/Files/test01/mul/mul ----> 83528953469337600000
/home/koko/PythonTest/Files/test01/mul ----> 8091103227903598131318620160000000
8091103227903598131318620160000000



koko@koko-HP-Notebook:~/PythonTest/Files$ python TestCreator.py
koko@koko-HP-Notebook:~/PythonTest/Files$ python source.py -a
43199869513002396978202162553646794606250878240772258028172185393081885601677801982838822967743901350599307126722527171275678854086656000000000000
koko@koko-HP-Notebook:~/PythonTest/Files$ python source.py
test01 --->
/home/koko/PythonTest/Files/test01/mul/add/add ----> 204
/home/koko/PythonTest/Files/test01/mul/add/mul/add ----> 715
/home/koko/PythonTest/Files/test01/mul/add/mul/mul/mul/add ----> 896
/home/koko/PythonTest/Files/test01/mul/add/mul/mul/mul/mul ----> 974014833511965877632000
/home/koko/PythonTest/Files/test01/mul/add/mul/mul/mul ----> 19424702640266225306227898002847623477936447268742758400000000000000
/home/koko/PythonTest/Files/test01/mul/add/mul/mul ----> 992058413243676658839671206801433826265170234909230157004800000000000000
/home/koko/PythonTest/Files/test01/mul/add/mul ----> 122538181546867143470071213994216531318318005435725721115009680130221451837572707778560000000000000000000
/home/koko/PythonTest/Files/test01/mul/add ----> 122538181546867143470071213994216531318318005435725721115009680130221451837572707778560000000000000000523
/home/koko/PythonTest/Files/test01/mul ----> 43199869513002396978202162553646794606250878240772258028172185393081885601677801982838822967743901350599307126722527171275678854086656000000000000
43199869513002396978202162553646794606250878240772258028172185393081885601677801982838822967743901350599307126722527171275678854086656000000000000


 
