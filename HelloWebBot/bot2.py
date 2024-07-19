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
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

tabela_xpath = '/html/body/div[3]/div[2]/div/div[2]/div'

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    """ chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors') """
    
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    # bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    bot.driver_path = "C:\chromedriver\chromedriver-win64\chromedriver.exe"

    # Opens the BotCity website.
    bot.browse("https://datatables.net")
    
    try:
        if not bot.find_element(By.XPATH, tabela_xpath):
            print("Elemento não encontrado")
            return
        
        linhas_xpath = tabela_xpath + "//tr"
        linhas = bot.find_element(By.XPATH, linhas_xpath)
        
        dados_tabela = []
        
        for linha in linhas:
            celulas = linha.find_elements(By.XPATH, ".//td")
            dados_linha = [celula.text for celula in celulas]
            dados_tabela.append(dados_linha)
            
        for dados in dados_tabela:
            print(dados) 
        # Implement here your logic...
    except Exception as e:
        print(f"An exception was ocurred {e}")
    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
