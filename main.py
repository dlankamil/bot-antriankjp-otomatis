import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Load data dari file JSON
with open('json/data.json', 'r') as file:
    data = json.load(file)

# Pilih nama dari json/data.json
nama = "Nama1"
kk_value = data[nama]["kk"]
ktp_value = data[nama]["ktp"]
kartu_value = data[nama]["kartu"]

# Setup Chrome agar tidak langsung close setelah diisi semuanya
options = Options()
options.add_experimental_option("detach", True)

# Lokasi file chromedriver.exe, sesuaikan!
service = Service('C:/laragon/www/bot-antriankjp-otomatis/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

# Link antriankjp
driver.get('https://antriankjp.pasarjaya.co.id/')

# Tunggu hingga max 40 detik
wait = WebDriverWait(driver, 40)

# Pilih opsi select 
wilayah_select_elem = wait.until(EC.presence_of_element_located((By.ID, 'wilayah')))
select = Select(wilayah_select_elem)
select.select_by_value('4')  # pilih opsi Jakarta Selatan (lihat pada json/wilayah.json untuk melihat value)

lokasi_select_elem = wait.until(EC.presence_of_element_located((By.ID, 'lokasi')))
select = Select(lokasi_select_elem)
select.select_by_value('109')  # pilih opsi Pancoran (lihat pada json/lokasi.json untuk melihat value)

# Isi input teks
wait.until(EC.presence_of_element_located((By.ID, 'kk'))).send_keys(kk_value)
wait.until(EC.presence_of_element_located((By.ID, 'ktp'))).send_keys(ktp_value)
wait.until(EC.presence_of_element_located((By.ID, 'kartu'))).send_keys(kartu_value)

# Ceklist checkbox
checkbox = wait.until(EC.presence_of_element_located((By.ID, 'box')))
if not checkbox.is_selected():
    checkbox.click()
    
print('Tinggal isi captcha aja~')