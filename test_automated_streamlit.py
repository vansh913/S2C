import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_streamlit_test():
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get('http://localhost:8501')

        wait = WebDriverWait(driver, 20)

        # Wait for the text area to be available
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
        textarea.clear()
        example_story = (
            "John walked into the room. \"Hello, Mary!\" he said. Mary smiled back."
            " The sun was setting and they felt peaceful. \"Look at that beautiful sky,\" Mary whispered."
        )
        textarea.send_keys(example_story)

        # Select mode using selectbox (dropdown)
        selectbox = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'select')))
        selectbox.click()
        # Choose baseline as example
        for option in selectbox.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'baseline':
                option.click()
                break

        # Click generate button
        generate_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
        generate_button.click()

        # Wait for output image to appear - streamlit uses img with alt="Image"
        img = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
        src = img.get_attribute('src')
        print(f"Generated comic image URL: {src}")

        # Return success
        return True
    except Exception as e:
        print(f"Test failed: {e}")
        return False
    finally:
        driver.quit()


if __name__ == "__main__":
    success = run_streamlit_test()
    if success:
        print("Streamlit app automated test passed.")
    else:
        print("Streamlit app automated test failed.")
