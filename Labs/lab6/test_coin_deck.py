import unittest
from unittest import TestCase
from unittest.mock import patch

import coin_desk


class Test_coin_desk(TestCase):

    @patch('coin_desk.get_coin_data')
    def test_rconvert(self, mock_get_coin_data):
        mock_rate=555
        example_api_response= {'bpi':{'USD':{'rate_float': mock_rate}}}
        mock_get_coin_data.side_effect=[example_api_response]
        result=coin_desk.convert(10)
        self.assertEqual(5550,result)


if __name__ == '__main__':
    unittest.main()
