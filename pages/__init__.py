from pages import (
    cart,
    contact_us,
    home,
    products,
    product_details,
    login,
    sign_up,
    account_created,
)


class Pages(object):

    def __init__(self, driver):
        self._driver = driver

    @property
    def cart(self):
        """Cart page

        :rtype: :class:`pages.cart.Cart`
        """
        return cart.Cart(self._driver)

    @property
    def contact_us(self):
        """Contact us page

        :rtype: :class:`pages.contact_us.ContactUs`
        """
        return contact_us.ContactUs(self._driver)

    @property
    def home(self):
        """Home page

        :rtype: :class:`pages.home.Home`
        """
        return home.Home(self._driver)

    @property
    def login(self):
        """Login page

        :rtype: :class:`pages.login.Login`
        """
        return login.Login(self._driver)

    @property
    def sign_up(self):
        """Sign up page

        :rtype: :class:`pages.sign_up.SignUp`
        """
        return sign_up.SignUp(self._driver)

    @property
    def account_created(self):
        """Account created page

        :rtype: :class:`pages.account_created.AccountCreated`
        """
        return account_created.AccountCreated(self._driver)

    @property
    def products(self):
        """Products page

        :rtype: :class:`pages.products.Products`
        """
        return products.Products(self._driver)

    @property
    def product_details(self):
        """Product details page

        :rtype: :class:`pages.product_details.ProductDetails`
        """
        return product_details.ProductDetails(self._driver)
