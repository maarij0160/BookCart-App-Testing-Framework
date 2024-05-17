import unittest
from RegisterTests.test_Register import UnitTestsRegister
from LoginTests.test_Login import UnitTestsLogin
from CartTests.test_Cart import UnitTestsCart
from CategoryTests.test_categories import UnitTestsCategories
from SearchTests.test_search import UnitTestsSearch
from CheckoutTests.test_Checkout import UnitTestsCheckout
from WishListTests.test_WishList import UnitTestsWishList
import HtmlTestRunner

if __name__ == "__main__":
    
    
    test_suite = unittest.TestSuite()
    test_suite.addTest(UnitTestsRegister("test_validRegister"))
    test_suite.addTest(UnitTestsRegister("test_InvalidRegister"))
    test_suite.addTest(UnitTestsLogin("test_validLogin"))
    test_suite.addTest(UnitTestsLogin("test_InvalidLogin"))
    test_suite.addTest(UnitTestsCheckout("test_checkout"))
    test_suite.addTest(UnitTestsCategories("test_click_category_biography"))
    test_suite.addTest(UnitTestsCategories("test_click_category_fiction"))
    test_suite.addTest(UnitTestsCategories("test_click_category_mystery"))
    test_suite.addTest(UnitTestsCategories("test_click_category_romance"))
    test_suite.addTest(UnitTestsCategories("test_click_category_fantasy"))
    test_suite.addTest(UnitTestsSearch("test_search"))
    test_suite.addTest(UnitTestsCart("test_addtocart"))
    test_suite.addTest(UnitTestsCart("test_incQty"))
    test_suite.addTest(UnitTestsCart("test_decQty"))
    test_suite.addTest(UnitTestsCart("test_deleteItem"))
    test_suite.addTest(UnitTestsCart("test_clearcart"))
    test_suite.addTest(UnitTestsWishList("test_addtoList"))
    test_suite.addTest(UnitTestsWishList("test_removefromList"))
    test_suite.addTest(UnitTestsWishList("test_clearList"))
    HtmlTestRunner.HTMLTestRunner(
        combine_reports=True,
        report_name="All Tests",
        report_title="All Tests",
    ).run(test_suite)

    