# Нейросети. Почему это кажется сложным и даже невозможным

## Вступление

Для того, чтобы погрузиться в тему моего доклада, заглянем в не такое далёкое прошлое и посмотрим на то, какие фантастические сценарии появлялись на больших экранах: Матрица, Терминатор, Робокоп, Метрополис, Трон и многие другие. В те времена казалось, что хоть какая-то мало-мальски похожая на человека программа представляет невероятную угрозу и вообще мы все вымрем.

Let’s go back to 2023. Не знаю как вы, но я каждое утро занимаюсь самым интересным занятием - открываю ленту телеграма и пытаюсь угадать, какие из подобных май-файных сценариев удалось приблизить благодаря развитию современных языковых моделей по типу GPT.

К чему это всё? Я не стою в шапочке из фольги и доставать её не планирую, по сему можно сделать вывод, что я не буду вас сподвигать строить храм имени языковых моделей, чтобы нас не убили. Скорее, мысль этого вступления в том, что абсолютно фантастические технологии из прошлого приходят к нам и становятся обыденностью, а нам, в свою очередь, необходимо адаптироваться к изменениям и изучать новые инструменты для работы.

Поэтому предлагаю залезть в страшные пучины кода на Python и разобрать то, как работают те самые “человекозаменители” изнутри.

## Немного теории

Все задачи, которые в простонародье принято относить к искуственному интелекту можно представить в виде вот таких луковиц. Как видите, их здесь две: одна относится к математике и статистике, а вторая отвечает за всё то, что приближает закат человечества. Если конкретнее, то это Artificial Intelligence, Machine Learning и Deep Learning, а серединкой в этих сросшихся луковицах является Data Science. Мы будем постепенно погружаться в левую часть розовой луковички, хотя и без обращений в левую не обойдётся. Это небольшое отступление насчёт роадмапа доклада. Теперь к более конкретным терминам.

> ML - класс методов искусственного интеллекта, характерной чертой которых является не прямое решение задачи, а обучение за счёт применения решений множества сходных задач.
> 

То есть вместо прописывания конкретного алгоритма в математической модели, мы обучаем эту математическую модель большими объёмами данных делать выводы из исходных данных и предсказывать верный результат. На основе данного утверждения можно понять, что такое нейросеть:

> Нейросеть — это тип машинного обучения, при котором компьютерная программа имитирует работу человеческого мозга. Подобно тому, как нейроны в мозге передают сигналы друг другу, в нейросети информацией обмениваются вычислительные элементы.
> 

Здесь, если честно, всё тоже выглядит вполне ясно. Мы создаём математическую модель, которая имитирует работу нашего мозга. И, забегая вперёд, называется она нейронной не только из-за попыток повторить наше мышление, а из-за вполне схожей структуры. Но вот вместо передачи электрических сигналов, нейронная сеть оперирует математическими конструкциями.

На словах всё выглядит нетяжело и красиво, но теперь копнём ещё дальше. Так выглядит структура простенькой нейронной сети (изображение). Это вполне конкретный кейс нейронной сети с несколькими входами и одним выходом, но количество комбинаций входов и выходов может быть каким угодно.

Что здесь нарисовано? Всё также просто, как и объяснялось ранее. Первые две точки (называемые нейронами) отвечают за “поимку” входных данных. Далее, переходя по различным рёбрам от нейрона к нейрону, модель домножает исходные данные на определённые веса, что в итоге , приходя к последнему нейрону, позволяет сделать определённое предсказание, на которое эта нейросеть и заточена.

Веса, как раз, выбираются на основе проведения обучения нейросети. Обучение бывает нескольких видов, самые основные из которых обучение с учителем, без учителя и с подкреплением. Обучение с учителем предполагает “скармливание” модели уже готовых результатов, на основе которых модель должна сделать выводы и начать делать предсказания самостоятельно. Нейросеть без учителя сначала сама проходит по данным для обучения, после чего смотрит на действительный ответ и таким образом постепенно корректирует своё поведение. Ну а обучение с подкреплением предполагает объединение двух других методов обучения, т. е. кормим сеть как размеченными, так и неразмеченными данными.

Мы рассмотрим примеры обучения без учителя, чтобы немножко потренировать голову и более чётко понять то, как машина “думает”.

## Трогаем ручками

Как принято в программировании, любая практика намного лучше тонны теории, потому перейдём к созданию нейросети и её обучению. Для начала, предлагаю вам посмотреть на следующий пример (показать код алгоритмов рекомендаций твиттера).

