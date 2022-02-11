from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
import datetime
from selenium.webdriver.common.keys import Keys


class TestOne(BaseClass):

    def test_e2e(self):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)

        sf_window = self.driver.window_handles[1]
        self.driver.switch_to.window(sf_window)
        try:
            self.driver.find_element(By.LINK_TEXT, "Office 365").click()
            self.driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")

        except Exception as e:
            self.driver.get("https://optimatax--develop.lightning.force.com/lightning/page/home")
            print(e)
        try:
            alert = self.driver.switch_to.alert()
            alert.accept()
        except Exception as e:
            print(e)

        self.driver.find_element(By.XPATH, "//div[@class='slds-card__body']/button").click()

        self.driver.execute_script("window.open('about:blank','disposable_email');")
        self.driver.switch_to.window("disposable_email")
        self.driver.get("https://www.disposablemail.com/")
        email = self.driver.find_element(By.CSS_SELECTOR, "span[id='email']").text

        self.driver.switch_to.window(sf_window)
        self.driver.find_element(By.XPATH, "//div[@id='modal-content-id-1']/div[6]/input").send_keys(email)

        first_name_last_name = email.split(".")
        firstName = first_name_last_name[0].capitalize()
        parsedLastname = first_name_last_name[1].split("@")
        lastName = parsedLastname[1].capitalize()

        self.driver.find_element(By.XPATH, "//div[@id='modal-content-id-1']/div[1]/input").send_keys(firstName + " " + lastName)
        self.driver.find_element(By.CSS_SELECTOR, "button[title='Create Data']").click()

        button = self.driver.find_element_by_xpath("//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
        self.driver.execute_script("arguments[0].click();", button)

        tel_css_selector = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").get_attribute(
            "value")

        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").clear()
        save = self.driver.find_element_by_xpath("//button[@title='Save']")
        self.driver.execute_script("arguments[0].click();", save)

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h3[title='Phone']")))
        time.sleep(2)
        phone_lead_conversion_window = self.driver.find_element(By.CSS_SELECTOR, "h3[title='Phone']").text
        self.driver.execute_script("window.scrollTo(0,0);")
        assert "Phone" in phone_lead_conversion_window
        time.sleep(1)
        self.driver.refresh()

        #adding wait because execute script of clicking the edit penchil is happening before the pencil is loaded.
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[title='Edit Phone, Primary'] lightning-primitive-icon")))
        edit_pencil = self.driver.find_element(By.XPATH,"//button[@title='Edit Phone, Primary']/lightning-primitive-icon")
        self.driver.execute_script("arguments[0].click();", edit_pencil)
        self.driver.execute_script("window.scrollTo(0,0);")
        self.driver.find_element(By.XPATH,"//a[contains(text(), 'Contact Details')]/parent::h2/parent::div/parent::div/parent::div/parent::div/div[2]/div/div/div[2]/div/section/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/input").send_keys(tel_css_selector)
        second_save = self.driver.find_element(By.XPATH, "//span[contains(text(),'Save' )]")
        action.move_to_element(second_save).perform()
        action.click(second_save).perform()


        convert_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Convert')]")
        self.driver.execute_script("arguments[0].click();", convert_button)

        java_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        self.driver.execute_script("arguments[0].click();", java_button)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        self.driver.refresh()
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")))
        create_payment_schedule_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create Pmt Schedules')]")
        self.driver.execute_script("arguments[0].click();", create_payment_schedule_button)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "div[id='modal-content-id-1'] iframe")))
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='date']")))
        date_element = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")
        current_time = datetime.datetime.now()
        date = str(current_time.strftime(("%m"))) + str(current_time.day) + str(current_time.year)
        print(date)

        time.sleep(5)
        #action.move_to_element(date_element).perform()
        #action.click(date_element).perform()
        #action.send_keys(Keys.ARROW_UP).send_keys(Keys.ARROW_LEFT).perform()
        #action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_LEFT).perform()
        #action.send_keys(Keys.ARROW_UP).perform()
        self.driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()
        time.sleep(10)

        self.driver.switch_to.default_content()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[7]/a")))
        manage_docs_element = self.driver.find_element(By.XPATH, "//ul[@role='tablist']/li[7]/a")
        self.driver.execute_script("arguments[0].click();", manage_docs_element)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@class='content iframe-parent']/iframe")))
        #putting sleep here because error that iframe cannot be found is thrown
        time.sleep(1)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='manage-forms']")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "i[class ='fa fa-rocket']").click()
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[style='display: block;']")))
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success send-email']").click()
        self.driver.switch_to.window("disposable_email")
        self.driver.find_element(By.CSS_SELECTOR, "a[title='Refresh this page']").click()

        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "//td[contains(text(),'Welcome to Optima Tax Relief')]").click()
        self.driver.switch_to.frame("iframeMail")
        self.driver.find_element(By.LINK_TEXT, "Create Account →").click()
        time.sleep(1)

        portal = self.driver.window_handles[3]
        self.driver.switch_to.window(portal)
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_name("password_confirmation").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "button[id='login-btn'").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Acknowledge')]").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Started')]").click()
        self.driver.find_element(By.LINK_TEXT, "I Agree").click()

        canvas = self.driver.find_element(By.CSS_SELECTOR, "div[class*='pad--body'] canvas")
        action.click_and_hold(canvas) \
            .move_by_offset(-10, -15) \
            .move_by_offset(20, 32) \
            .move_by_offset(10, 25) \
            .release()
        action.perform()
        submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        self.driver.execute_script("arguments[0].click();", submit_button)

        ssn = self.driver.find_element(By.CSS_SELECTOR, "input[name='masked_tax_identification_number']")
        ssn.send_keys("123456789")
        dob_dropdowns_elements = self.driver.find_elements(By.CSS_SELECTOR, "select[name*='birth']")
        for dob in dob_dropdowns_elements:
            date_select = Select(dob)
            date_select.select_by_index(2)
        verify_button = self.driver.find_element(By.CSS_SELECTOR, "button[id='show-confirmation-modal']")
        self.driver.execute_script("arguments[0].click();", verify_button)
        self.driver.find_element(By.CSS_SELECTOR,"button[id='forms-nav-verify']").click()

        for i in range(4):
            try:
                self.driver.find_element(By.PARTIAL_LINK_TEXT, "View").click()
                self.driver.find_element(By.LINK_TEXT, "read more...").click()
                program_outline = self.driver.find_elements(By.CSS_SELECTOR, "div[class='more'] p")
                for p in program_outline:
                    text = p.text
                    assert text is not None, "Program outline may be missing contents please login to check."
                self.driver.find_element(By.CSS_SELECTOR, "button[class='close']").click()
                # self.driver.execute_script("argument[0].scrollIntoView();", close_element)
                # close_element.click()
                continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
                self.driver.execute_script("arguments[0].click();", continue_button_location)
            except:
                self.driver.find_element(By.CSS_SELECTOR, "button[class='close']").click()
                continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
                self.driver.execute_script("arguments[0].click();", continue_button_location)

        self.driver.find_element(By.XPATH, "//div[@id='signers']/button[1]").click()

        self.driver.find_element(By.XPATH, "//button[contains(text(),'Credit or Debit Card')]").click()

        self.driver.find_element(By.CSS_SELECTOR, "input[id='cc-number']").send_keys(
            "4111111111111111")

        self.driver.find_element(By.CSS_SELECTOR, "input[name='cc_cvv']").send_keys(
            "123")

        #check confirm payment schedule button because it goes back to the payment page
        for i in range(4):

            continue_button_location = self.driver.find_element(By.CSS_SELECTOR, "[class*='btn-success']")
            self.driver.execute_script("arguments[0].click();", continue_button_location)

        self.driver.switch_to.window(sf_window)

        self.driver.refresh()

        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//ul[@role='tablist']/li[7]/a")))
        manage_docs_element = self.driver.find_element(By.XPATH, "//ul[@role='tablist']/li[7]/a")
        self.driver.execute_script("arguments[0].click();", manage_docs_element)

        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//div[@class='content iframe-parent']/iframe")))
        # putting sleep here because error that iframe cannot be found is thrown
        time.sleep(1)
        wait.until(
            expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='manage-forms']")))
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[id='ready-for-payments-btn']").click()

        self.driver.execute_script("window.open('about:blank','admin_portal');")
        self.driver.switch_to.window("admin_portal")
        self.driver.get("https://admin-dev.optimatax.com/dashboard")

        self.driver.find_element(By.CSS_SELECTOR, "input[id='search']").send_keys(firstName)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Opportunities").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Opportunity").click()
        self.driver.find_element(By.XPATH, "//tr[@id='form-21244']/td[5]").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Approve").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Services").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Payments").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Payment Schedule").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Pay Now')]").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-form-id='pay-now-otr-form']").click()

        try:
            alert_success_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'processed successfully.')]")
            wait.until(expected_conditions.visibility_of(alert_success_element))
            print(alert_success_element.text)
        except:
            print("Unable to verify alert-success for Payment")

        self.driver.switch_to.window(sf_window)




























