from selene import browser, be, have


def test_positive_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_negative_search(open_browser):
    search = 'sfпsdkрjfhdиsjf10jвfljfеlsdтf_01'
    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('[id="center_col"]').should(have.text(f'Your search - {search} - did not match any documents.'))
