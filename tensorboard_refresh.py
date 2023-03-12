import argparse
import time
from selenium import webdriver

parser = argparse.ArgumentParser(description='Atualizar dados do TensorBoard')

parser.add_argument('-p', '--page', type=str, help='Página do TensorBoard')
parser.add_argument('-t', '--time', type=int, help='Intervalo, em Segundos, para o Refresh')

args = parser.parse_args()
page = args.page
sleep = args.time

xpath = '/html/body/tb-webapp/app-header/mat-toolbar/app-header-reload'

nav = webdriver.Chrome()
nav.get(page)

while True:
    time.sleep(sleep)
    nav.find_element("xpath", xpath).click()
