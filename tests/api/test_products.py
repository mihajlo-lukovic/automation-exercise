from schema import Schema, Or


class TestProducts:

    def test_get_list_of_products(self, api_client):
        """Get list of products

        Test steps:
        1. Get list of all products
        2. Verify status code
        3. JSON contains the key products
        4. The products array is not empty
        """
        # 1. Get list of all products
        json_data = api_client.get_products()

        # 2. Verify status code
        assert json_data['responseCode'] == 200, 'Response code is incorrect'

        # 3. JSON contains the key products
        assert 'products' in json_data, 'Key products is not in response'

        # 4. The products array is not empty
        assert len(json_data['products']) > 0, 'Products array is not empty'

    def test_verify_search_returns_valid_results(self, api_client):
        """Verify search returns valid results

        Body: { "search_product": "shirt" }

        Test steps:
        1. Send post request with given body
        2. Verify status code (200)
        3. Verify result contains only products that are relevant to the
        search term 'shirt'
        """
        # 1. Send post request with given body
        json_data = api_client.search_product(body={'search_product': 'shirt'})

        # 2. Verify status code (200)
        assert json_data['responseCode'] == 200, 'Response code is incorrect'

        # 3. Verify result contains only products that are relevant to the
        # search term 'shirt'
        for product in json_data['products']:
            name = product['name'].lower()
            category = product['category']['category'].lower()

            if 'shirt' not in name and 'shirt' not in category:
                raise AssertionError("Term 'shirt' not found in the product")

    def test_search_with_multiple_parameters(self, api_client):
        """Search with multiple parameters

        Body: {
        "search_product": "shirt", "brand": "Polo", "category": "Men"
        }

        Test steps:
        1. Send post request with given body
        2. Verify status code
        3. Verify that all returned products belong to the category
        “Men”, the brand “Polo”, and contain “shirt” in the name
        """
        expected_category = 'Men'
        expected_brand = 'Polo'
        expected_product = 'shirt'

        # 1. Send post request with given body
        json_data = api_client.search_product(
            body={
                'search_product': expected_product,
                'brand': expected_brand,
                'category': expected_category
            }
        )

        # 2. Verify status code
        assert json_data['responseCode'] == 200, 'Response code is incorrect'

        # 3. Verify that all returned products belong to the category
        # “Men”, the brand “Polo”, and contain “shirt” in the name
        for product in json_data['products']:
            assert (
                    product['category']['usertype']['usertype'] ==
                    expected_category
            ), (f'Category {expected_category} is not equal '
                f'with {product['category']['usertype']['usertype']}')

            assert (
                    product['brand'] == expected_brand
            ), f'Brand {expected_brand} is not equal with {product['brand']}'

            assert (
                    expected_product in product['name'].lower()
            ), f'Product {expected_product} not found in the product name'

    def test_product_price_range_validation(self, api_client):
        """Verify that all returned products are within an expected price range

        Body: { "search_product": "shirt" }

        Test steps:
        1. Send a POST request with the body above
        2. Verify the response status code
        3. Iterate through all products in the response and
        verify that each product’s price is between 200 and 1500
        """
        # 1. Send a POST request with the body above
        json_data = api_client.search_product(body={'search_product': 'shirt'})

        # 2. Verify the response status code
        assert json_data['responseCode'] == 200, 'Response code is incorrect'

        # 3. Iterate through all products in the response and
        # verify that each product’s price is between 200 and 1500
        for product in json_data['products']:
            price = int(product['price'].split(' ')[-1])
            assert 200 <= price <= 1500

    def test_products_response(self, api_client):
        """Response validation

        Test steps:
        1. Send a GET request to /api/productsList
        2. Iterate through all products in the response
        3. Verify that each product contains the following fields and
        data types:
        id (number), name (string), price (number or string), brand (string),
        category (string)
        """
        # 1. Send a GET request to /api/productsList
        json_data = api_client.get_products()

        expected_product_schema = Schema({
            'id': int,
            'name': str,
            'price': Or(str, float),
            'brand': str,
            'category': {
                'usertype': {
                    'usertype': str
                },
                'category': str
            }
        })

        # 2. Iterate through all products in the response
        for product in json_data['products']:
            # 3. Verify that each product contains the following fields and
            # data types:
            # id (number), name (string), price (number or string),
            # brand (string), category (string)
            expected_product_schema.validate(product)

    def test_create_update_delete_user(self, api_client, mock_data):
        """Create, update and delete user

        Test case:
        1. Send POST request to /api/createAccount for user creation
        2. Verify status code (201)
        3. Verify success message in response
        4. Send PUT request to /api/updateAccount for user update
        5. Verify status code (200)
        6. Verify success message in response
        7. Send DELETE request to /api/deleteAccount for user deletion
        8. Verify status code (200)
        9. Verify success message in response
        """
        # Get user details
        user_details = {
            'name': mock_data['name'],
            'email': mock_data['email'],
            'password': mock_data['password'],
            'title': mock_data['title'],
            'birth_date': mock_data['birth_date'],
            'birth_month': mock_data['birth_month'],
            'birth_year': mock_data['birth_year'],
            'firstname': mock_data['first_name'],
            'lastname': mock_data['last_name'],
            'address1': mock_data['address1'],
            'country': mock_data['country'],
            'state': mock_data['state'],
            'city': mock_data['city'],
            'zipcode': mock_data['zipcode'],
            'mobile_number': mock_data['mobile_number']
        }

        # 1. Send POST request to /api/createAccount for user creation
        json_data = api_client.create_user(body=user_details)

        # 2. Verify status code (201)
        assert json_data['responseCode'] == 201, 'Response code is incorrect'

        # 3. Verify success message in response
        assert (
                json_data['message'] == 'User created!'
        ), 'Response message is incorrect'

        # Update user details address1
        user_details['address1'] = 'Test'

        # 4. Send PUT request to /api/updateAccount for user update
        json_data = api_client.update_user(body=user_details)

        # 5. Verify status code (200)
        assert json_data['responseCode'] == 200, 'Response code is incorrect'

        # 6. Verify success message in response
        assert (
                json_data['message'] == 'User updated!'
        ), 'Response message is incorrect'

        # 7. Send DELETE request to /api/deleteAccount for user deletion
        json_data = api_client.delete_user(
            email=mock_data['email'],
            password=mock_data['password']
        )

        # 8. Verify status code (200)
        assert json_data['responseCode'] == 200, 'Response code is incorrect'

        # 9. Verify success message in response
        assert (
                json_data['message'] == 'Account deleted!'
        ), 'Response message is incorrect'