Неужели ничего не понятно? Вау. А для кого я тут распинался миллион минут? Ладно, это всё мои авторские юморески. Я сам этот код с трудом понимаю, а это, между прочим, кусочек из алгоритмов рекомендации твиттера (спасибо Илону Маску за открытый доступ к репочке). Естественно понятно, что для создания таких моделей необходимо обладать большими познаниями в математике и работе с данными. Да и скиллы программиста тут нужны явно не маленькие. Для того, чтобы показать вам, что нейросети это не страшно, я возьму пример из книги Эндрю Траска “Грокаем глубокое обучение” (кто внимательно следил, знает, что глубокое обучение это самая дальняя часть левой луковички, которую я показывал в начале).

В данном примере мы попробуем предсказать вероятность победы бейсбольной команды на основе данных о том, что с этой командой происходило в последнее время (познаний в бейсболе не требуется, тут всё будет элементарно).

Для нашей нейронной сети мы будем подавать 3 вида данных на вход: среднее число сыгранных игр командой (`number_of_toes`), средний винрейт команды (`wlrec`) и количество фанатов команды в миллионах человек (`nfans`). Возьмем сразу несколько подобных данных и заключим в массивы. 

```python
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [.65, .8, .8, .9]
nfans = [1.2, 1.3, .5, 1.0]
```

Теперь зададим начальные веса нашей нейронной сети. Они взяты плюс-минус наугад, потому что далее мы будем её обучать на основе наших данных. В массиве веса для наших трёх наборов данных соответственно.

```python
weights = [.1, .2, -1]
```

В своём коде я избегу использования сторонних опенсурсных библиотек типа numpy, поэтому для некоторых вычислений нам будет необходимо написать пару методов, реализующих некоторые операции. 

Для начала рассмотрим функцию `ele_mul` (elements multiplication)

```python
def ele_mul(number, vector):
	output = []
	for i in range(len(vector)):
	    output.append(number * vector[i])
	
	return output
```

Данный метод принимает на вход массив и вектор и последовательно перемножает каждый элемент на это число. В данный момент он нам будет не нужен, но пригодится в момент обучения и мы к нему вернёмся.

Функция `w_sum` будет вычислять скалярное произведение векторов. Т. е. складывать произведение соответствующих элементов векторов.

```python
def w_sum(a, b):
	assert(len(a) == len(b))
	output = 0
	for i in range(len(a)):
	output += a[i] * b[i]
	return output
```

Теперь, зная о функциях этих методов, мы можем написать нейросеть. Не поверите, но вот так она будет выглядеть:

```python
def neural_network(_input, weights):
	pred = w_sum(_input, weights)
	return pred
```

Мы вполне можем запустить нейросеть в подобном виде и посмотреть на результат для всего нашего набора данных и посмотреть, что он выдаст. Дабы не напрягаться насчёт вычислений, я вынес их в табличку:

| toes | wlrec | nfans | result |
| --- | --- | --- | --- |
| 8.5 | 0.65 | 1.2 | -0.21999999999999986 |
| 9.5 | 0.8 | 1.3 | -0.18999999999999995 |
| 9.9 |  0.8 | 0.5 | 0.6500000000000001 |
| 9.0 | 0.9 |  1.0 | 0.08000000000000007 |

Как вы видите, у нас команда физически не может выиграть с подобными весами (хотя в третьем примере вполне справляется, в других уходит в минус).

Теперь необходимо ещё немного погрузить вас в теорию. Для того, чтобы понять, что такое обучение, необходимо также понимать, какой результат для нас будет подходящим, т. е. какой результат необходмо достигнуть в результате обучения. 

На самом деле, для данного набора данных, у меня есть готовые результаты, которые были проверены экспериментальным путём. Вот собственно и они:

```python
win_or_lose_binary = [1, 1, 0, 1]
```

Зная необходимый результат, мы можем рассчитать величину ошибки. Их на самом деле две: среднеквадратичная и чистая. Как найти вторую всё ясно - из необходимого результата вычитаем фактический, а среднеквадратичная ошибка просто возводит чистую в квадрат. Необходимо это для формализации ошибки. Т. е. среднеквадратичная показывает только количественную величину ошибки, а чистая указывает ешё и на её направление. 

```python
delta = pred - true
error = delta ** 2
```

![Untitled](images/Untitled.png)

Для чего нам вообще нужно оценивать величину ошибки? Вопрос глупый, но всё же ответим на него, потому что для темы обучения он фундаментальный. Зависимость изменения ошибки от веса на графике можно отобразить с помощью параболы: 

То есть, с изменением веса ошибка будет уменьшаться до точки экстремума, но дальше снова будет расти. И в процессе обучения мы как раз должны будем найти эту точку, в которой и будет наиболее точный результат. 

