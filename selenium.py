from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

webdriver_path = './drivers/chromedriver.exe'  # Change this to the path of your webdriver
driver = webdriver.Chrome(executable_path=webdriver_path)

# List of items to search on Amazon
items_to_search = ["books", "shirts", "magzine"]  # Add your items to the list

search_results = []

for item in items_to_search:
    # Navigate to Amazon
    driver.get("https://www.amazon.com/")

    # Find the search input field and enter the current item
    search_box = driver.find_element("id", "twotabsearchtextbox")
    search_box.clear()  # Clear any previous text
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)

    # Wait for some time to allow the page to load
    time.sleep(3)

    # Extract the results (you may need to adjust the selector based on Amazon's site structure)
    results = driver.find_elements_by_css_selector(".s-result-item")
    
    # Store the results in the search_results list
    search_results.append({item: [result.text for result in results]})

# Print or process the search results
for result in search_results:
    for item, results in result.items():
        print(f"Results for {item}:")
        for r in results:
            print(r)
        print("\n")

driver.quit()