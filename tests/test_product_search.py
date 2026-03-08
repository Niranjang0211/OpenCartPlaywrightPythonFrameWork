
from config import Config
from pages.home_page import HomePage
from pages.search_result import SearchResultsPage
from playwright.sync_api import expect
import pytest

@pytest.mark.regression
@pytest.mark.sanity
def test_product_search(page):

    product_name = Config.product_name
    home_page=HomePage(page)
    search_result_page = SearchResultsPage(page)

    home_page.enter_product_name(product_name)
    home_page.click_search()

    expect(search_result_page.get_search_results_page_header()).to_be_visible(timeout=3000)
    expect(search_result_page.is_product_exist(product_name)).to_be_visible(timeout=3000)
