import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# 자유게시판의 첫번째 글 클릭해서 들어가서 주요 component 확인
def test_free_board_read():
    driver = webdriver.Chrome()

    driver.get("https://damoang.net/free")
    driver.implicitly_wait(5)

    title = driver.title
    assert title.startswith('자유게시판')

    list_element = driver.find_element(By.CSS_SELECTOR, ".da-link-block.subject-ellipsis")
    href = list_element.get_attribute("href")
    assert href.startswith("https://damoang.net/free/")  # 목록 item 링크 주소 확인
    list_title = list_element.get_attribute("innerText")

    ActionChains(driver).click(list_element).perform()  # 목록 item 클릭
    sleep(1)
    assert driver.current_url == href  # 이동한 page의 url과 전 링크주소 매칭 확인
    
    article_element = driver.find_element(By.ID, "bo_v")
    title = article_element.find_element(By.ID, "bo_v_title")
    assert title.get_attribute("innerText") == list_title  # 이전 목록 text와 article title 일치하는가?
    try:
        info_panel = article_element.find_element(By.ID, "bo_v_info")  # Info Panel 존재 여부
    except:
        assert False, f"Info panel (bo_v_info) not found"
    
    try:
        article_body = article_element.find_element(By.ID, "bo_v_atc")  # 글 body 존재 여부
    except:
        assert False, f"Article body (bo_v_atc) not found"
        
    try:
        comment_section = article_element.find_element(By.ID, "viewcomment")  # 답글 창 존재 여부
    except:
        assert False, f"Comment section (viewcomment) not found"

    driver.quit()
