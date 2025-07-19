from rich.panel import Panel
from rich.console import Console

class Car():
    def __init__(self, marka, model, price, type = "Car"):
        self.__marka = marka
        self.__model = model
        self.__price = price
        self.__type = type
        self.__console = Console()
    
    @property
    def marka(self):
            return self.__marka
    
    @property
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price

    def check_price_car(self):
        price = self.__price
        if price < 100000:
            self.__type = "Уровень машины - Таз"
        
        elif 100000 <= price <= 1000000:
            self.__type = "Уровень машины - Бюджетный"
    
        elif 1000000 < price <= 3000000:
            self.__type = "Уровень машины - Лада"
    
        elif 3000000 < price <= 5000000:
            self.__type = "Средний класс"
    
        elif 5000000 < price <= 10000000:
            self.__type = "Уровень машины - Хороший"
    
        elif 10000000 < price <= 20000000:
            self.__type = "Уровень машины - Отличная"
    
        elif self.__price > 20000000:  
            self.__type = "Уровень машины - Элита"
    
        else:
            self.__type = "Неизвестный уровень"
            
        self.__console.print(Panel.fit(
        f"[bold green]{self.__type}[/]",
        title="[bold blue]Тип[/][bold]💲[/]",
        border_style="bright_magenta"
		))

    def print_car_info(self):
        self.__console.print(Panel.fit(
            f"[bold purple]Марка: {self.__marka}[/]\n[bold cyan]Модел: {self.__model}[/]\n[bold magenta]Цена: {self.price}[/]",
            title="[bold blue]Car info🚗",
            border_style="bright_magenta"
		))
        
    def print_car_marka(self):
        self.__console.print(Panel.fit(
        f"[bold purple]ထထ Марка авто: {self.__marka}[/]", 
        title="[bold blue]Марка[/]",
        border_style="bright_magenta"
		))
        
    def print_car_model(self):
        self.__console.print(Panel.fit(
        f"[bold cyan]🇩🇪🚘Модель авто: {self.__model}[bold cyan]",
        title="[bold blue]Модель[/]",
        border_style="bright_magenta"
		))
        
    def print_car_price(self):
        self.__console.print(Panel.fit(
        f"[bold magenta]Цена авто: {self.__price}[/]",
        title="[bold blue]Цена[/][bold]💲[/]",
        border_style="bright_magenta"
		))        