# вариант задания "5", группа 78-23

# Задания

Разработать инструмент командной строки для учебного конфигурационного 
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из 
входного формата в выходной. Синтаксические ошибки выявляются с выдачей 
сообщений. 
Входной текст на языке yaml принимается из стандартного ввода. Выходной 
текст на учебном конфигурационном языке попадает в файл, путь к которому 
задан ключом командной строки. 
Однострочные комментарии: 
// Это однострочный комментарий 
Словари: 
{ 
} 
имя -> значение. 
имя -> значение. 
имя -> значение. 
... 
Имена: 
[_a-zA-Z][_a-zA-Z0-9]* 
Значения: 
• Числа. 
• Строки. 
• Словари. 
Строки: 
'Это строка' 
Объявление константы на этапе трансляции: 
25 
const имя = значение 
Вычисление константы на этапе трансляции: 
@(имя) 
Результатом вычисления константного выражения является значение. 
Все конструкции учебного конфигурационного языка (с учетом их 
возможной вложенности) должны быть покрыты тестами. Необходимо показать 3 
примера описания конфигураций из разных предметных областей.


## описание
- файл main.py содкржит переводчик с языка yaml на выдуманный язык
- файл test.py провераяет правильность выполнения всех функций, написанных в main.py
- файл config.yaml содержит пример конфигурации для перевода
- файл config2.yaml содержит пример конфигурации для перевода
- файл config3.yaml содержит пример конфигурации для перевода
- файл output.txt является результатом работы программы над config.yaml 
- файл output2.txt является результатом работы программы над config3.yaml 
- файл output3.txt является результатом работы программы над config2.yaml 

## Примеры
1. Входной файл на языке yaml:
```yaml
# Конфигурация приложения
app:
  name: 'App'
  version: 1.0
  features:
    logging: true
    monitoring: false
    max_users: 100
  constants:
    const_max_connections: 10
    const_timeout: 30
    const_name: 'confup_constant'  
  database:
    host: 'db.confup.com'
    port: 5432
    user: 'admin'
    password: 'secret'
    name: 'my_database'
  api:
    endpoint: 'v1'
    methods:
      GET: 'fetchData'
      POST: 'sendData'
  settings:
    timeout: '@(const_timeout)' 
    max_connections: '@(const_max_connections)'  
  messages:
    welcome: 'Добро пожаловат!'
    goodbye: 'До свидания!'
    error: 'Произошла ошибка!'
  description: 'Это описание.'
```
Выходной файл на учебном конфигурационном языке:
```
app -> {
  name -> 'App'
  version -> 1.0
  features -> {
    logging -> True
    monitoring -> False
    max_users -> 100
  }
  constants -> {
    const_max_connections -> 10
    const_timeout -> 30
    const_name -> 'confup_constant'
  }
  database -> {
    host -> 'db.confup.com'
    port -> 5432
    user -> 'admin'
    password -> 'secret'
    name -> 'my_database'
  }
  api -> {
    endpoint -> 'v1'
    methods -> {
      GET -> 'fetchData'
      POST -> 'sendData'
    }
  }
  settings -> {
    timeout -> '30'
    max_connections -> '10'
  }
  messages -> {
    welcome -> 'Добро пожаловат!'
    goodbye -> 'До свидания!'
    error -> 'Произошла ошибка!'
  }
  description -> 'Это описание.'
}
```

2. Входной файл на языке yaml:
```yaml
# Конфигурация приложения
app:
project:
  name: "Разработка веб-приложения"
  deadline: "2024-12-31"
  team:
    Разработчик:
      Иван Иванов:
        experience: 12
      Анна Петрова:
        experience: 3
    Дизайнер:
      Светлана Сидорова:
        experience: 4
  tasks:
    Создание макета:
      assigned_to: "Светлана Сидорова"
      status: "В процессе"
    Разработка бэкенда:
      assigned_to: "Иван Иванов"
      status: "Не начато"
    Тестирование:
      assigned_to: "Анна Петрова"
      status: "Не начато"
```
Выходной файл на учебном конфигурационном языке:
```
project -> {
  name -> 'Разработка веб-приложения'
  deadline -> '2024-12-31'
  team -> {
    Разработчик -> {
      Иван Иванов -> {
        experience -> 12
      }
      Анна Петрова -> {
        experience -> 3
      }
    }
    Дизайнер -> {
      Светлана Сидорова -> {
        experience -> 4
      }
    }
  }
  tasks -> {
    Создание макета -> {
      assigned_to -> 'Светлана Сидорова'
      status -> 'В процессе'
    }
    Разработка бэкенда -> {
      assigned_to -> 'Иван Иванов'
      status -> 'Не начато'
    }
    Тестирование -> {
      assigned_to -> 'Анна Петрова'
      status -> 'Не начато'
    }
  }
}
```

3. Входной файл на языке yaml:
```yaml
# Конфигурация приложения
environment:
  title: 'Ocean'
  version: 2.0
  features:
    tracking_enabled: true
    weather_updates: true
    passenger_limit: 303
  settings:
    max_boats: 20
    delay_time: 60
    unique_identifier: 'ocean_id'  
  storage:
    server_info:
      address: 'db.oceanvoyager.com'
      port: 5432
    access:
      user: 'marina'
      pass: 'securepass'
    database_name: 'ocean'
  api_info:
    api_version: 'v2.0'
    routes:
      get_data: 'fetchData'
      post_data: 'sendData'
  preferences:
    timeout_setting: '@(delay_time)' 
    connection_limit: '@(max_boats)'  
  alerts:
    welcome_message: 'welcome'
    farewell_message: 'THX!!!'
    error_notification: 'ERR!!!'
  description: 'ZXC'
```
Выходной файл на учебном конфигурационном языке:
```
environment -> {
  title -> 'Ocean'
  version -> 2.0
  features -> {
    tracking_enabled -> True
    weather_updates -> True
    passenger_limit -> 303
  }
  settings -> {
    max_boats -> 20
    delay_time -> 60
    unique_identifier -> 'ocean_id'
  }
  storage -> {
    server_info -> {
      address -> 'db.oceanvoyager.com'
      port -> 5432
    }
    access -> {
      user -> 'marina'
      pass -> 'securepass'
    }
    database_name -> 'ocean'
  }
  api_info -> {
    api_version -> 'v2.0'
    routes -> {
      get_data -> 'fetchData'
      post_data -> 'sendData'
    }
  }
  preferences -> {
    timeout_setting -> '@(delay_time)'
    connection_limit -> '@(max_boats)'
  }
  alerts -> {
    welcome_message -> 'welcome'
    farewell_message -> 'THX!!!'
    error_notification -> 'ERR!!!'
  }
  description -> 'ZXC'
}
```


## Тестирование
### при запуске "py -m unittest test.py" теста test.py мы видим в выводе:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```

при заупске "python main.py" с выбранным конф. файлом config.yaml  в файле output.txt мы видим успешно переведённый файл 

для запуска необходимо сначала написать приставку py затем исполняемвый файл main.py затем конф. файл config.yaml затем выходной файл (куда запишется рещультат) output.txt
пример #py main.py config.yaml output.txt

