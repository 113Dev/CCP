from rich.console import Console

console = Console()
	

from exit_check import exit_check
from Car import Car

console.print("(exit для выхода) ВВЕДИТЕ ДАННЫЕ О СВОЕЙ МАШИНЕ:", style="bold magenta")

marka = exit_check(console.input("[bold green]Марка машины:[/]"))
if marka == "":
    marka = "Undefined"
    
model = exit_check(console.input("[bold green]Модель авто:[/]"))
if model == "":
    model = "Undefined"
    
price = exit_check(str(console.input("[bold green]Цена вашего авто:[/]")))
if price.isnumeric():
    price = int(price)
else:
    while True:
        price = exit_check(str(console.input("[bold green]Цена вашего авто:[/]")))
        if price.isnumeric():
            price = int(price)
            break
        else:
            continue
        
marka_obj = Car(marka, model, price)


while True:
    def choisee():
        console.print("Что вы хотите сделать?(exit для выхода)", style="bold green")
        console.print("1. Инфо о авто ", style="bold magenta")
        console.print("2. Марка авто", style="bold magenta")
        console.print("3. Модел авто", style="bold magenta")
        console.print("4. Цена авто", style="bold magenta")
        console.print("5. Чекер цены авто", style="bold magenta")
        console.print("6. Изменить данные о авто", style="bold magenta")
     
    choisee()
    choise = exit_check(str(console.input("[bold green]ЦИФРА:[/bold green] ")))
     
    if choise.isnumeric():
        num = int(choise)
        if 1 <= num <= 6:
                choise = num
        else:
            while True:
                console.print("Ведите число от 1 до 6", style="bold red")
                choise = exit_check(str(console.input("[bold green]ЦИФРА:[/bold green] ")))
                num = int(choise)
                if 1 <= num <= 6:
                    choise = num
                    break
                else:
                    continue
                
    else:                   
        console.print("ОШИБКА:ВВЕДИТЕ НОМЕР КОМАНДЫ КОТОРУЮ ХОТИТЕ ВЫПОЛНИТЬ(exit для выхода)", style="bold magenta")
        while True:
            choisee()
            choise = exit_check(str(console.input("[bold green]ЦИФРА:[/bold green] ")))
            
            if choise.isnumeric():
                num = int(choise)
                if 1 <= num <= 6:
                    choise = num
                    break
            else:
                while True:
                    console.print("Ведите число от 1 до 6", style="bold red")
                    choise = exit_check(str(console.input("[bold green]ЦИФРА:[/bold green] ")))
                    if choise.isnumeric():
                        num = int(choise)
                        if 1 <= num <= 6:
                            choise = num
                            break
                    else:
                        continue
                    
    if choise == 1:
        marka_obj.print_car_info()
        
    elif choise == 2:
        marka_obj.print_car_marka()
        
    elif choise == 3:
        marka_obj.print_car_model()
        
    elif choise == 4:
        marka_obj.print_car_price()
        
    elif choise == 5:
        marka_obj.check_price_car()
        
    elif choise == 6:
        console.print("ВВЕДИТЕ НОВЫЕ ДАННЫЕ О СВОЕЙ МАШИНЕ:", style="bold magenta")
        marka = exit_check(console.input("[bold green]Марка машины:[/]"))
        model = exit_check(console.input("[bold green]Модель авто:[/]"))
        price = exit_check(str(console.input("[bold green]Цена вашего авто:[/]")))
        if price.isnumeric():
            price = int(price)
        else:
            while True:
                price = exit_check(str(console.input("[bold green]Цена вашего авто:[/]")))
                if price.isnumeric():
                    price = int(price)
                    break
                else:
                    continue
 
        marka_obj = Car(marka, model, price)
        