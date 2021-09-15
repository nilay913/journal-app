Feature('Admin Page Tests');

Scenario('1. Admin Page Create Resource and View On Front-End', ({ I }) => {
	I.amOnPage("http://127.0.0.1:8000/")
	I.dontSee("test name")
	I.dontSee("http://test.com")
	I.amOnPage('http://127.0.0.1:8000/admin/')
	I.fillField("username","admin")
	I.fillField("password","nilay913")
	I.click("Log in")
	I.amOnPage("admin/journal/resource/add/")
 	I.fillField("Name:","test name")
 	I.fillField("Link:","http://test.com")
 	I.selectOption("#id_software","Django")
 	I.attachFile('#id_attachment','test.jpg')
 	I.click("_save")
 	I.click("View site")
 	I.see("test name")
 	I.see("http://test.com")
});

Scenario('2. Admin Page Edit Resource and View On Front-End', ({ I }) => {
	I.amOnPage("http://127.0.0.1:8000/")
	I.see("test name")
	I.see("http://test.com")
	I.amOnPage('http://127.0.0.1:8000/admin/')
	I.fillField("username","admin")
	I.fillField("password","nilay913")
	I.click("Log in")
	I.click("Resource object")
 	I.fillField("Name:","test name UPDATE")
 	I.fillField("Link:","http://testUPDATE.com")
 	I.click("_save")
 	I.click("View site")
 	I.see("test name UPDATE")
 	I.see("http://testUPDATE.com")
});


Scenario('3. Admin Page Delete Resource and View On Front-End', ({ I }) => {
	I.amOnPage("http://127.0.0.1:8000/")
	I.see("test name UPDATE")
	I.see("http://testUPDATE.com")
	I.amOnPage('http://127.0.0.1:8000/admin/')
	I.fillField("username","admin")
	I.fillField("password","nilay913")
	I.click("Log in")
	I.click("Resource object")
 	I.click("Delete")
 	I.click("Yes, I’m sure")
 	I.click("View site")
 	I.dontSee("test name UPDATE")
 	I.dontSee("http://testUPDATE.com")
});
