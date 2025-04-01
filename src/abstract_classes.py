
from abc import ABC, abstractmethod


class ParsingData(ABC):
    """ абстракный класс для класса HeadHunterAPI """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @abstractmethod
    def parsing_data(self):
        pass


class ABCWorkWithFile(ABC):
    """ абстрактный класс для класса WorkWithFile"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_to_file(self, vacancies):
        pass

    @abstractmethod
    def read_data_json(self):
        pass

    @abstractmethod
    def return_vacancies(self):
        pass
