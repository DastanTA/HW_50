from task_tracker.models import Task, Type, Status
from datetime import datetime, timedelta
from django.db.models import Q


# задача №1 - Закрытые задачи за последний месяц от текущей даты:
    # В days лучше указать более короткий срок. Иначе, так как, записи были сделаны недавно,
    # выводятся все что есть в базе.

date_count_start = datetime.now() - timedelta(days=30)
tasks1 = Task.objects.filter(status__status_name='выполнен').filter(updated_at__gt=date_count_start)
print(tasks1)




# задача №2 - Задачи, имеющие один из указанных статусов И один из указанных типов:

# Вариант 1
q_s_new = Q(status__status_name="новый")
q_s_ip = Q(status__status_name="в процессе")
q_t_b = Q(types__type_name="Баг")
q_t_z = Q(types__type_name="задача")
tasks2 = Task.objects.filter((q_s_new | q_s_ip) & (q_t_z | q_t_b))
print(tasks2)

# Вариант 2
q_1 = Q(status__status_name__in=["новый", "в процессе"])
q_2 = Q(types__type_name__in=("Баг", "задача"))
tasks2 = Task.objects.filter(q_1 & q_2).distinct()
print(tasks2)



# Задача 3 - Задачи, в названии которых содержится слово "bug" в любом регистре
    # или относящиеся к типу "Баг", имеющие НЕ закрытый статус
q_1 = Q(summary__icontains="bug")
q_2 = Q(types__type_name="Баг")
tasks3 = Task.objects.exclude(status__status_name="выполнен").filter(q_1 | q_2)
print(tasks3)
