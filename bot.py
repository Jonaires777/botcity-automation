"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot, Backend

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    app_path = "wordpad.exe"
        
    bot.execute(app_path)
    
    bot.connect_to_app(backend=Backend.UIA, path=app_path)
    
    main_window = bot.find_app_window(title_re='Documento - WordPad', class_name="WordPadClass", control_type="Window")
                    
    edit = bot.find_app_element(from_parent_window=main_window, control_type="Document", class_name='RICHEDIT50W')
    
    edit.type_keys("Hello, Welcome to BotCity", with_spaces=True)
    
    """ save_work = bot.find_app_element(from_parent_window=main_window, control_type="Button", title_re="Salvar") """
    
    """ save_work.click() """
    
    bot.wait(2000)
    
    select = bot.find_app_element(from_parent_window=main_window, title="Selecionar tudo", control_type="Button")
    
    select.click()
        
    bot.backspace()

    edit.type_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et massa ipsum. Donec malesuada tincidunt sapien, nec egestas mi ornare eu. Maecenas commodo ex ut arcu maximus mattis. Pellentesque ac aliquet mi. Fusce luctus eros ante, ut cursus sem suscipit quis. Donec id nisi non mauris pulvinar tincidunt pharetra vel lacus. Nunc lacinia id lectus sed ornare. Vestibulum tincidunt fringilla aliquet. Aenean dolor justo, vulputate quis lacus vitae, venenatis faucibus sem. Integer id ante in nibh aliquet commodo eu nec augue. Duis ac sapien et augue condimentum tristique in nec dolor. Etiam at ipsum metus. Fusce luctus velit quis placerat commodo. Aenean ut venenatis nibh.")
    
    close = bot.find_app_element(from_parent_window=main_window, title="Fechar", control_type="Button")    
    
    close.click()
    
    bot.wait(2000)
    
    """ popup_window = bot.find_app_window(title="WordPad")

    save_button = bot.find_app_element(from_parent_window=popup_window, title="Salvar", control_type="Button")
    
    save_button.click() """
    
    bot.click_at(x=630, y=400)
    
    bot.click_at(x=750, y=600)

    bot.backspace()
    bot.kb_type("WordPad_Automation_Teste")
    
    bot.click_at(x=830, y=680)

    print("Tarefa finalizada")
    """ save_window = bot.find_app_window(title="Salvar como", class_name="ThunderRT6MDIForm")
    
    if save_window:
        print("Janela de salvamento encontrada.")
        save_window.print_control_identifiers()
    else:
        print("Janela de salvamento não encontrada.") """
    
def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()