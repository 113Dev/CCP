from rich.console import Console

console = Console()

def exit_check(input):
    if input.strip().lower() == "exit":
        console.print("Выход из программы...", style="bold red")
        exit()
    return input
