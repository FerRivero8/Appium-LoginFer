#from multiprocessing.pool import AsyncResult
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest
import allure
from allure_commons.types import AttachmentType
import time

# Importamos clase Main para cobertura
import main

@pytest.fixture()
def test_setup():
    # Capabilites en forma de Options (ya que la otra manera había quedado obsoleta)
    options = UiAutomator2Options()
    options.device_name = "R5CRB0X2M5N"
    options.platform_name = "Android"
    options.app_package = "com.example.mylogin"
    options.app_activity = "com.example.mylogin.MainActivity"
    
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    yield
    driver.quit()

""" ******************************  HASTA AQUÍ LEVANTA LA APP ESCOGIDA *********************************** """

@allure.description("Ingresar credenciales correctas y acceder a la pantalla de Bienvenida.")
def test_validCredentials(test_setup):
    driver.find_element("id", 'com.example.mylogin:id/inputUsername').send_keys("admin")
    driver.find_element("id", 'com.example.mylogin:id/inputPassword').send_keys("admin")
    driver.find_element("id", 'com.example.mylogin:id/btnLogin').click()
    
    assert ".DialerActivity" in driver.current_activity

@allure.description("Ingresar credenciales inválidas y permanecer en la pantalla Login.")
def test_invalidCredentials(test_setup):
    driver.find_element("id", 'com.example.mylogin:id/inputUsername').send_keys("fernando")
    driver.find_element("id", 'com.example.mylogin:id/inputPassword').send_keys("admin")
    driver.find_element("id", 'com.example.mylogin:id/btnLogin').click()
    assert ".MainActivity" in driver.current_activity

@allure.description("Ingresar credenciales inválidas y permanecer en la pantalla Login (parte 2).")
def test_invalidCredentials2(test_setup):
    driver.find_element("id", 'com.example.mylogin:id/inputUsername').send_keys("fernando")
    driver.find_element("id", 'com.example.mylogin:id/inputPassword').send_keys("admin")
    driver.find_element("id", 'com.example.mylogin:id/btnLogin').click()
    try:
        assert ".DialerActivity" in driver.current_activity
    finally:
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Credentials", attachment_type=AttachmentType.PNG)
    
@allure.description("Acceder a la pantalla de registro.")
def test_userRegister(test_setup):
    driver.find_element("id", 'com.example.mylogin:id/btnSignUp').click()
    assert ".RegisterActivity" in driver.current_activity 
