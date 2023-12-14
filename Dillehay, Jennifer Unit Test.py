import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import Mock, patch
from Dillehay import LotChangeApp, LotCloseApp, FeedbackApp

class TestLotChangeApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def test_change_lot_confirmation(self):
        app = LotChangeApp(self.root)
        with patch.object(messagebox, 'askyesno', return_value=True):
            with patch.object(app, 'open_forms_page') as mock_open_forms:
                app.change_lot()
                mock_open_forms.assert_called_once()

    def test_change_lot_cancellation(self):
        app = LotChangeApp(self.root)
        with patch.object(messagebox, 'askyesno', return_value=False):
            with patch.object(messagebox, 'showinfo') as mock_showinfo:
                app.change_lot()
                mock_showinfo.assert_called_once_with("Lot Change", "Different item numbers usually mean different material or packaging.  Please check both DHRs before proceeding.")

    def tearDown(self):
        self.root.destroy()

class TestLotCloseApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def test_close_lot_confirmation(self):
        app = LotCloseApp(self.root)
        with patch.object(messagebox, 'askyesno', return_value=True):
            with patch.object(app, 'open_forms_page') as mock_open_forms:
                app.close_lot()
                mock_open_forms.assert_called_once()

    def test_close_lot_cancellation(self):
        app = LotCloseApp(self.root)
        with patch.object(messagebox, 'askyesno', return_value=False):
            with patch.object(messagebox, 'showinfo') as mock_showinfo:
                app.close_lot()
                mock_showinfo.assert_called_once_with("Lot Close", "Opening Forms.")

    def tearDown(self):
        self.root.destroy()

class TestFeedbackApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def test_feedback_submission(self):
        app = FeedbackApp(self.root)
        with patch.object(tk.Entry, 'get', return_value='Test Feedback'):
            with patch.object(app, 'show_feedback_page'):
                app.show_feedback_page()
                with patch.object(messagebox, 'showinfo') as mock_showinfo:
                    with patch.object(tk.Label, 'config') as mock_config:
                        app.feedback()
                        mock_showinfo.assert_called_once_with("User Feedback", "Test Feedback")
                        mock_config.assert_called_once_with(text="User Feedback: Test Feedback")

    def test_feedback_submission_empty(self):
        app = FeedbackApp(self.root)
        with patch.object(tk.Entry, 'get', return_value=''):
            with patch.object(app, 'show_feedback_page'):
                app.show_feedback_page()
                with patch('builtins.print') as mock_print:
                    app.feedback()
                    mock_print.assert_called_once_with("Please enter feedback.")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
