import unittest
import datetime
import events
import shutil
import os


class TestEvents(unittest.TestCase):

    def test_read_events(self):
        example_file_name = "events.example.yaml"
        file_name = "events_test.yaml"
        try:
            # Create a temp
            shutil.copyfile(example_file_name, file_name)

            # read events
            loaded_events = events.read_events(file_name)

            # assert results
            self.assertEqual(len(loaded_events), 1,
                             "number of events should be 1")
            first_event = loaded_events[0]
            self.assertDictEqual(first_event, {
                'name': 'Wedding anniversary',
                'date': datetime.date(2021, 12, 1),
                'notification': {
                    'title': '👰🏻\u200d♀️ Wedding Anniversary 💍',
                    'message': 'Happy anniversary'
                },
                'remind_on': [0, -1, -7]
            })
        finally:
            # Delete the temp file
            os.remove(file_name)

    def test_is_time_for_remind(self):
        original_date = datetime.datetime.strptime(
            '2021-12-15', "%Y-%m-%d").date()
        remind_on = [0, -1, -7]

        days_results = {
            '2022-12-09': False,    # -6
            '2022-12-10': False,    # -5
            '2022-12-14': True,     # -1
            '2022-12-15': True,     # 0
        }

        for day, expected_value in days_results.items():
            self.assertEqual(
                expected_value,
                events.is_time_for_remind(
                    original_date,
                    remind_on,
                    datetime.datetime.strptime(day, "%Y-%m-%d").date()
                )
            )


if __name__ == '__main__':
    unittest.main()