Процесс, при котором мы будем перемещаться к этой точке будет называться градиентным спуском. Мы будем изменять веса на величину, равную произведению ошибки на входные данные. А также будем использовать ещё одну величину - альфа коэффициент. Он необходим для того, чтобы контролировать то, как мы будем двигаться по этому графику, и предотвращать преждевременный переход за точку экстремума. 

Теперь перенесём всё сказанное в код и рассмотрим конкретнее. Ко всему, что было в нашей модели ранее мы добавим следующий код:

```python
for i in range(len(wlrec)):
	print(f'-----{i+1}------')
	true = win_or_lose_binary[i]
	_input = [toes[i], wlrec[i], nfans[i]]
	
	pred = neural_network(_input, weights)
	delta = pred - true
	error = delta ** 2
	
	print(f'Prediction: {pred}\\nError: {error}\\n')
	
	weight_deltas = ele_mul(delta, _input)
	
	alpha = 0.01
	
	for j in range(len(weights)):
	    weights[j] -= alpha * weight_deltas[j]
	
	print(f'Weights: {str(weights)}\\nWeight deltas: {str(weight_deltas)}\\n')
	
	pred = neural_network(_input, weights)
	print(f'New prediction: {pred}\\nError: {error}\\n')
```

Этот цикл for будет пробегать по всем нашим входным данным и изменять веса градиентным спуском.  Т. е. мы возьмём правильный ответ для конкретной итерации, возьмём исходные данные в отдельный массив и вычислим ответ для таких весов (эти ответы мы получили ранее в таблице), после чего вычислим среднеквадратичную и чистую ошибку и выведем предикт и его ошибку в консоль для наглядности. После чего перейдём к обучению. Найдём разницу в весах, произведя поэлементное умножение вектора входных данных на величину ошибки и запишем в переменную альфа-коэффициент. теперь пробежимся по изменённым весам и домножим на тот самый коэффициент, чтобы отрегулировать изменение весов (альфа-коэффициент выбирался интуитивно, но в итоге приведёт нас к нужному результату, только дождитесь). Далее просто для наглядности выведем обновлённые веса, после чего дадим “виртуальному мозгу” вынести свой вердикт и показать величину ошибки. Вот и всё обучение!

Не терпится посмотреть на результат? Тогда давайте и посмотрим:

```python
----1------
Prediction: -0.21999999999999986
Error: 1.4883999999999995
Weights: [0.2037, 0.20793, -0.98536]
Weight deltas: [-10.369999999999997, -0.7929999999999998, -1.4639999999999997]
New prediction: 0.6841725000000001
Error: 1.4883999999999995
```

```python
----2------
Prediction: 0.8205259999999996
Error: 0.03221091667600013
Weights: [0.22075003000000004, 0.209365792, -0.983026838]
Weight deltas: [-1.7050030000000034, -0.1435792000000003, -0.23331620000000047]
New prediction: 0.9866830292000008
Error: 0.03221091667600013
```

```python
----3------
Prediction: 1.8614045116000004
Error: 3.464826755804836
Weights: [0.03647098335160001, 0.1944745559072, -0.992333860558]
Weight deltas: [18.427904664840003, 1.4891236092800004, 0.9307022558000002]
New prediction: 0.02047544962760023
Error: 3.464826755804836
```

```python
----4------
Prediction: -0.4890679100771199
Error: 2.2173232408214414
Weights: [0.1704870952585408, 0.20787616709789408, -0.9774431814572287]
Weight deltas: [-13.401611190694078, -1.3401611190694078, -1.4890679100771198]
New prediction: 0.7440292262577431
Error: 2.2173232408214414
```

Тут довольно много занимательного трейсбека, но самое главное - сравнить экспериментальные данные с тем, что предсказала нейросеть!

| Experimental | Neural prediction |
| --- | --- |
| 1 | 0.68 |
| 1 | 0.98 |
| 0 | 0.02 |
| 1 | 0.74 |

Можно увидеть, что нейросеть скорректировала веса и смогла выдать вполне подходящие предсказания, причём скормив сети достаточное количество данных, мы сможем найти те веса, которые в любой типовой ситуации сможет предсказать, выиграет эта команда или нет, ведь при большом наборе данных, получится выявить более точную закономерность.

## Вот и всё!

На небольшом блоке теории и примере я хотел показать, что нейросети - это невероятно полезный инструмент, а что ещё более важно, - это интересная область знаний, разбираться в которой невероятно увлекательно. Понимаю, что на первый взгляд всё то, что я показал выглядит страшно и не понятно, но стоит потратить на изучение всего два часа в день на протяжение недели и всё это будет абсолютно понятно.

Для тех, кого заинтересовал, рекомендую ознакомиться с книгой, из которой был взят этот пример, мной решённый. Написано всё простым языком и не требует особых познаний ни в программировании, ни в математике.
