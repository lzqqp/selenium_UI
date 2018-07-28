from selenium import webdriver
from pub import login
from pwd_read import password
import unittest

class Logintest(unittest.TestCase):

    def setUp(self):

        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url='https://www.yunke.com/index.main.login'
        self.driver.get(self.base_url)
        print('测试开始')
    def tearDown(self):
        self.driver.close()
        print('测试结束')
    def test_correct(self):
        #用户名正确,密码正确
        login(self.driver,password(1,0),password(1,1))
        self.driver.implicitly_wait(1)
        self.curl=self.driver.current_url
        self.assertEqual(self.base_url,self.curl,msg='you are right')

    def test_username_error(self):
        # 用户名错误，密码正确
        login(self.driver, password(5, 0), password(5, 1))
        self.driver.implicitly_wait(1)
        self.curl = self.driver.current_url
        self.assertEqual(self.base_url, self.curl, msg='you are right')

    def test_username_null(self):
        # 用户名为空，密码正确
        login(self.driver, password(4, 0), password(4, 1))
        self.driver.implicitly_wait(1)
        self.curl = self.driver.current_url
        self.assertEqual(self.base_url, self.curl, msg='you are right')

    def test_pwd_correct(self):
        # 用户名正确，密码错误
        login(self.driver, password(2, 0), password(2, 1))
        self.driver.implicitly_wait(1)
        self.curl = self.driver.current_url
        self.assertEqual(self.base_url, self.curl, msg='you are right')

    def test_pwd_null(self):
        # 用户名和密码正确
        login(self.driver, password(3, 0), password(3, 1))
        self.driver.implicitly_wait(1)
        self.curl = self.driver.current_url
        self.assertEqual(self.base_url, self.curl, msg='you are right')

'''
        def test_password_error(self):
            login(password(2,0),password(2,1))
        def test_password_null(self):
            login(password(3,0),password(3,1))
        def test_username_error(self):
            login(password(4,0),password(4,1))
        def test_username_null(self):
            login(password(5,0),password(5,1))
    except:
        pass
'''

if __name__=='__main__':
    unittest.main()