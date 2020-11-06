from project.caretaker import Caretaker
from project.keeper import Keeper
from project.vet import Vet
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            type_of_animal = type(animal).__name__
            return f"{animal.name} the {type_of_animal} added to the zoo"
        elif self.__animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            type_of_worker = type(worker).__name__
            return f'{worker.name} the {type_of_worker} hired successfully'
        else:
            return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker.__dict__['name']:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        else:
            return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_needs = sum([a.get_needs() for a in self.animals])
        if self.__budget >= total_needs:
            self.__budget -= total_needs
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        else:
            return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animal_count = len(self.animals)
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        NEW_LINE = '\n'

        return f'''You have {total_animal_count} animals
----- {len(lions)} Lions:
{NEW_LINE.join(map(str ,lions))}
----- {len(tigers)} Tigers:
{NEW_LINE.join(map(str, tigers))}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(map(str, cheetahs))}'''

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [w.__repr__() for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w.__repr__() for w in self.workers if isinstance(w, Caretaker)]
        vets = [w.__repr__() for w in self.workers if isinstance(w, Vet)]

        NEW_LINE = '\n'

        return f'''You have {total_workers_count} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(map(str, keepers))}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(map(str, caretakers))}
----- {len(vets)} Vets:
{NEW_LINE.join(map(str, vets))}'''
