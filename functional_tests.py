from selenium import webdriver

# spins a Firefox browser open
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

# checks if Congratulations is present in browser title
assert "Congratulations!" in browser.title

# if test passes, prints OK
print("OK")