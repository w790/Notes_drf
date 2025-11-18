# Notes Project

Простой проект для управления заметками с использованием Django REST Framework (бэкенд) и Vue.js (фронтенд). Этот проект создавался как учебное пособие для изучения синтаксиса и структуры DRF и Vue.

## Технологии

### Бэкенд
- **Python 3.11+**
- **Django 4.2+**
- **Django REST Framework**
- **PostgreSQL** (база данных)
- **CORS Headers** (для связи с фронтендом)

### Фронтенд
- **Vue 3** (первый опыт!)
- **Vite** (сборщик)
- **JavaScript ES6+**
- **Fetch API** (для HTTP запросов)

## Структура проекта

```
notes_project/
├── backend/                 # Django бэкенд
│   ├── apps/               # Приложения Django
│   │   └── notes/          # Приложение заметок
│   │       ├── models.py       # Модели данных
│   │       ├── serializers.py  # Сериализаторы DRF
│   │       ├── views.py        # API views
│   │       └── urls.py         # Маршруты API
│   ├── notes_project/      # Настройки Django
│   │   ├── settings.py     # Конфигурация
│   │   ├── urls.py         # Главные URL
│   │   └── wsgi.py
│   ├── .venv/              # Виртуальное окружение
│   ├── .env                # Переменные окружения
│   ├── manage.py
│   └── requirements.txt
├── frontend/               # Vue фронтенд
│   ├── src/
│   │   ├── components/     # Vue компоненты
│   │   ├── views/          # Страницы приложения
│   │   ├── services/       # API сервисы
│   │   ├── stores/         # Состояние приложения
│   │   ├── router/         # Маршрутизация
│   │   └── App.vue         # Главный компонент
│   └── package.json
└── README.md
```

## Установка и запуск

### Предварительные требования
- Python 3.11+
- Node.js 16+
- PostgreSQL

### 1. Бэкенд (Django)

```bash
# Активация виртуального окружения
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Настройка базы данных
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

Бэкенд будет доступен по адресу: `http://localhost:8000`

### 2. Фронтенд (Vue)

```bash
cd frontend

# Установка зависимостей
npm install

# Запуск dev сервера
npm run dev
```

Фронтенд будет доступен по адресу: `http://localhost:5173`

## API Endpoints

| Метод | URL | Описание |
|-------|-----|-----------|
| GET | `/api/v1/notes/` | Получить все заметки |
| POST | `/api/v1/notes/` | Создать новую заметку |
| GET | `/api/v1/notes/{id}/` | Получить заметку по ID |
| PUT | `/api/v1/notes/{id}/` | Обновить заметку |
| PATCH | `/api/v1/notes/{id}/` | Частично обновить заметку |
| DELETE | `/api/v1/notes/{id}/` | Удалить заметку |

## Архитектура бэкенда

### Views (Представления)

```python
# apps/notes/views.py
class NoteListCreateView(generics.ListCreateAPIView):
    """Представление для списка и создания заметок"""
    queryset = Note.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NoteCreateSerializer
        return NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для деталей, обновления и удаления заметок"""
    queryset = Note.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return NoteUpdateSerializer
        return NoteSerializer
```

### URL Маршруты

```python
# apps/notes/urls.py
urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]

# notes_project/urls.py (главный файл)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.notes.urls')),
]
```

## Особенности реализации

### Множественные сериализаторы
Проект использует разные сериализаторы для разных операций:
- **NoteSerializer** - для чтения данных
- **NoteCreateSerializer** - для создания заметок
- **NoteUpdateSerializer** - для обновления заметок

### Структура приложений
Приложения организованы в папке `apps/` для лучшей структуризации проекта.

### Связь фронтенда и бэкенда
Фронтенд общается с бэкендом через REST API. Основной сервис находится в `frontend/src/services/api.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Пример GET запроса
async getNotes() {
    return this.request('/notes/');
}

// Пример POST запроса  
async createNote(noteData) {
    return this.request('/notes/', {
        method: 'POST',
        body: JSON.stringify(noteData),
    });
}
```

## Цели проекта

- [x] Изучение синтаксиса Django REST Framework
- [x] Первое знакомство с Vue.js
- [x] Настройка связи между фронтендом и бэкендом
- [x] Работа с PostgreSQL через Django ORM
- [x] Реализация CRUD операций
- [x] Использование разных сериализаторов для разных операций
- [x] Организация приложений в папке apps/

## Развитие проекта

Потенциальные улучшения:
- [ ] Аутентификация пользователей
- [ ] Категории заметок
- [ ] Поиск и фильтрация
- [ ] Темная тема
- [ ] Мобильное приложение
- [ ] Тесты для API
- [ ] Документация API с Swagger

## Примечания для новичков в Vue

1. **Компоненты** - переиспользуемые блоки интерфейса
2. **Props** - данные, передаваемые от родителя к ребенку
3. **Emits** - события, отправляемые от ребенка к родителю
4. **Reactive data** - данные, которые автоматически обновляют интерфейс
5. **Lifecycle hooks** - методы, вызываемые в разные моменты жизни компонента

## Troubleshooting

### Проблемы с CORS
Если фронтенд не может подключиться к бэкенду, проверьте настройки CORS в Django.

### Проблемы с миграциями
При изменении моделей Django:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Проблемы с импортами
Убедитесь, что приложения в папке `apps/` правильно настроены в `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'apps.notes',
]
```

---
