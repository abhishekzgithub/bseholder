# -*- coding: utf-8 -*-
import requests
import json
import ast

# Added for Selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import selenium.webdriver.support.ui as ui
from selenium.webdriver.chrome.options import Options
from datetime import date, datetime
import sqlite3 as sql
from string import ascii_lowercase
from selenium.common.exceptions import TimeoutException
from DCRDataBaseUtility import db_query, db_commit_query, db_json, db_commit_query_id
from selenium.webdriver.common.keys import Keys

# TO MAKE THE SCRAPPING FASTER
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
delay = 0
# Query for Ticker
BSE_ticker_list = db_query("""
    select Ticker, BSETicker
    from TblCompany
    where Ticker != "" and BSETicker != "" and BSETicker is not Null 
""")

'65, 69, 73, 77, 81, 85, 89, '
period_id_list = [85]

for period_id in period_id_list:
    for b in BSE_ticker_list:

        BSETicker = b['BSETicker']
        Ticker = b['Ticker']

        link_profile = "https://beta.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=" + \
            BSETicker + "&qtrid="+str(period_id)+"&QtrName=A"
        driver.get(link_profile)

        try:
            myElem = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "TTRow")))

        except TimeoutException:
            pass

        holder_dict = {
            "holder_name": "",
            "holder_type": "",
            "no_of_shareholders": 0,
            "no_of_fully_paid_shares": 0,
            "num_total_shares": 0,
            "perc_total_shares": 0.0,
            "num_pledged_shares": 0,
            "perc_pledged_shares": 0.0,
            "num_demat_shares": 0,
            "Ticker": Ticker,
            "period_id": period_id
        }
        col_list = ['holder_name', 'no_of_shareholders', 'no_of_fully_paid_shares',
                    'num_total_shares', 'perc_total_shares', 'num_pledged_shares', 'perc_pledged_shares']
        col_dic = {'Category of shareholder': 'holder_name',
                   'Nos. of shareholders': 'no_of_shareholders',
                   'No. of fully paid up equity shares held': 'no_of_fully_paid_shares',
                   'Total nos. shares held': 'num_total_shares',
                   'Shareholding as a % of total no. of shares (calculated as per SCRR, 1957)As a % of (A+B+C2)': 'perc_total_shares',
                   'Number of equity shares held in dematerialized form': 'num_demat_shares'
                   }
        try:
            table_1 = driver.find_elements_by_tag_name('table')
            table_2 = table_1[0].find_elements_by_tag_name('table')
            main_table = table_2[0].find_elements_by_tag_name('table')
            # print main_table[1].text
            # get all of the rows in the table
            headers = driver.find_elements_by_class_name('innertable_header1')
            i = 0
            flag = 0
            key_dict = {}
            index_dict = {}
            demat_adj = 0
            # Using colspan to get the rows which are multicolmn heading
            for h in headers:
                try:
                    # Adjust for the sub headings
                    if h.text == 'Number of Shares pledged or otherwise encumbered':
                        key_dict['num_pledged_shares'] = i
                        key_dict['perc_pledged_shares'] = i + 1
                    else:
                        key_dict[col_dic[h.text]] = i
                except:
                    pass
                if len(h.get_attribute('outerHTML').split('colspan="', 1)) > 1:
                    # flag is the extra columns i must add
                    flag = int(h.get_attribute('outerHTML').split(
                        'colspan="', 1)[1].split('">')[0]) - 1
                else:
                    flag = 0
                i = i + 1 + flag
            index_dict = {y: x for x, y in key_dict.iteritems()}

            rows = main_table[1].find_elements(By.TAG_NAME, "tr")
            for row in rows:
                # Get the columns (all the column 2)
                # note: index start from 0, 1 is col 2
                col_count = 0
                try:
                    col = row.find_elements(By.TAG_NAME, "td")

                    for c in col:
                        # Check if it is a heading text
                        # print c.text
                        flag = True

                        if c.text == "A1) Indian":
                            holder_dict["holder_type"] = 'Total|A|A1'
                        elif c.text == "A2) Foreign":
                            # This is a category A heading
                            holder_dict["holder_type"] = 'Total|A|A1'
                            # This row is blank now
                            flag = False
                            break
                        if c.text == "Individuals/Hindu undivided Family":
                            holder_dict["holder_type"] = 'Total|A|A1|I'
                            holder_dict["holder_name"] = "Individuals/Hindu undivided Family"
                        elif c.text == "Individuals (NonResident Individuals/ Foreign Individuals)":
                            holder_dict["holder_type"] = 'Total|A|A2|I'
                            holder_dict["holder_name"] = "Individuals (NonResident Individuals/ Foreign Individuals)"
                        elif c.text == "Sub Total A1":
                            holder_dict["holder_type"] = 'Total|A|A1'
                            holder_dict["holder_name"] = "Sub Total A1"
                        elif c.text == "Sub Total A2":
                            holder_dict["holder_type"] = 'Total|A|A2'
                            holder_dict["holder_name"] = "Sub Total A2"
                        elif c.text == "A=A1+A2":
                            holder_dict["holder_type"] = 'Total|A'
                            holder_dict["holder_name"] = "A=A1+A2"
                        elif c.text == "Any Other (specify)":
                            if holder_dict["holder_type"][-2:] == "|I" or holder_dict["holder_type"][-2:] == "|O":
                                holder_dict["holder_type"] = holder_dict["holder_type"].replace(
                                    "|I", "|O")
                            elif holder_dict["holder_type"][-3:] == "|I|" or holder_dict["holder_type"][-3:] == "|O|":
                                holder_dict["holder_type"] = holder_dict["holder_type"].replace(
                                    "|I|", "|O")
                            else:
                                if holder_dict["holder_type"][-1:] == "|":
                                    holder_dict["holder_type"] = holder_dict["holder_type"] + "O"
                                else:
                                    holder_dict["holder_type"] = holder_dict["holder_type"] + "|O"
                            holder_dict["holder_name"] = c.text
                        else:
                            if col_count == key_dict['holder_name']:
                                holder_dict["holder_name"] = c.text
                                if holder_dict["holder_type"][-1:] != "|":
                                    holder_dict["holder_type"] = holder_dict["holder_type"] + "|"
                            else:
                                try:
                                    holder_dict[index_dict[col_count]] = float(
                                        c.text.replace(",", ""))
                                except:
                                    pass
                        col_count = col_count + 1

                    if holder_dict['num_total_shares'] and flag:
                        # insert or update in the database
                        try:
                            # print ".",
                            db_commit_query("""
                            insert into tbl_holders (holder_name, holder_type, no_of_shareholders, no_of_fully_paid_shares, num_total_shares, perc_total_shares, num_pledged_shares, perc_pledged_shares, Ticker, period_id)
                            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """, (holder_dict['holder_name'], holder_dict['holder_type'], holder_dict['no_of_shareholders'], holder_dict['no_of_fully_paid_shares'], holder_dict['num_total_shares'], holder_dict['perc_total_shares'], holder_dict['num_pledged_shares'], holder_dict['perc_pledged_shares'], holder_dict['Ticker'], holder_dict['period_id']))
                        except:
                            pass
                            # Get the update query here
                except:
                    pass
            print ".",
        except:
            pass
        print "Added " + Ticker + str(period_id)
print "Period: " + str(period_id)

driver.quit()
