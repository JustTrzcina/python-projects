from unittest import TestCase
from printer import Printer,PrinterError

class TestPrinter(TestCase):
    
    def setUp(self):
        self.printer = Printer(pages_per_s=2,capacity=300)

    def test_print_within_capacity(self):
        self.printer.print(25)

    def test_printing_outside_capacity_self(self):
        with self.assertRaises(PrinterError):
            self.printer.print(350)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages=10
        expected='Printed 10 pages in 5.00 seconds.'

        result = self.printer.print(pages)
        self.assertEqual(result,expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0,capacity=300)
        pages=11
        expected = 'Printed 11 pages in 3.67 seconds.'
        result = fast_printer.print(pages)
        self.assertEqual(result,expected)

    def test_multiple_prints(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)
    
    def test_multiple_runs_errors(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)