from time import sleep
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas,random,pyperclip,requests 
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from bs4 import BeautifulSoup
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

class Whatsapp():
    MAX_SCROLL = """
    i = document.querySelector("div[class='_3Bc7H g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o ag5g9lrv bs7a17vp']");
    return i.scrollHeight;

    """
    SCROLL_DOWN_CURRENT= """
    i.scrollTop = i.scrollTop + i.offsetHeight;
    return i.scrollTop;
    """
    SCRAPE_NUMBERS_CODE = """
    numbers = document.querySelectorAll("div[tabindex='0'] div._3uIPm.WYyr1 div.zoWT4");
    return numbers;
    """
    def __init__(self,list_) -> None:
        self.headless = False
        self.contact_file = list_[0]
        self.msg_file = list_[1]
        self.waiting_time = list_[2]
        option = Options()
        option.headless = self.headless
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        option.add_argument('--disable-logging')
        self.driver =webdriver.Chrome(ChromeDriverManager().install(),options=option)
        self.driver.maximize_window()
        self.driver.get("https://web.whatsapp.com/")
        self.wait = WebDriverWait(self.driver, 500)
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@data-testid='chatlist-header']")))   
        self.search_ = self.driver.find_element(By.XPATH,value="//*[@data-testid='chat-list-search']")

        
        

    def jscode(self,command):
        return self.driver.execute_script(command)


    @staticmethod
    def messagebox(text): # that mean this Function not working outside Class
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Critical)
            messagebox.setText(f" {text} ")
            messagebox.setWindowTitle(" Warning ")
            messagebox.exec_()


    def check_number(
        self,
        number: str,
    ) -> bool:
        f"""Checks the Number to see if number have +966 """

        return ("+966" in number)
           


    def send_msg_to_phone(
        self,
        phone_num:str,
        text:str,
        
    ):
        sleep(int(self.waiting_time)-8)

        self.driver.get(f"https://web.whatsapp.com/send?phone={phone_num}&text=")
        self.driver.implicitly_wait(5)
        self.wait_elm(by=By.XPATH,val="//div[@title='Type a message']",timeout=30)
        lastcopy = pyperclip.paste()
        pyperclip.copy(text)
        act = ActionChains(self.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        act.key_down(Keys.ENTER).perform()
        pyperclip.copy(lastcopy)
        

        

    def wait_clickable(self,val:str,by:str=By.XPATH,timeout:int=30)->WebElement:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        return self.wait.until(EC.element_to_be_clickable(arg))
        

    def convert(self)->tuple:
        
        try:
            phone_numbers =self.convert_lists(self.contact_file,"Number")
            messages = self.convert_lists(self.msg_file,"messages")
            return phone_numbers,messages
        except Exception as e:
            self.messagebox(e)
            return False


    def have_whatsapp(self,phone):
        #+966593886033
        self.driver.get(f"https://web.whatsapp.com/send?phone={phone}&text=")       ###http://wa.me/0543881690
        self.driver.implicitly_wait(3)
        try:
            self.wait_elm("//div[@title='Type a message']",timeout=5)
            return True
        except:
            return False
            

    def convert_lists(
        self,
        excel_name:str,
        col_name:str):

        df = pandas.read_excel(excel_name)
        df = df.drop_duplicates(subset=col_name,keep="first") ## remove duplicates
        df.dropna(inplace=True)
        list_ = df[col_name].to_list()
        return list_
        

    def random_msg(
        self,
        msg_list:list)->str:
        if len(msg_list)<1:
            self.messagebox(" Message List is Empty Please Write any Messages ")
        else:
            index = random.randint(0,len(msg_list)-1)

        return str(msg_list[index])
    

   
    def search(self,phone)-> bool:
        phone = self.phone_s(f"+{phone}")
        self.search_ = self.driver.find_element(By.XPATH,value="//*[@data-testid='chat-list-search']")
        self.search_.clear()
        self.search_.send_keys(phone)
        try:
            f = self.wait_elm(val=f"//span[@title='{phone}']",timeout=10)
            return True
        except Exception as e :
            return False
        
    def wait_elm(self,val:str,by:str=By.XPATH,timeout:int=30)->WebElement:
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        arg = (by,val)
        return self.wait.until(EC.presence_of_element_located(arg))


    def phone_s(self,phone:str):
        return phone[:4]+" "+phone[4:6]+" "+phone[6:9]+" "+phone[9:]

    def exit(self):
        self.wait_elm("//*[@id='app']/div/div/div[3]/header/div[2]/div/span/div[3]/div/span",timeout=5).click()
        logout = self.wait_clickable("//*[@aria-label='Log out']",timeout=5).click()
        self.wait_clickable("//*[@data-testid='popup-controls-ok']",timeout=5).click()
        sleep(5)
        self.driver.quit()
     
    def scrape_numbers(self,group_link:str):
        url = group_link.replace("https://chat.whatsapp.com/","https://web.whatsapp.com/accept?code=")
        self.driver.get(url)
        self.wait_elm("//div[@data-testid='popup-controls-ok']").click() # Going into Group
        self.wait_elm("//div[@data-testid='chat-subtitle']").click() #  Show side bar
        self.wait_elm("//div[@class='ggj6brxn ljrqcn24 jq3rn4u7']").click() # Show All Numbers 
        maxhight = self.jscode(self.MAX_SCROLL)
        current = 0
        numbers = []
        while maxhight > current :
            sub_numbers =  self.jscode(self.SCRAPE_NUMBERS_CODE)
            for num in sub_numbers:
                number = num.text
                if numbers.count(number) > 0:
                    numbers.append(number)
                    print(number)
            current = self.jscode(self.SCROLL_DOWN_CURRENT)



        self.wait_elm("//span[@class='_3NUK1 _2Hpjf VWPRY _1lF7t BZCNr']").click() # Red Button For exit Group 

        self.wait_elm("//div[@data-testid='popup-controls-ok']").click() # Exit Button Green 

        
#  div[data-testid="chat-subtitle"]       Header of group
#  span[class="_3NUK1 _2Hpjf VWPRY _1lF7t BZCNr"]     [0]  Delete Red Button
#  div[data-testid="popup-controls-ok"]                Exit Group Button
 



class StockInfo():
    def __init__(self) -> None:

        pass

    def get_chart(self,stock_code)->list:
        req = requests.get(f"https://www.mubasher.info/markets/TDWL/stocks/{stock_code}")
        soup = BeautifulSoup(req.text, 'html.parser')
        try:
            current_price = soup.find("div",class_="market-summary__last-price down-icon-only").text
            type = "down"
        except Exception as e :
            try:
                current_price = soup.find("div",class_="market-summary__last-price unchanged-icon-only").text
                type = "unchanged"
            except:
                try:
                    current_price = soup.find("div",class_="market-summary__last-price up-icon-only").text
                    type = "up"
                except :
                    current_price = False
                    type = "Error in type"

        charts = soup.find_all("span",class_="market-summary__block-number")
        #print(charts)
        if not current_price :
            chart_list = ["No Stock has this code !!!!!!",type]
        else:
            chart_list = [float(current_price),type]

        for chart in charts:
            #print(chart)
            chart_list.append(float(chart.text.replace(",","")))
        return chart_list



    def analysis(self,stock_code,type):
        if type == "Error in type":
            list_ = None
        else:
            req = requests.get(f"https://www.mubasher.info/markets/TDWL/stocks/{stock_code}/support-resistance")
            soup = BeautifulSoup(req.text, 'html.parser')

            price_from_fulcrum = soup.find_all("div",class_=f"support-and-resistance__change-column-2 number {type}")[1].text
            elms = soup.find_all("span",class_="support-and-resistance__block-number")
            list_ = [price_from_fulcrum]
            for elm in elms:  #[Second resistance level (M2) , First resistance level (M1) , fulcrum point , First support level (D1) , Second support level (D2)]
                list_.append(float(elm.text))

        return list_



    def tasi_statues(self):
        req = requests.get(f"https://www.saudiexchange.sa/wps/portal/tadawul/markets/equities/indices/today?locale=ar")
        soup = BeautifulSoup(req.text, 'html.parser')
        try:
            current_price = soup.findAll("dl",class_="in_tbl large down")[1].text
            type = "down"
        except Exception as e :
            try:
                current_price = soup.findAll("dl",class_="in_tbl large unchanged")[1].text
                type = "unchanged"
            except:
                try:
                    current_price = soup.findAll("dl",class_="in_tbl large up")[1].text
                    type = "up"
                except :
                    current_price = False
                    type = "Error in type"
        val = soup.findAll("dl",class_=f"in_tbl large {type}")[1].text.split("-")[0].replace("\n","")
        return (type,val)


    def time_sission(self)->str:
        now = datetime.now()
        current_time = now.strftime("%H")#:%M:%S
        
        if int(current_time)>= 9 and int(current_time)< 14: # in session
            return "in session"
        else: # after sission
            return "out session"

    def format_tasi_statues(self,tuple_:tuple)->list:
        if tuple_[0] == "down":
            return [float(tuple_[1].replace("-","")),False]
        elif tuple_[0]=="up":
            return [float(tuple_[1]),True]
        else:
            return [float(tuple_[1]),None]
        
    

#https://web.whatsapp.com/accept?code=Jb71Ee7okxx0KeXFOjcYeC


    
# def msg_ai(setting)->str:
#     stock = StockInfo()
#     s = stock.tasi_statues()
#     if len(setting)>3:
#             if s[0]=="down":
#                     if int(s[1].split(".")[0]) >= self.setting[3]:
#                             return "tasi down"
#                     else:
#                             return stock.time_sission()
#             else:    
#                     return stock.time_sission()
#     else:
#             return "messages"

"""
s= StockInfo().tasi_statues()

print(int(s[1].split(".")[0]))

stock = StockInfo()
s = stock.tasi_statues()
if s[0]=="down":
    if int(s[1].split(".")[0]) >= 10:
        print("tasi down") 
    else:
        print(stock.time_sission())
else:    
    print(stock.time_sission())
"""
#https://web.whatsapp.com/send?group=HiWWbHEOijSCfKoPwN1N0y&text=.
#https://chat.whatsapp.com/HiWWbHEOijSCfKoPwN1N0y

#sleep(100)
#sleep(10)
