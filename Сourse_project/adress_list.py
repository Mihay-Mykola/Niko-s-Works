#Область
def DOblast(n):
 if n == 1:
    oblasti = ["Вінницька", "Волинська", "Дніпропетровська", "Донецька", "Житомирська", "Закарпатська",
            "Запорізька", "Івано-Франківська", "Київська", "Кіровоградська", "Луганська", "Львівська",
            "Миколаївська", "Одеська", "Полтавська", "Рівненська", "Сумська", "Тернопільська", "Харківська",
            "Херсонська", "Хмельницька", "Черкаська", "Чернівецька", "Чернігівська", "м. Київ",
            "Автономна Республіка Крим", "м. Севастополь"]
    
    while True:
        for i, oblast in enumerate(oblasti):
            print(f"{i+1} - {oblast}")
        
        try:
            num = int(input("Введіть номер області: "))
            if num < 1 or num > len(oblasti):
                print("Некоректний ввід. Введіть число від 1 до", len(oblasti))
                continue
            oblast = oblasti[num-1]
            return oblast
        except ValueError:
            print("Некоректний ввід. Введіть число від 1 до", len(oblasti))
            continue
 else:    
        oblasti = ["Вінницька", "Волинська", "Дніпропетровська", "Донецька", "Житомирська", "Закарпатська",
            "Запорізька", "Івано-Франківська", "Київська", "Кіровоградська", "Луганська", "Львівська",
            "Миколаївська", "Одеська", "Полтавська", "Рівненська", "Сумська", "Тернопільська", "Харківська",
            "Херсонська", "Хмельницька", "Черкаська", "Чернівецька", "Чернігівська", "м. Київ",
            "Автономна Республіка Крим", "м. Севастополь","Інша держава"]
        
        while True:
         for i, oblast in enumerate(oblasti):
            print(f"{i+1} - {oblast}")
        
         try:
            num = int(input("Введіть номер області: "))
            if num < 1 or num > len(oblasti):
                print("Некоректний ввід. Введіть число від 1 до", len(oblasti))
                continue
            oblast = oblasti[num-1]
            break
         except ValueError:
            print("Некоректний ввід. Введіть число від 1 до", len(oblasti))
            continue
        if oblast == "Інша держава":
              oblast = input("Введіть цю державу \n")
              return oblast
        else: return oblast               
#Район,адреса
def Daddress(oblast):

    if oblast == "Вінницька":
            rayoni = ["Вінницький", "Гайсинський", "Жмеринський","Могилів-Подільський","Тульчинський", "Хмільницький"]


    elif oblast == "Волинська":
            rayoni = ["Володимир-Волинський","Камінь-Каширський",  "Ковельський","Луцький"]


    elif oblast == "Дніпропетровська":
            rayoni = ["Дніпровський",  "Кам'янський", "Криворізький","Нікопольський", "Новомосковський","Павлоградський", "Синельниківський"]


    elif oblast == "Донецька":
            rayoni = ["Бахмутський", "Волноваський", "Горлівський", "Донецький", "Кальміуський","Краматорський", "Маріупольський", "Покровський"]


    elif oblast == "Житомирська":
            rayoni = ["Бердичівський", "Житомирський", "Коростенський", "Новоград-Волинський"]

    elif oblast == "Закарпатська":
            rayoni = ["Берегівський", "Мукачівський", "Рахівський", "Тячівський", "Ужгородський","Хустський"]


    elif oblast == "Запорізька":
            rayoni = ["Бердянський", "Василівський", "Запорізький",  "Мелітопольський","Пологівський"]


    elif oblast == "Івано-Франківська":
            rayoni = ["Верховинський","Івано-Франківський",  "Калуський", "Коломийський", "Косівський", "Надвірнянський"]


    elif oblast == "Київська":
            rayoni = [ "Білоцерківський", "Бориспільський", "Броварський", "Бучанський","Вишгородський", "Обухівський", "Фастівський",]


    elif oblast == "Кіровоградська":
            rayoni = ["Голованівський", "Кропивницький", "Новоукраїнський", "Олександрійський"]


    elif oblast == "Луганська":
            rayoni = ["Алчевський", "Довжанський", "Луганський", "Ровеньківський", "Сватівський","Сєвєродонецький", "Старобільський", "Щастинський"]


    elif oblast == "Львівська":
            rayoni = ["Дрогобицький", "Золочівський", "Львівський", "Самбірський", "Стрийський","Червоноградський","Яворівський"]

    elif oblast == "Миколаївська":
            rayoni = ["Баштанський", "Вознесенський", "Миколаївський", "Первомайський"]


    elif oblast == "Одеська":
            rayoni = ["Березівський", "Білгород-Дністровський", "Болградський", "Ізмаїльський", "Одеський район","Подільський","Роздільнянський"]


    elif oblast == "Полтавська":
            rayoni = ["Кременчуцький", "Лубенський", "Миргородський", "Полтавський"]


    elif oblast == "Рівненська":
            rayoni = ["Вараський", "Дубенський", "Рівненський", "Сарненський"]


    elif oblast == "Сумська":
            rayoni = ["Конотопський", "Охтирський", "Роменський", "Сумський район", "Шосткинський"]


    elif oblast == "Тернопільська":
            rayoni = ["Кременецький", "Тернопільський", "Чортківський"]


    elif oblast == "Харківська":
            rayoni = ["Богодухівський", "Ізюмський", "Красноградський", "Куп`янський", "Лозівський","Харківський","Чугуївський"]


    elif oblast == "Херсонська":
            rayoni = ["Бериславський", "Генічеський", "Каховський", "Скадовський", "Херсонський"]


    elif oblast == "Хмельницька":
            rayoni = ["Кам`янець-Подільський", "Хмельницький", "Шепетівський"]


    elif oblast == "Черкаська":
            rayoni = ["Звенигородський", "Золотоніський", "Уманський", "Черкаський"]


    elif oblast == "Чернівецька":
            rayoni = ["Вижницький", "Дністровський", "Чернівецький"]


    elif oblast == "Чернігівська":
            rayoni = ["Чернігівська", "Корюківський", "Ніжинський", "Новгород-Сіверський", "Прилуцький","Чернігівський"]


    elif oblast == "м. Київ":
            rayoni = ["Дарницький", "Деснянський", "Дніпровський", "Голосіївський", "Оболонський", "Печерський", "Подільський", "Шевченківський"]


    elif oblast == "Автономна Республіка Крим" :
            rayoni = ["Алуштинський", "Бахчисарайський", "Білогірський", "Джанкойський", "Євпаторійський", "Керченський",
                    "Кіровський", "Красногвардійський", "Ленінський", "Нижньогірський", "Первомайський", "Роздольненський",
                    "Сакський", "Сімферопольський", "Совєтський", "Чорноморський"]

    elif oblast == "м. Севастополь":
           rayoni = ["м. Севастополь"]

    while True:
        try:
                for i, rayon in enumerate(rayoni):
                    print(f"{i+1} - {rayon}")
                rayon = rayoni[int(input("Введіть номер району: ")) - 1]
                break
        except IndexError:
                print("Введений номер району некоректний. Спробуйте ще раз.")
        except ValueError:
                print("Введено некоректний номер. Спробуйте ще раз.")

    home_adress=input("Введіть адресу проживання (вул. Маяковського 28,кв 121 ; Баришівська громада, с. Лукаші,вул. Щастя 34)):\n")

    return  rayon ,home_adress

    