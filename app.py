from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

scores_aiscore = openpyxl.load_workbook("scores_aiscore.xlsx")
sheet_aiscore = scores_aiscore["Sheet1"]

input_round = input(
    "Choose the round you want the match results (format: Just a number valid - 1 to 38): "
)

chrome_options = Options()
chrome_options.add_argument("--lang=en")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.aiscore.com/tournament-spanish-la-liga/yzrkn6iorbjqle4")

sleep(3)

buttons_round = driver.find_elements(
    By.XPATH, "//div[contains(@class, 'item flex justify-center align-center')]"
)

sleep(2)

for button_round in buttons_round:
    if button_round.text == input_round:
        button_round.click()
        sleep(2)

dates = driver.find_elements(By.XPATH, "//span[@class='col color-333 col-15']")
home_teams = driver.find_elements(By.XPATH, "//a[@itemprop='homeTeam']")
results = driver.find_elements(By.XPATH, "//a[@class='col col-10 color-333']")
away_teams = driver.find_elements(By.XPATH, "//a[@itemprop='awayTeam']")

for date, home_team, result, away_team in zip(dates, home_teams, results, away_teams):
    sheet_aiscore.append([date.text, home_team.text, result.text, away_team.text])

scores_aiscore.save("scores_aiscore.xlsx")
scores_aiscore.close()
driver.quit()
