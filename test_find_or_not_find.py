from selene import browser, have


def test_google_should_find_selene():
    browser.open('')
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_should_not_find():
    browser.open('')
    browser.element('[name="q"]').type(';ko/l.ik,gmjhndgbfvdcavzsbfxgn,vjhl.b/kn;ml/.k,jbmhvngcfbx').press_enter()
    browser.element('#center_col').should(have.text("По запросу ;ko/l.ik,gmjhndgbfvdcavzsbfxgn,vjhl.b/kn;ml/.k,jbmhvngcfbx ничего не найдено"))



