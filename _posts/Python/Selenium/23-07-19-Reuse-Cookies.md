---
title: Reuse Cookies in Selenium
date: 2023-07-19 02:02:00 -700
categories: [Python,Selenium]
tags: [python,selenium]
---

## Reuse Cookies in Selenium
In Selenium, cookies are your friend. Whenever you login to a system, always use cookies if there is a cookies option. See the following videos for more details:
* [Reuse cookies in Selenium with Python](https://www.youtube.com/watch?v=vhjKJ7huN-w)
* [Python Selenium Tutorial #7 - Save & Reuse Cookies](https://www.youtube.com/watch?v=dYAytG965ZE&list=PLuJJZ-W1NwdoTS0UXLUZoPH7GQ0kURHgH&index=7)

### Selenium Python Cookies Code:
Feel free to use these code snippets to save, load, and login with cookies:
* Save and load cookies:
```
	def save_cookies(self):
		cookies = self.driver.get_cookies()
		with open(self.cookie_location, 'wb') as f:
			pickle.dump(cookies, f)
		return cookies
#
	def load_cookies(self):
		try:
			with open(self.cookie_location, 'rb') as f:
				cookies = pickle.load(f)
			return cookies
		except:
			return []
```
* Login with Cookies:
```
	def cookie_login(self):
		logger.log('Attempting cookie login...', verbose=self.verbose)
		self.driver.get(self.tv_home)
		cookies = self.load_cookies()
		if len(cookies) == 0:
			return {'status': 400, 'message': 'Error: Failed to log in with cookies, no cookies found.'}
		for cookie in cookies:
			try:
				cookie['domain'] = '.tradingview.com'
				self.driver.add_cookie(cookie)
			except:
				pass
		logger.log('Cookies found and loaded...', verbose=self.verbose)
		try:
			logger.log('Checking to see if cookie login was successful...', verbose=self.verbose)
			time.sleep(1)
			self.driver.refresh()
			self.wait_locate(By.XPATH, "//div[contains(@class, 'widgetbar-pages')]", 'class')
			return {'status': 200, 'message': 'Successfully logged in with cookies.'}
		except:
			return {'status': 400, 'message': 'Error: Cookie login failed, cookies were invalid or expired.'}
```